# Account 1 wants to buy NFT that Account 2 is selling for 5 ALGOs.
# Create NFT that Account 2 will sell
# Create opt-in transaction from Account 2 to Account 1
# Creat Group transaction

from algosdk import account, mnemonic, transaction
from algosdk.v2client import algod
from typing import Dict, Any

# Load the API key from the environment file
api_key = ''

# example: ALGOD_CREATE_CLIENT
# Create a new algod client, configured to connect to our local sandbox
algod_address = "https://testnet-api.algonode.cloud"
algod_client = algod.AlgodClient(api_key, algod_address)

mn = 'forum eagle priority become joke alcohol false kiwi task orphan town day entire height view half strategy piece winner decorate leaf guide oyster about garage'
private_key = mnemonic.to_private_key(mn)
# print(f"Base64 encoded private key: {private_key}")
address_2 = account.address_from_private_key(private_key)
print(f"Address: {address_2}")
address_1 = '4D5QWA76FIBL7FH6DX7FBRU5TZHE2RPINZMCYWVDJHHFDFTZVUPH64T66M'

# Account 2 creates an NFT called `ESG` with a total supply
# of 1 units and sets itself to the freeze/clawback/manager/reserve roles
sp = algod_client.suggested_params()
txn = transaction.AssetConfigTxn(
    sender=address_2,
    sp=sp,
    default_frozen=False,
    unit_name="ESG",
    asset_name="ESG Token",
    manager=address_2,
    reserve=address_2,
    freeze=address_2,
    clawback=address_2,
    url="https://www.weforum.org/reports/annual-report-2021-2022",
    total=1,
    decimals=0,
)

# Sign with secret key of creator
stxn = txn.sign(private_key)
# Send the transaction to the network and retrieve the txid.
txid = algod_client.send_transaction(stxn)
print(f"Sent asset create transaction with txid: {txid}")
# # Wait for the transaction to be confirmed
results = transaction.wait_for_confirmation(algod_client, txid, 4)
print(f"Result confirmed in round: {results['confirmed-round']}")

# grab the asset id for the asset we just created
created_asset = results["asset-index"]
print(f"Asset ID created: {created_asset}")

# example: ASSET_INFO
# Retrieve the asset info of the newly created asset
asset_info = algod_client.asset_info(created_asset)
asset_params: Dict[str, Any] = asset_info["params"]
print(f"Asset Name: {asset_params['name']}")
print(f"Asset params: {list(asset_params.keys())}")
# example: ASSET_INFO


# example: ASSET_OPTIN
sp = algod_client.suggested_params()
receiver_address = "4D5QWA76FIBL7FH6DX7FBRU5TZHE2RPINZMCYWVDJHHFDFTZVUPH64T66M"
# Create opt-in transaction
# asset transfer from me to me for asset id we want to opt-in to with amt==0
optin_txn = transaction.AssetOptInTxn(
    sender="4D5QWA76FIBL7FH6DX7FBRU5TZHE2RPINZMCYWVDJHHFDFTZVUPH64T66M", sp=sp, index=created_asset
)
signed_optin_txn = optin_txn.sign(private_key="+5pItA3OJ4+IJ/1k3knk2SMvy1IZxB89iWPgaPyAr8Xg+wsD/ioCv5T+Hf5Qxp2eTk1F6G5YLFqjSc5RlnmtHg==")
txid = algod_client.send_transaction(signed_optin_txn)
print(f"Sent opt in transaction with txid: {txid}")

# Wait for the transaction to be confirmed
results = transaction.wait_for_confirmation(algod_client, txid, 4)
print(f"Result confirmed in round: {results['confirmed-round']}")
# example: ASSET_OPTIN

# example: ATOMIC_CREATE_TXNS
# payment from account 1 to account 2
txn_1 = transaction.PaymentTxn(
    address_1, sp, address_2, 5000000
)

# example: ASSET_XFER
sp = algod_client.suggested_params()
# Create transfer transaction
xfer_txn = transaction.AssetTransferTxn(
    sender=address_2,
    sp=sp,
    receiver=address_1,
    amt=1,
    index=created_asset,
)
signed_xfer_txn = xfer_txn.sign(private_key="3ULRVT8hPBhIanvwNqfMgcOlqn1+aLYe6feRUz+ezXPDzte2rqRWimeKhmDhEbpsHVRglCkrlTqjuegC6JhnVw==")
txid = algod_client.send_transaction(signed_xfer_txn)
print(f"Sent transfer transaction with txid: {txid}")
# example: ATOMIC_CREATE_TXNS


# example: ATOMIC_GROUP_TXNS
# Assign group id to the transactions (order matters!)
transaction.assign_group_id([txn_1, xfer_txn])
# Or, equivalently
# get group id and assign it to transactions
# gid = transaction.calculate_group_id([txn_1, txn_2])
# txn_1.group = gid
# txn_2.group = gid
# example: ATOMIC_GROUP_TXNS

# example: ATOMIC_GROUP_SIGN
# sign transactions
stxn_1 = txn_1.sign(private_key)
stxn_2 = xfer_txn.sign("3ULRVT8hPBhIanvwNqfMgcOlqn1+aLYe6feRUz+ezXPDzte2rqRWimeKhmDhEbpsHVRglCkrlTqjuegC6JhnVw==")
# example: ATOMIC_GROUP_SIGN

# example: ATOMIC_GROUP_ASSEMBLE
# combine the signed transactions into a single list
signed_group = [stxn_1, stxn_2]
# example: ATOMIC_GROUP_ASSEMBLE

# example: ATOMIC_GROUP_SEND

# Only the first transaction id is returned
tx_id = algod_client.send_transactions(signed_group)

# wait for confirmation
result: Dict[str, Any] = transaction.wait_for_confirmation(algod_client, tx_id, 4)
print(f"txID: {tx_id} confirmed in round: {result.get('confirmed-round', 0)}")
# example: ATOMIC_GROUP_SEND

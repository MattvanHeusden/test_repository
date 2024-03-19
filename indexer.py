from algosdk.v2client import indexer
import json
import datetime

# Create a new indexer client, configured to connect to a node e.g. https://testnet-algorand.api.purestake.io/idx2
    # or https://testnet-idx.algonode.cloud
indexer_address = "https://testnet-idx.algonode.cloud"
indexer_token = ""
headers = ""
indexer_client = indexer.IndexerClient(indexer_token, indexer_address, headers)

txid = "O7EONEOHDYCGASUR4OIOPW73WMOVFWDHZUQ4MJOOZL7PINN54TZA"


# example: INDEXER_SEARCH_TRANSACTIONS_BY_ID
    # Read the transaction by ID
try:
    txn1 = indexer_client.transaction(txid)
    if txn1 is not None:
            print("Transaction information tx1: {}".format(json.dumps(txn1, indent=4)))
    else:
            print("Transaction not found")
        # indexer search by address search_transactions_by_address
except Exception as err:
        print(err)
    # example: INDEXER_SEARCH_TRANSACTIONS_BY_ID
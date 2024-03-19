from pyteal import *

alex_votes = App.globalGet(Bytes("alex_votes"))
bob_votes = App.globalGet(Bytes("bob_votes"))
max_votes = Int(100)

handle_creation = Seq(
    App.globalPut(Bytes("Votes"), Int(0)),
    App.globalPut(Bytes("alex_votes"), Int(0)),
    App.globalPut(Bytes("bob_votes"), Int(0)),
    Approve(),
)


def vote_for_candidate(candidate: str):
    return Seq(
        If(
            alex_votes + bob_votes < max_votes,
            Seq(
                App.globalPut(
                    Bytes("alex_votes"),
                    If(candidate == "alex", alex_votes + Int(1), alex_votes),
                ),
                App.globalPut(
                    Bytes("bob_votes"),
                    If(candidate == "bob", bob_votes + Int(1), bob_votes),
                ),
                Approve(),
            ),
            Reject(Bytes("Vote limit reached")),
        )
    )


def read_votes():
    return Return(App.globalGet(Bytes("alex_votes")), App.globalGet(Bytes("bob_votes")))


router = Router(
    "Mock Voting System",
    BareCallActions(no_op=OnCompleteAction.create_only(handle_creation)),
)


@router.method
def vote(*, candidate: str):
    return vote_for_candidate(candidate)


@router.method
def read():
    return read_votes()


if __name__ == "__main__":
    import os
    import json

    path = os.path.dirname(os.path.abspath(__file__))
    approval, clear, contract = router.compile_program(version=8)

    # Dump out the contract as json that can be read in by any of the SDKs
    with open(os.path.join(path, "artifacts/contract.json"), "w") as f:
        f.write(json.dumps(contract.dictify(), indent=2))

    # Write out the approval and clear programs
    with open(os.path.join(path, "artifacts/approval.teal"), "w") as f:
        f.write(approval)

    with open(os.path.join(path, "artifacts/clear.teal"), "w") as f:
        f.write(clear)
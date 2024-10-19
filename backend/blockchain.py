from pytezos import pytezos

class VotingFundContract:
    def __init__(self):
        self.pytezos = pytezos.using(shell='https://granadanet.smartpy.io', key='your_private_key')

    def donate(self, wallet, amount):
        contract = self.pytezos.contract('your_contract_address')
        return contract.donate().with_amount(amount).send()

    def create_request(self, amount, purpose):
        contract = self.pytezos.contract('your_contract_address')
        return contract.create_request(amount=amount, purpose=purpose).send()

    def vote(self, wallet, request_id, vote):
        contract = self.pytezos.contract('your_contract_address')
        return contract.vote(request_id=request_id, vote=vote).send()

    def release_funds(self, request_id):
        contract = self.pytezos.contract('your_contract_address')
        return contract.release_funds(request_id=request_id).send()

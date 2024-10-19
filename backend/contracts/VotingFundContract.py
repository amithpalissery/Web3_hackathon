import smartpy as sp

class VotingFundContract(sp.Contract):
    def __init__(self):
        self.init(
            fund_balance = sp.tez(0), 
            requests = sp.map(tkey=sp.TNat, tvalue=sp.record(amount=sp.tez, purpose=sp.string, votes_for=sp.nat, votes_against=sp.nat, status=sp.string)),
            donors = sp.map(tkey=sp.TAddress, tvalue=sp.nat),
            next_request_id = 0
        )

    @sp.entry_point
    def donate(self, params):
        self.data.donors[sp.sender] = self.data.donors.get(sp.sender, 0) + sp.amount
        self.data.fund_balance += sp.amount

    @sp.entry_point
    def create_request(self, params):
        sp.verify(sp.sender == sp.admin, "Only admin can create requests")
        self.data.requests[self.data.next_request_id] = sp.record(
            amount=params.amount, 
            purpose=params.purpose, 
            votes_for=0, 
            votes_against=0, 
            status="Pending"
        )
        self.data.next_request_id += 1

    @sp.entry_point
    def vote(self, params):
        sp.verify(self.data.donors.contains(sp.sender), "Only donors can vote")
        request = self.data.requests[params.request_id]
        sp.verify(request.status == "Pending", "Voting has ended")
        
        if params.vote:
            request.votes_for += 1
        else:
            request.votes_against += 1
        
        total_votes = request.votes_for + request.votes_against
        if total_votes > (len(self.data.donors) // 2):
            if request.votes_for > request.votes_against:
                request.status = "Approved"
            else:
                request.status = "Rejected"

    @sp.entry_point
    def release_funds(self, params):
        request = self.data.requests[params.request_id]
        sp.verify(request.status == "Approved", "Request not approved")
        sp.send(sp.sender, request.amount)
        self.data.fund_balance -= request.amount

# Compile and test the contract in the SmartPy IDE or SmartPy CLI

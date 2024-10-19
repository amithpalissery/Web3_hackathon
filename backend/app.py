from flask import Flask, request, jsonify
from pytezos import pytezos
from wallet import Wallet
from blockchain import VotingFundContract

app = Flask(__name__)

# Initialize wallet and blockchain contract instances
wallet = Wallet()
contract = VotingFundContract()

@app.route('/create-wallet', methods=['POST'])
def create_wallet():
    wallet_data = wallet.create_new_wallet()
    return jsonify(wallet_data)

@app.route('/donate', methods=['POST'])
def donate():
    data = request.get_json()
    donation_response = contract.donate(data['wallet'], data['amount'])
    return jsonify(donation_response)

@app.route('/create-request', methods=['POST'])
def create_request():
    data = request.get_json()
    request_response = contract.create_request(data['amount'], data['purpose'])
    return jsonify(request_response)

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    vote_response = contract.vote(data['wallet'], data['request_id'], data['vote'])
    return jsonify(vote_response)

@app.route('/release-funds', methods=['POST'])
def release_funds():
    data = request.get_json()
    release_response = contract.release_funds(data['request_id'])
    return jsonify(release_response)

if __name__ == '__main__':
    app.run(debug=True)

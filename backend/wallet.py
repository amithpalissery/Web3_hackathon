from pytezos import pytezos

class Wallet:
    def __init__(self):
        self.pytezos = pytezos

    def create_new_wallet(self):
        key = pytezos.key.generate()
        wallet = {
            'public_key': key.public_key(),
            'private_key': key.secret_key(),
            'address': key.public_key_hash()
        }
        return wallet

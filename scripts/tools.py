from brownie import (
    accounts,
    network,
    config
)

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork', 'mainnet-fork-dev']
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']

def get_account(index=None, id=None):
    """Retrieve an account depending of the network"""
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or
        network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        # To retrieve a ganache account
        return accounts[0]
    
    # To retrieve your own address
    return accounts.add(config['wallets']['from_key'])
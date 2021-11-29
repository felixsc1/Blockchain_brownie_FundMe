from brownie import network, config, accounts, MockV3Aggregator

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'local-ganache']

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        print('Deploying Mocks...')
        MockV3Aggregator.deploy(DECIMALS,
                                STARTING_PRICE, {'from': get_account()})
        print('Mocks Deployed!')

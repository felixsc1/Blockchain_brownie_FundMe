from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()

    # if we are on a persistent network like rinkeby, use associated oracle address,
    # otherwise deploy mocks.
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config['networks'][network.show_active(
        )]['eth_usd_pricefeed']
    else:
        print(f'The active network is {network.show_active()}')
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    # pass price feed address to our contract.
    fund_me = FundMe.deploy(price_feed_address,
                            {'from': account}, publish_source=config['networks'][network.show_active()].get("verify"),)
    print(f'Contract deployed to {fund_me.address}')
    return fund_me


def main():
    deploy_fund_me()

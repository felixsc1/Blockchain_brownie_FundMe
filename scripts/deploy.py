from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()

    # if we are on a persistent network like rinkeby, use associated oracle address,
    # otherwise deploy mocks.
    if network.show_active() != "development":
        price_feed_address = config['networks'][network.show_active(
        )]['eth_usd_pricefeed']

    # pass price feed address to our contract.
    fund_me = FundMe.deploy(price_feed_address,
                            {'from': account}, publish_source=True)
    print(f'Contract deployed to {fund_me.address}')


def main():
    deploy_fund_me()

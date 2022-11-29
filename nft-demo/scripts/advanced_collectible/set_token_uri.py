from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_breed, get_account


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectible = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectible} tokenIds")
    for token_id in range(number_of_collectible):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting token URI of {token_id}")
            set_token_uri(token_id, advanced_collectible)


def set_token_uri(token_id, nft_contract):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button")

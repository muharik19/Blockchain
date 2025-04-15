1. Setup a [local ganache chain](https://www.trufflesuite.com/ganache)

2. Install Brownie

```bash
python -m pip install --user pipx
python -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
Or, if that doesn't work, via pip
```bash
pip install eth-brownie
```

3. Clone this
```bash
git clone https://github.com/muharik19/Blockchain.git
cd brownie_simple_storage
```
4. Add your metamask to the brownie accounts at the `0` index

```bash
brownie accounts new 0
```
You'll be prompted to add your private key:
`0xa5555555555555a09215803a6b540f1e054797eeda2eec6d49076760d48e7589`
And a password, and you can see your new added account with `brownie accounts list`

Or, export your `PRIVATE_KEY` as an environment variable, and uncomment the line:
```python
# account = accounts.add(config["wallets"]["from_key"])
```
and comment the line:
```python
account = accounts[0]
```

5. Testing

```bash
brownie test
```

6. Running scripts development

```bash
brownie run scripts/deploy.py --network development
```

7. Check network list

```bash
brownie networks list
```

8. Create account new

```bash
brownie accounts new name-account
```

9. Check accounts list

```bash
brownie accounts list
```

10. Deploy to a testnet
Add your `WEB3_INFURA_PROJECT_ID` from [Infura](https://infura.io/) to your `.env` and run 
```bash
source .env
``` 
To set your environment variable. You can check you've done it correctly with:
```bash
echo $WEB3_INFURA_PROJECT_ID
```
Change the `deploy_simple_storage` function in `deploy.py` to look like:
```
account = accounts.add(config["wallets"]["from_key"])
# account = accounts.load("id")
# account = accounts[0]
```

11. Check active endpoints infura
- [Infura active endpoints](https://developer.metamask.io/key/active-endpoints)

10. Running scripts sepolia

```bash
# network list Ethereum Infura
brownie run scripts/deploy.py --network sepolia
```

Make sure you have some testnet ETH. You can find faucets in the [Chainlink Documenatation](https://docs.chain.link/docs/link-token-contracts/)



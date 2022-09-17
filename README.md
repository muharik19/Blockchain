1. Clone this repo
```
git clone https://github.com/muharik19/Blockchain.git
cd web3_py_simple_storage
```
2. Setup a [local ganache chain](https://www.trufflesuite.com/ganache)
3. Install requirements
```bash
pip install
```
4. Set your private keys and address, and adjust this section appropriately:
```python
# For connecting to ganache
w3 = Web3(Web3.HTTPProvider(os.getenv("PROVIDER")))
chain_id = os.getenv("CHAIN_ID")
my_address = os.getenv("MY_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
```
To set your private key as an environment variable, run `export PRIVATE_KEY=0xasdfasdfasfdasf`. If you're confused on how environment variables work, just set:
```python
private_key = "0xYOUR_KEY_HERE"
```
5. Run 
```
python deploy.py
```

To run on a testnet, just change these variables to whatever testnet you want to work with:
```
w3 = Web3(Web3.HTTPProvider(os.getenv("PROVIDER")))
chain_id = os.getenv("CHAIN_ID")
my_address = os.getenv("MY_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
```
And make sure you have testnet ETH for whatever testnet you're on!
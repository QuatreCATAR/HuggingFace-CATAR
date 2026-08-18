import bittensor as bt
from miners.miner import MinerCATAR, get_config

config = get_config()
miner = MinerCATAR(config)

synapse = bt.Synapse(prompt="Test CATAR")
response = miner.forward(synapse)

print("=== Résultat CATAR ===")
for key, value in response.items():
    print(f"{key}: {value}")

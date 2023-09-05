
import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

def calculate_hash(block):
    block_string = f"{block.index}{block.timestamp}{block.data}{block.previous_hash}"
    return hashlib.sha256(block_string.encode()).hexdigest()

def add_block(data, blockchain):
    last_block = blockchain[-1]
    new_index = last_block.index + 1
    new_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    new_block = Block(new_index, new_timestamp, data, calculate_hash(last_block))
    blockchain.append(new_block)

def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        if blockchain[i].previous_hash != calculate_hash(blockchain[i-1]):
            return False
    return True

# Create the Genesis Block
genesis_block = Block(0, "2023-01-01 00:00:00", "Genesis Block", "0")
blockchain = [genesis_block]

# Add some blocks
add_block("Block 1 Data", blockchain)
add_block("Block 2 Data", blockchain)
add_block("Block 3 Data", blockchain)

# Validate the blockchain
if is_chain_valid(blockchain):
    print("Blockchain is valid")
else:
    print("Blockchain is not valid")

# Print the blockchain
for block in blockchain:
    print(f"Index: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Previous Hash: {block.previous_hash}")

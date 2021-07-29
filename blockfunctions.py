# Modules used are hashlib: for hashing and deque: for Queue. I did not want to write a new queue when the wheel was already invented

import hashlib
from collections import deque

# I am choosing the sha256 algorithm here as a global configurable. The intention is it can be changed at any time
hash_algorithm = hashlib.sha256

''' The Merkle node defines a node in the merkle tree. It generates a node which points to its primitive nodes(None if leaf nodes) along with the combined transaction hash. '''
class MerkleNode:
    def __init__(self, transaction_hash, left, right):
        self.transaction_hash = transaction_hash
        self.left = left or None
        self.right = right or None

def generate_hash(transaction):

    # Generate the hash for a single transaction

    return hash_algorithm(transaction.encode()).hexdigest()

def create_merkle_nodes(transactions):
    
    # Use the hash values from the transactions to create merkle nodes.
    merkle_nodes = []
    for transaction in transactions:
        merkle_nodes.append(MerkleNode(transaction, None, None))
    return merkle_nodes

def generate_padding_node():
    
    # The merkle tree operates on pairs. This function generates a padding node to make sure that the nodes are always even numbers. 
    hash = generate_hash('0')
    return MerkleNode(hash, None, None)
            
# Generating the Merkle tree.
def generate_merkle_hash(transactions):
    transaction_hash_array = []
    for transaction in transactions:
        transaction_hash_array.append(generate_hash(transaction))

    merkle_nodes = deque(create_merkle_nodes(transaction_hash_array))

    while len(merkle_nodes) > 1:
        if len(merkle_nodes) % 2 != 0:
            merkle_nodes.append(generate_padding_node())
        length = len(merkle_nodes)
        for nodeindex in range(0, (length//2)):
            node1 = merkle_nodes.popleft()
            node2 = merkle_nodes.popleft()
            new_hash = generate_hash(node1.transaction_hash + node2.transaction_hash)
            node = MerkleNode(new_hash, node1, node2)
            merkle_nodes.append(node)

    return merkle_nodes[0].transaction_hash




        



    



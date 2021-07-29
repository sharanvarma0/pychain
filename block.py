import random
import blockfunctions
import block_header as header

class Block:
    def __init__(self, previous_block_hash, transactions):
        self.hash = blockfunctions.generatehash(previous_block_hash)
        self.header = header(previous_block_hash, transactions)
        self.transaction_count = len(transactions)
        self.transactions = transactions
        


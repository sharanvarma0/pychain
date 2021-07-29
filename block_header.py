import datetime
from blockfunctions import *

class Header:
    def __init__(previous_hash, transactions):
        self.version = conf.VERSION
        self.previous_hash = previous_hash
        self.merkle_root_hash = generatemerklehash(transactions)
        self.timestamp = datetime.datetime.now()

    def get_version(self):
        return self.version

    def get_merkle_hash(self):
        return self.merkle_root_hash

    def get_time(self):
        return self.timestamp




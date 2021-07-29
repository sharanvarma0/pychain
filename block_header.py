import datetime
from blockfunctions import *

class Header:
    def __init__(previous_hash, transactions):
        self.version = conf.VERSION
        self.previous_hash = previous_hash
        self.merkle_root_hash = generatemerklehash(transactions)
        self.timestamp = datetime.datetime.now()

    def getversion(self):
        return self.version

    def getmerklehash(self):
        return self.merkle_root_hash

    def gettime(self):
        return self.timestamp




class WalletDto:
    def __init__(self):
        self.account_map = {}

    def getAccountMap(self):
        return self.account_map

    def setAccountMap(self, account_map):
        self.account_map = account_map

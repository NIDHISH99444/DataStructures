class WalletDao:
    def __init__(self):
        self.account_map = {}

    @property
    def account_map(self):
        return self._account_map

    @account_map.setter
    def account_map(self, account_map):
        self._account_map = account_map

from apis.blackfrost import resolveAdaHandle, fetchBalance

class Wallet:
    def __init__(self, identifier):
        if identifier[0] != '$':
            self.handle = ''
            self._addr = identifier
            self._balance = 0
            return
        
        self.handle = identifier[1:] # remove '$' prefix
        self._addr = resolveAdaHandle(self.handle)
        self._balance = 0
        return
    
    def update_balance(self):
        self._balance = fetchBalance(self._addr)
        return self._balance
    
    def get_balance(self) -> int:
        return round(self._balance, 2)
    
    def get_addr(self) -> str:
        return self._addr

    
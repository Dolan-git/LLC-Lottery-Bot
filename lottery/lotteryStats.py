from table2ascii import table2ascii as t2a, PresetStyle
from wallet import Wallet
from .tickets import Tickets

# obtained from the LLC whitepaper: 
# https://drive.google.com/file/d/1Qw8tP81lHhzxFwr0IEQXOyy84UaRBgaD/view 
TOTAL_MASKS = 4444
PRIZE_DISTRIBUTION_BREAKDOWN = {
    'Match first 1' : 0.02,
    'Match first 2' : 0.03,
    'Match first 3': 0.05,
    'Match first 4': 0.1,
    'Match first 5': 0.2,
    'Match first 6': 0.4,
    'Rollover to next draw': 0.1,
    'Mask Holders': 0.06,
    'Product Teams': 0.04
}

class LotteryStatistics(object):
    def __new__(cls, *args, **kwargs):
        # singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(LotteryStatistics, cls).__new__(cls)
        return cls.instance

    def __init__(self, *args, **kwargs):
        if hasattr(self, 'wallet'):
            return

        self.tickets = Tickets()
        self.wallet = Wallet(kwargs.get('wallet_identifier', '$LLC.LOTTERY'))
        self.set_prize_breakdown()
    
    def set_prize_breakdown(self):
        breakdown = {}
        total_pool = self.wallet.get_balance()

        for k, v in PRIZE_DISTRIBUTION_BREAKDOWN.items():
            breakdown[k] = round(v * total_pool, 2)
        
        self.breakdown = breakdown
    
    def get_payout_per_mask(self) -> int:
        return round(self.breakdown['Mask Holders'] / TOTAL_MASKS, 2)
    
    def __repr__(self) -> str:
        body = [['Total', self.wallet.get_balance()]]
        for k, v in self.breakdown.items():
            body.append([k, v])
        
        body.append(['Per Mask', self.get_payout_per_mask()])
        body.append(['Tickets Sold', self.tickets.minted])

        return t2a(
            header=['','₳'],
            body=body,
            style=PresetStyle.thin_compact
        )
    


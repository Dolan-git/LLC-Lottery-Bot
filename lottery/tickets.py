from apis.opencnft import fetchTicketsMinted

class Tickets:
    def __init__(self):
        self.update_tickets_minted()
    
    def update_tickets_minted(self):
        self.minted = fetchTicketsMinted()


import email
from payment import Payment

class paypal(Payment):
    email = str
    
    def __init__(self, amount, kind) -> None:
        super().__init__(amount, kind, email)
        self.email = email
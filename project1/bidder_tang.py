import random

class Bidder:
    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.__balance = 0
        self.history = {}

    def bid(self, user_id):
        bid_amount = random.uniform(0, 1)
        return round(bid_amount, 3)

    def notify(self, auction_winner, price, clicked):
        if auction_winner:
            self.__balance += 1 if clicked else 0
            self.__balance -= price

        # Existing logging code...
        unique_key = f"{random.randint(1, 1000)}_{random.randint(1, 1000)}"
        self.history[unique_key] = {'won': auction_winner, 'price': price, 'clicked': clicked}

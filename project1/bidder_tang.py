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
        print(f"Notification received: {'Won' if auction_winner else 'Lost'} the auction.")
        print(f"Price paid by winner: {price}")
        print(f"Ad clicked: {clicked}")

        if auction_winner:
            self.__balance += 1 if clicked else 0
            self.__balance -= price

        # Use some way to generate a unique key for each round
        # For example, a combination of the round number and user_id
        unique_key = f"{random.randint(1, 1000)}_{random.randint(1, 1000)}"
        self.history[unique_key] = {'won': auction_winner, 'price': price, 'clicked': clicked}

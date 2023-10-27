import random

class Bidder:
    def __init__(self, num_users, num_rounds):
        """
        Initialize the bidder with the total number of users and rounds.
        """
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.__balance = 0  # Private variable to store the balance of the bidder
        self.history = {}  # Dictionary to store the history of bids and clicks

    def __repr__(self):
        return f"Bidder: {self.__balance}"

    def __str__(self):
        return f"Bidder: {self.__balance}"

    def bid(self, user_id):
        """
        Submit a bid for a particular user.
        """
        bid_amount = random.uniform(0, 1)
        return round(bid_amount, 3)  # Rounding to 3 decimal places as specified

    def notify(self, auction_winner, price, clicked, user_id):
        """
        Update the bidder based on the auction results.
        """
        if auction_winner:
            self.__balance += 1 if clicked else 0  # Increment balance if the ad was clicked
            self.__balance -= price  # Decrement balance by the cost of the ad

        # Update history
        self.history[user_id] = {'won': auction_winner, 'price': price, 'clicked': clicked}

import random

class Bidder:
    def __init__(self, num_users, num_rounds):
        """
        Initialize the bidder with the total number of users and rounds.
        
        Args:
            num_users (int): The total number of users in the auction.
            num_rounds (int): The total number of auction rounds.
        """
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.__balance = 0  # Private variable to store the balance of the bidder
        self.history = {}  # Dictionary to store the history of clicks

    def __repr__(self):
        return f"Bidder: {self.__balance}"

    def __str__(self):
        return f"Bidder: {self.__balance}"

    def bid(self, user):
        """
        Submit a bid for a particular user.
        """
        return random.uniform(0, 1)  # Initial algorithm of bidding for a random amount between 0 and 1

    def notify(self, auction_winner, price, clicked, user_id):
        """
        Update the bidder based on the auction results.

        Args:
            auction_winner (bool): True if this bidder won the auction, False otherwise.
            price (float): The price of the ad.
            clicked (bool): True if the ad was clicked, False otherwise.
            user_id (int): The ID of the user to whom the ad was shown.
        """
        if auction_winner:
            self.__balance += 1 if clicked else 0  # Increment balance if the ad was clicked
            self.__balance -= price  # Decrement balance by the cost of the ad

        # Update history
        self.history[user_id] = clicked

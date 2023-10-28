import random


class Bidder:
    """Represents a bidder in the auction system."""

    def __init__(self, num_users, num_rounds):
        """Initialize the Bidder instance.

        Args:
            num_users (int): The number of users in the auction.
            num_rounds (int): The number of auction rounds.
        """
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.__balance = 0
        self.history = {}

    def bid(self, user_id):
        """Generate a random bid.

        Args:
            user_id (int): The user ID to bid for.

        Returns:
            float: The generated bid amount.
        """
        bid_amount = random.uniform(0, 1)
        return round(bid_amount, 3)

    def notify(self, auction_winner, price, clicked):
        """Update balance and history based on auction outcome.

        Args:
            auction_winner (bool): True if this bidder won, False otherwise.
            price (float): The price paid in the auction.
            clicked (bool or None): Whether the ad was clicked, if this bidder won.
        """
        if auction_winner:
            self.__balance += 1 if clicked else 0  # Reward for the click
            self.__balance -= price  # Payment for the ad spot

        unique_key = f"{random.randint(1, 1000)}_{random.randint(1, 1000)}"
        self.history[unique_key] = {
            "won": auction_winner,
            "price": price,
            "clicked": clicked,
        }

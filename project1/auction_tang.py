import random
from bidder_tang import Bidder

class User:
    user_count = 0  # Class-level counter to keep track of the number of User instances

    def __init__(self):
        """
        Initialize a new User instance with a unique ID and a random click probability.
        """
        self.__probability = random.uniform(0, 1)
        self.user_id = User.user_count
        User.user_count += 1

    def __repr__(self):
        return f"User of id: {self.user_id}"

    def __str__(self):
        return f"User of id: {self.user_id}"

    def show_ad(self):
        """
        Simulate showing an ad to the user and return True if the ad was clicked, False otherwise.
        """
        return random.random() < self.__probability


class Auction:
    def __init__(self, users, bidders):
        """
        Initialize the auction with given users and bidders.
        
        Args:
            users (list): A list of User objects.
            bidders (list): A list of Bidder objects.
        """
        self.users = users
        self.bidders = bidders
        self.balances = {}  # Placeholder for future functionality to track bidder balances

    def execute_round(self):
        """
        Execute one round of the auction process.
        """
        selected_user = random.choice(self.users)  # Randomly select a user for this round
        bids = {}  # Initialize an empty dictionary to store bids from bidders

        print(f"Selected User: {selected_user}")  # Log the selected user

        # Collect bids from all bidders
        for bidder in self.bidders:
            bid_amount = bidder.bid(selected_user.user_id)
            bids[bidder] = bid_amount

        print(f"Bids: {bids}")  # Log the bids made by bidders

        # Determine the first and second place bidders based on the bids
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
        first_place_bidder, first_place_bid = sorted_bids[0]
        second_place_bidder, second_place_bid = sorted_bids[1]

        print(f"First Place Bidder: {first_place_bidder}, Bid: {first_place_bid}")  # Log the first place bidder and bid
        print(f"Second Place Bidder: {second_place_bidder}, Bid: {second_place_bid}")  # Log the second place bidder and bid

        # Show the ad to the selected user and check if they clicked it
        clicked = selected_user.show_ad()

        print(f"Ad Clicked: {clicked}")  # Log whether the ad was clicked or not

        # Notify all bidders about the outcome of this auction round
        for bidder in self.bidders:
            is_winner = (bidder == first_place_bidder)
            bidder.notify(is_winner, second_place_bid, clicked, selected_user.user_id)
            print(f"Updated Bidder State: {bidder}")  # Log the updated state of each bidder

'''
if __name__ == "__main__":
    # TODO: Remove before submission or place in a separate file (like main.py)

    # Change these values to test the auction
    num_rounds = 10
    num_users = 10
    num_bidders = 10

    # Generate lists of bidders and users, then construct the Auction with them
    bidders = [Bidder(num_users, num_rounds) for _ in range(num_bidders)]
    users = [User() for _ in range(num_users)]
    auction = Auction(users, bidders)

    # Run each auction round
    for round_number in range(num_rounds):
        print(f"{round_number=}")
        auction.execute_round()
'''
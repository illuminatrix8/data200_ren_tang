import random

# from bidder_tang import Bidder

class User:
    user_count = 0  # Class-level counter

    def __init__(self):
        self.__probability = random.uniform(0, 1)
        self.user_id = User.user_count
        User.user_count += 1

    def __repr__(self):
        return f"User of id: {self.user_id}"

    def __str__(self):
        return f"User of id: {self.user_id}"

    def show_ad(self):
        return random.random() < self.__probability

class Auction:
    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in bidders}
        self.user_ids = {user: i for i, user in enumerate(users)}

    def execute_round(self):
        selected_user = random.choice(self.users)
        selected_user_id = self.user_ids[selected_user]
        bids = {}
        for bidder in self.bidders:
            bid_amount = bidder.bid(selected_user_id)
            bids[bidder] = bid_amount
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
        first_place_bidder, first_place_bid = sorted_bids[0]
        second_place_bidder, second_place_bid = sorted_bids[1]
        clicked = selected_user.show_ad()
        
        # Update the balances here
        if clicked:
            self.balances[first_place_bidder] += 1  # Reward for the click
        self.balances[first_place_bidder] -= second_place_bid  # Payment for the ad spot

        for bidder in self.bidders:
            is_winner = (bidder == first_place_bidder)
            bidder.notify(is_winner, second_place_bid, clicked if is_winner else None)

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
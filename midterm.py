tweets = ["This is great! RT @fakeuser: Can you believe this?",
         "It's the refs! RT @dubsfan: Boo the refs and stuff wargarbal",
         "That's right RT @ladodgers: The dodgers are destined to win the west!",
         "RT @sportball: That sporting event was not cool",
         "This is just a tweet about things @person, how could you",
         "RT @ladodgers: The season is looking great!",
         "RT @dubsfan: I can't believe it!",
         "I can't believe it either! RT @dubsfan: I can't believe it"]


def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    # initialize a dictionary
    retweets_by_username = {}

    # filter out retweets
    retweets = [tweet for tweet in tweets if 'RT @' in tweet]

    # find users from retweets
    retweets_usernames = [retweet.split('RT @')[1].split(':')[0] for retweet in retweets]

    # add in retweet counts in dictionary
    for username in retweets_usernames:
        if username not in retweets_by_username:
            retweets_by_username[username] = 1
        else:
            retweets_by_username[username] += 1

    return retweets_by_username


# allow this code to work by implementing count_retweets_by_username function above
print(count_retweets_by_username(tweets))



deposits = [(0, 4, .3), (6, 2, 3), (3, 7, 2.2), (5, 5, .5), (3, 5, .8), (7, 7, .3)]

def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    ans = "" # delete this line and enter your own code

    # each row is numbered from 0 to n-1 where 0 is the top and n-1 is the bottom
    # each column is also numbered from 0 to n-1 where 0 is the left and n-1 is the right

    # initialize the grid
    num_rows = bottom - top
    num_columns = right - left
    grid = [['-' for _ in range(num_columns)] for _ in range(num_rows)]

    # update the grid according to deposits
    for row in range(top, top + num_rows):
        for col in range(left, left + num_columns):
            if any(r == row and c == col for r, c, d in deposits):
                ans += 'x'
            else:
                ans += '-'
        ans += '\n'
    return ans

print(display(deposits, 5, 8, 5, 8))


def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    ans = "" # delete this line and enter your own code

    # each row is numbered from 0 to n-1 where 0 is the top and n-1 is the bottom
    # each column is also numbered from 0 to n-1 where 0 is the left and n-1 is the right

    # initialize the grid
    num_rows = bottom - top
    num_columns = right - left
    grid = [['-' for _ in range(num_columns)] for _ in range(num_rows)]

    # update the grid according to deposits
    for row in range(top, top + num_rows):
        for col in range(left, left + num_columns):
            deposit_value = None
            for r, c, d in deposits:
                if r == row and c == col:
                    deposit_value = d
                    break
            ans += str(deposit_value) if deposit_value is not None else '-'
        ans += '\n'
    return ans

print(tons_inside(deposits, 0, 8, 0, 8))


# The 2nd to last tuple needs the int(2) in it so that it is uniquely stored in memory compared to (2,8)
# Under the hood Python 3.7 changed how these are stored so (2,8) and (2,8) are stored in the same location
# and then the algorithm below doesn't work

dates = [(3,14),(2,8),(10,25),(5,17),(3,2),(7,25),(4,30),(8,7),(int(2),8),(1,22),(2, int(8))]


def birthday_original(dates_list):
    count = 0

    for person_a in dates_list:
        for person_b in dates_list:
            # Make sure we have different people        

            if person_a is person_b:
                continue

            # Check both month and day
            if person_a[0] == person_b[0] and person_a[1] == person_b[1]:
                count += 1
                
    # We counted each pair twice (e.g. jane-bob and bob-jane) so divide by 2:          
    return count//2

birthday_original(dates)


def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""

    # somehow we need to turn this into sets
    count = len(dates_list)
    count_unique = len(set(dates_list))

    return count - count_unique

birthday_count(dates)

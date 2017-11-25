from __future__ import division 
from collections import Counter

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Each pair (i,j) indicates that person i and person j are friends
# We can augment each user with a `friends` property

for user in users:
    user["friends"] = []

# and then populate the list using `friendships` data

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
    #print(users[i]["name"] + " and " + users[j]["name"] + " are friends!");

# We are asked to find the average number of friends of any user

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

# We can sort by number of friends

num_friends_by_id = [(user["id"],number_of_friends(user)) for user in users]
sorted(num_friends_by_id,                               # get it sorted
    key=lambda (user_id, num_friends): num_friends,     # by num_friends
    reverse=True)                                       # largest to smallest

def naive_friends_of_friend_ids(user):
    return [fof["id"]
        for friend in user["friends"]
        for fof in friend["friends"]]
        
naive_friends_of_friend_ids(users[0])

# the naive method includes repeats, direct friends, and the input user itself
# let's fix that

def not_the_same(userA, userB):
    return (userA["id"] != userB["id"])

def not_friends(userA, userB):
    return all(not_the_same(friend, other_user)
        for friend in user["friends"])

print([1,2,3])
print(naive_friends_of_friend_ids(users[0]))
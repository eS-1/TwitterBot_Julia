from config import myAPI
import tweepy


def getAllFollowers():
    followers = list()
    for follower in tweepy.Cursor(myAPI.followers).items():
        followers.append(follower)
    return followers


def getAllFriends():
    friends = list()
    for friend in tweepy.Cursor(myAPI.friends).items():
        friends.append(friend)
    return friends


def followBack():
    followers = getAllFollowers()
    friends = getAllFriends()
    for unknown in followers:
        if unknown not in friends:
            unknown.follow()


if __name__ == "__main__":
    followers = getAllFollowers()
    friends = getAllFriends()
    for unknown in followers:
        if unknown not in friends:
            unknown.follow()

from config import myAPI
import tweepy


def GetAllFollowers():
    followers = list()
    for follower in tweepy.Cursor(myAPI.followers).items():
        followers.append(follower)
    return followers


def GetAllFriends():
    friends = list()
    for friend in tweepy.Cursor(myAPI.friends).items():
        friends.append(friend)
    return friends


if __name__ == "__main__":
    followers = GetAllFollowers()
    friends = GetAllFriends()
    for unknown in followers:
        if unknown not in friends:
            unknown.follow()

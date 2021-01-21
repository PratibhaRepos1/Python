import twitter
import random
print("hi")
api = twitter.Api(consumer_key='5Kkw7BqqRo9Q8IBAdIrEvghQt',
                      consumer_secret='kMK68fzYuRdJjMxGxxDdf37xiQD7HHRNwOPy5ZFVJEBI5ztg7J',
                      access_token_key='1351414127214821376-zKWQ9MgBHNBhpmdV7n95BHJ34nV4P7',
                      access_token_secret='v0J1wFNLsqdAYTSuIGUjE3yWtgmWcQ2QPdq7yxWXzIc7Y')

#print(api.VerifyCredentials())
#users = api.GetFriends()
follwers = api.GetFollowers()
#print([u.name for u in users])
#print(len(users))

randomIndex = random.randint(0,len(follwers)-1)
randomFollower = follwers[randomIndex]
#print(randomFollower.screen_name)

tweet = "@{} you are random follower of the day! Turnup to tweet!".format(randomFollower.screen_name)
#print(tweet)
api.PostUpdate(tweet)
print("Thanks for Twetting!")

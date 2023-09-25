import tweepy

api_key= '9dM1OnwRonmPJcEAODM2IKwyk'
api_key_secret = '01qxKYP8Dm5EdCAc2uiy0sUfPtIov7sOHDKvBtaxJmIEfoBOr7'
bearer_tokens = 'AAAAAAAAAAAAAAAAAAAAAM8vmwEAAAAAjgWQk9Cis6LjXgsIczG63CJ5DUg%3D1XV1Huvq3XtCsxbxgxD0MU8w8yk3eHM6TNh5i4kG7930KPkfpb'
access_token= '1500965362434723840-UBC8OhmI3h2seHH7LgfPGezi99GDqW'
access_token_secret = 'RkUScDmsAXzwc9THs5rK13GUZaOBKZvRQ0W2JyXs4H315'
client_id= 'RkJkMDUwZ1l2dmJaYk5Mb0h3b286MTpjaQ'
client_secret= '1U8GErkUm5F9tcSZDN4saCsIsyK54IZRKcJmJdpbtKGVxdsOQv'


client = tweepy.Client(consumer_key=api_key, 
                                consumer_secret=api_key_secret,
                                access_token=access_token, 
                                access_token_secret=access_token_secret)


response = client.create_tweet(text='hello world')

print(response)


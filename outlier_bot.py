#! /usr/bin/python3
import praw
import datetime

reddit = praw.Reddit("outlier_bot1",
    user_agent="linux:outlier_bot:v0.0.0: (by u/Outlier_Bot)"
)
#Creates reddit instance "reddit"
#Creds in ./praw.ini

articles = ["futurecore", "strongshank", "32", "33", "futureslimworks"]
def outputs (post):
    print(post) #Need to replace print with a form of notification
    cache = open("outlier_bot_cache.txt", 'a')
    cache.write(post)
    cache.close()

def check_cache(post):
    cache = open("outlier_bot_cache.txt", 'r')
    if post in cache.read():
        cache.close()
        return 1
    else:
        return 0

for submission in reddit.subreddit("outliermarket").new(limit=10):
    for word in articles:
        if word in submission.title.lower() and "wts" in submission.title.lower():
            post = ("Post: "+submission.title
            +"\nBy: "+str(submission.author)
            +"\nLink: "+"reddit.com"+submission.permalink
            +"\nAt: "+str(datetime.datetime.fromtimestamp(submission.created))
            + "\n-------------------------\n"
            )
            if check_cache(post) == 1:
                continue
            outputs(post)
#print(reddit.display_name)
from twitter_scraper import get_tweets


def main():
    for tweet in get_tweets('kennethreitz', pages=100):
        print(tweet['time'])
        print(tweet['tweetId'])


if __name__ == '__main__':
    main()

# reddit_clique


Generate usernames by training a simple LSTM network on ~1m characters of reddit usernames. Usernames are obtained through reddit api from the commenters on the most popular subreddits. 

The data I scraped is provided in the repository but rerunning requires [praw](https://praw.readthedocs.io/en/latest/index.html) credentials stored in "credentials.json" in root folder.

In order to get usernames just run the "predict.py" script. Most names are slight variations or recombinations of names in the database and some are identical. Can easily be checked by plugging in to reddit.com/user/name.

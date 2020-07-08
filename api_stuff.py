import praw
import pickle
import json 

with open('credentials.json', 'r') as f:
    credentials_dict = json.load(f)

reddit = praw.Reddit(client_id=credentials_dict["client_id"], client_secret=credentials_dict["client_secret"], user_agent=credentials_dict["user_agent"])
subreddits=reddit.subreddits.popular(limit=99)
sub_names=[x.display_name for x in subreddits]
print(reddit.read_only)
names=[]
for sub_name in sub_names:
    submissions=reddit.subreddit(sub_name).top(limit=1000)
    authors=[x.author for x in submissions]
    #authors=list(set(authors))
    for x in authors:
        try: 
            names.append(x.name)
        except:
            pass

# link_karma=[x.link_karma for x in authors]
# comment_karma=[x.comment_karma for x in authors]
# karma=list(zip(link_karma,comment_karma))
# karma_dict=dict(zip(names,karma))

out_file=open("usernames",'wb')
pickle.dump(names,out_file)
out_file.close()
# out_file=open("karma_dict",'wb')
# pickle.dump(karma_dict,out_file)
# out_file.close()


print("done")


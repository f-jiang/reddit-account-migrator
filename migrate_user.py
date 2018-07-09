from getpass import getpass
import praw


def get_subreddits(reddit, **generator_kwargs):
    return list(reddit.user.subreddits(params=generator_kwargs))


def set_subreddits(reddit, subreddits):
    pass


def get_upvoted(reddit, **generator_kwargs):
    return list(reddit.user.me().upvoted(params=generator_kwargs))


def set_upvoted(reddit, upvoted):
    pass


def get_downvoted(reddit, **generator_kwargs):
    return list(reddit.user.me().downvoted(params=generator_kwargs))


def set_downvoted(reddit, downvoted):
    pass


def get_saved(reddit, **generator_kwargs):
    return list(reddit.user.me().saved(params=generator_kwargs))


def set_saved(reddit, saved):
    pass


def get_hidden(reddit, **generator_kwargs):
    return list(reddit.user.me().hidden(params=generator_kwargs))


def set_hidden(reddit, hidden):
    pass


def get_gilded(reddit, **generator_kwargs):
    return list(reddit.user.me().gilded(params=generator_kwargs))


def set_gilded(reddit, gilded):
    pass


def get_gildings(reddit, **generator_kwargs):
    return list(reddit.user.me().gildings(params=generator_kwargs))


def get_friends(reddit):
    return reddit.user.friends()


def set_friends(reddit, friends):
    pass


def get_blocked(reddit):
    return reddit.user.blocked()


def set_blocked(reddit, blocked):
    pass


def get_preferences(reddit):
    return reddit.user.preferences


def set_preferences(reddit, preferences):
    pass


if __name__ == '__main__':
    old_acct_reddit = praw.Reddit(client_id=input('enter client id for old account: '),
                                  client_secret=getpass('enter client secret for old account: '),
                                  username=input('enter username for old account: '),
                                  password=getpass('enter password for old account: '),
                                  user_agent='account-migrator for old account')

    subreddits = get_subreddits(old_acct_reddit)
    upvoted = get_upvoted(old_acct_reddit)
    downvoted = get_downvoted(old_acct_reddit)
    saved = get_saved(old_acct_reddit)
    hidden = get_hidden(old_acct_reddit)
    gilded = get_gilded(old_acct_reddit)
    gildings = get_gildings(old_acct_reddit)
    friends = get_friends(old_acct_reddit)
    blocked = get_blocked(old_acct_reddit)
    preferences = get_preferences(old_acct_reddit)

    new_acct_reddit = praw.Reddit(client_id=input('enter client id for new account: '),
                                  client_secret=getpass('enter client secret for new account: '),
                                  username=input('enter username for new account: '),
                                  password=getpass('enter password for new account: '),
                                  user_agent='account-migrator for new account')

    set_subreddits(new_acct_reddit, subreddits)
    set_upvoted(new_acct_reddit, upvoted)
    set_downvoted(new_acct_reddit, downvoted)
    set_saved(new_acct_reddit, saved)
    set_hidden(new_acct_reddit, hidden)
    set_gilded(new_acct_reddit, gilded)
    set_gildings(new_acct_reddit, gildings)
    set_friends(new_acct_reddit, friends)
    set_blocked(new_acct_reddit, blocked)
    set_preferences(new_acct_reddit, preferences)


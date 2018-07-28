import argparse
from json import dumps
from getpass import getpass
from sys import argv

import praw


def get_subreddits(reddit):
    return list(reddit.user.subreddits(limit=None))


def set_subreddits(reddit, items, brief):
    subreddit = reddit.subreddit(items[0].display_name)
    subreddit.subscribe(items[1:])

    if not brief:
        subreddit_names = sorted([item.display_name for item in items])
        print('=== subscribed to the following subreddits:')
        print(', '.join(subreddit_names))


def get_upvoted(reddit):
    return list(reddit.user.me().upvoted(limit=None))


def set_upvoted(reddit, items, brief):
    n_items = len(items)
    field_width = len(str(n_items))

    for i in range(n_items):
        if type(items[i]) == praw.models.Submission:
            submission = reddit.submission(items[i].id)
            submission.upvote()

            if not brief:
                print('=== ({:<{width}} of {:<{width}}) upvoted submission titled "{}" from subreddit "{}"'
                      .format(i + 1,
                              n_items,
                              submission.title,
                              submission.subreddit.display_name,
                              width=field_width))
        elif type(items[i]) == praw.models.Comment:
            comment = reddit.comment(items[i].id)
            comment.upvote()

            if not brief:
                print('=== ({:<{width}} of {:<{width}}) upvoted comment with body "{}..." from submission "{}"'
                      .format(i + 1,
                              n_items,
                              comment.body[:40],
                              comment.link_title,
                              width=field_width))


def get_downvoted(reddit):
    return list(reddit.user.me().downvoted(limit=None))


def set_downvoted(reddit, items, brief):
    n_items = len(items)
    field_width = len(str(n_items))

    for i in range(n_items):
        if type(items[i]) == praw.models.Submission:
            submission = reddit.submission(items[i].id)
            submission.downvote()

            if not brief:
                print('=== ({:<{width}} of {:<{width}}) downvoted submission titled "{}" from subreddit "{}"'
                      .format(i + 1,
                              n_items,
                              submission.title,
                              submission.subreddit.display_name,
                              width=field_width))
        elif type(items[i]) == praw.models.Comment:
            comment = reddit.comment(items[i].id)
            comment.downvote()

            if not brief:
                print('=== ({:<{width}} of {:<{width}}) downvoted comment with body "{}..." from submission "{}"'
                      .format(i + 1,
                              n_items,
                              comment.body[:40],
                              comment.link_title,
                              width=field_width))


def get_saved(reddit):
    return list(reddit.user.me().saved(limit=None))


def set_saved(reddit, items, brief):
    n_items = len(items)
    field_width = len(str(n_items))

    for i in range(n_items):
        if type(items[i]) == praw.models.Submission:
            submission = reddit.submission(items[i].id)
            submission.save()

            if not brief:
                print('=== ({:<{width}} of {:<{width}}) saved submission titled "{}" from subreddit "{}"'
                      .format(i + 1,
                              n_items,
                              submission.title,
                              submission.subreddit.display_name,
                              width=field_width))
        elif type(items[i]) == praw.models.Comment:
            comment = reddit.comment(items[i].id)
            comment.save()

            if not brief:
                print('=== ({:<{width}} of {:<{width}}) saved comment with body "{}..." from submission "{}"'
                      .format(i + 1,
                              n_items,
                              comment.body[:40],
                              comment.link_title,
                              width=field_width))


def get_hidden(reddit):
    return list(reddit.user.me().hidden(limit=None))


def set_hidden(reddit, items, brief):
    n_items = len(items)
    field_width = len(str(n_items))

    for i in range(n_items):
        submission = reddit.submission(items[i].id)
        submission.hide()

        if not brief:
            print('=== ({:<{width}} of {:<{width}}) hid submission titled "{}" from subreddit "{}"'
                  .format(i + 1,
                          n_items,
                          submission.title,
                          submission.subreddit.display_name,
                          width=field_width))


def get_friends(reddit):
    return reddit.user.friends()


def set_friends(reddit, items, brief):
    n_items = len(items)
    field_width = len(str(n_items))

    for i in range(n_items):
        redditor = reddit.redditor(items[i].name)
        redditor.friend()

        if not brief:
            print('=== ({:<{width}} of {:<{width}}) friended redditor named "{}"'
                  .format(i + 1, n_items, redditor.name, width=field_width))


def get_blocked(reddit):
    return reddit.user.blocked()


def set_blocked(reddit, items, brief):
    n_items = len(items)
    field_width = len(str(n_items))

    for i in range(n_items):
        redditor = reddit.redditor(items[i].name)
        redditor.block()

        if not brief:
            print('=== ({:<{width}} of {:<{width}}) blocked redditor named "{}"'
                  .format(i + 1, n_items, redditor.name, width=field_width))


def get_preferences(reddit):
    return reddit.user.preferences()


def set_preferences(reddit, item, brief):
    reddit.user.preferences.update(**item)

    if not brief:
        print('=== updated preferences to the following:')
        print(dumps(item, sort_keys=True, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transfer user data between Reddit accounts')
    parser.add_argument('-q', '--brief', action='store_true', help='suppress status output')
    args = parser.parse_args()

    old_client_id = input('>>> enter client id for old account: ')
    old_client_secret = getpass('>>> enter client secret for old account: ')
    old_username = input('>>> enter username for old account: ')
    old_password = getpass('>>> enter password for old account: ')
    old_user_agent = 'account-migrator for old account'

    new_client_id = input('>>> enter client id for new account: ')
    new_client_secret = getpass('>>> enter client secret for new account: ')
    new_username = input('>>> enter username for new account: ')
    new_password = getpass('>>> enter password for new account: ')
    new_user_agent = 'account-migrator for new account'

    old_acct_reddit = praw.Reddit(client_id=old_client_id,
                                  client_secret=old_client_secret,
                                  username=old_username,
                                  password=old_password,
                                  user_agent=old_user_agent)

    new_acct_reddit = praw.Reddit(client_id=new_client_id,
                                  client_secret=new_client_secret,
                                  username=new_username,
                                  password=new_password,
                                  user_agent=new_user_agent)

    print('=== fetching user data from old account "{}"...'.format(old_username))

    if not args.brief:
        print('=== looking for subscribed subreddits...')
    subreddits = get_subreddits(old_acct_reddit)
    n_subreddits = len(subreddits)
    if not args.brief:
        print('=== found {} {}'.format(n_subreddits, 'subreddit' if n_subreddits == 1 else 'subreddits'))

    if not args.brief:
        print('=== looking for upvoted items...')
    upvoted = get_upvoted(old_acct_reddit)
    n_upvoted = len(upvoted)
    if not args.brief:
        print('=== found {} upvoted {}'.format(n_upvoted, 'item' if n_upvoted == 1 else 'items'))

    if not args.brief:
        print('=== looking for downvoted items...')
    downvoted = get_downvoted(old_acct_reddit)
    n_downvoted = len(downvoted)
    if not args.brief:
        print('=== found {} downvoted {}'.format(n_downvoted, 'item' if n_downvoted == 1 else 'items'))

    if not args.brief:
        print('=== looking for saved items...')
    saved = get_saved(old_acct_reddit)
    n_saved = len(saved)
    if not args.brief:
        print('=== found {} saved {}'.format(n_saved, 'item' if n_saved == 1 else 'items'))

    if not args.brief:
        print('=== looking for hidden items...')
    hidden = get_hidden(old_acct_reddit)
    n_hidden = len(hidden)
    if not args.brief:
        print('=== found {} hidden {}'.format(n_hidden, 'item' if n_hidden == 1 else 'items'))

    if not args.brief:
        print('=== looking for friended redditors...')
    friends = get_friends(old_acct_reddit)
    n_friends = len(friends)
    if not args.brief:
        print('=== found {} friended {}'.format(n_friends, 'redditor' if  n_friends == 1 else 'redditors'))

    if not args.brief:
        print('=== looking for blocked redditors...')
    blocked = get_blocked(old_acct_reddit)
    n_blocked = len(blocked)
    if not args.brief:
        print('=== found {} blocked {}'.format(n_blocked, 'redditor' if n_blocked == 1 else 'redditors'))

    if not args.brief:
        print('=== looking for preferences...')
    preferences = get_preferences(old_acct_reddit)
    if not args.brief:
        print('=== found preferences')

    print('=== transfer user data to new account "{}"...'.format(new_username))

    print('=== subscribing to {} {}...'.format(n_subreddits, 'subreddit' if n_subreddits == 1 else 'subreddits'))
    set_subreddits(new_acct_reddit, subreddits, args.brief)

    print('=== upvoting {} {}...'.format(n_upvoted, 'item' if n_upvoted == 1 else 'items'))
    set_upvoted(new_acct_reddit, upvoted[::-1], args.brief)

    print('=== downvoting {} {}...'.format(n_downvoted, 'item' if n_downvoted == 1 else 'items'))
    set_downvoted(new_acct_reddit, downvoted[::-1], args.brief)

    print('=== saving {} {}...'.format(n_saved, 'item' if n_saved == 1 else 'items'))
    set_saved(new_acct_reddit, saved[::-1], args.brief)

    print('=== hiding {} {}...'.format(n_hidden, 'item' if n_hidden == 1 else 'items'))
    set_hidden(new_acct_reddit, hidden[::-1], args.brief)

    print('=== friending {} {}...'.format(n_friends, 'redditor' if n_friends == 1 else 'redditors'))
    set_friends(new_acct_reddit, friends, args.brief)

    print('=== blocking {} {}...'.format(n_blocked, 'redditor' if n_blocked == 1 else 'redditors'))
    set_blocked(new_acct_reddit, blocked, args.brief)

    print('=== setting preferences')
    set_preferences(new_acct_reddit, preferences, args.brief)


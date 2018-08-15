# reddit-account-migrator

## Features

- Transfer the following between accounts:
  - Subscriptions
  - Upvotes
  - Downvotes
  - Saved content
  - Hidden content
  - Friends (using new account, sends a request to each friend from old account)
  - Blocked users
  - Preferences

## Command-line usage:

```
usage: reddit_account_migrator.py [-h] [-q] [-t]

This script allows one to Transfer user data between Reddit accounts. Before
using this script, go to Preferences > Apps for each Reddit account and create
a "personal use script" with a placeholder redirect uri such as
`http://localhost:8080`. Take note of the app's client ID and secret.

optional arguments:
  -h, --help            show this help message and exit
  -q, --brief           suppress status output
  -t, --transfer-votes  move your upvotes and downvotes to your new account
                        (do at your own risk)
```


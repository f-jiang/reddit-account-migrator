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
usage: migrate_user.py [-h] [-q]

Transfer user data between Reddit accounts

optional arguments:
  -h, --help   show this help message and exit
  -q, --brief  suppress status output
```

## Setup

For each Reddit account, go to Preferences > Apps and create a "personal use script" with a placeholder redirect uri such as `http://localhost:8080`. Take note of the app's client ID and secret.


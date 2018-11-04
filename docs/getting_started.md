# Requirements

Python 2.7, Python 3.3, 3.4 or 3.5 are supported.

# Installation

```bash
$ virtualenv ~/.ihan
$ source ~/.ihan/bin/activate
$ pip install --upgrade ihan
```

# Shipping Logs

Make sure the user account that is running has read access to the main nginx log file. If it doesn't please run the following. Replace ``your_user_name`` with your unix username (found via ``whoami``).

```bash
$ sudo usermod -a -G www-data your_user_name
$ sudo chmod g+r /var/log/nginx/access.log
```

```
$ sudo apt install screen
$ screen
$ ihan live /var/log/nginx/access.log
```

# Backfill Older Log Files

If the file is not compressed, run the following:

```
$ screen
$ ihan backfill /var/log/nginx/access.log
```

If it is compressed, run the following:

```
$ screen
$ gunzip -c /var/log/nginx/access.log.gz | ihan backfill -
```
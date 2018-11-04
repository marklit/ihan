# IHAN Client

[IHAN](https://www.ihan.ee/) Client for feeding and back filling log files.

[![Documentation Status](https://readthedocs.org/projects/ihan/badge/?version=latest)](http://ihan.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.org/marklit/ihan.svg?branch=master)](https://travis-ci.org/marklit/whois)
[![Coverage Status](https://coveralls.io/repos/marklit/ihan/badge.png)](https://coveralls.io/r/marklit/whois)
[![Code Health](https://landscape.io/github/marklit/ihan/master/landscape.svg?style=flat)](https://landscape.io/github/marklit/ihan/master)
[![Latest Release](https://img.shields.io/pypi/v/ihan.svg)](https://pypi.python.org/pypi/ihan)
[![license](http://img.shields.io/badge/license-MIT-red.svg?style=flat)](http://opensource.org/licenses/MIT)

## Requirements

Python 2.7 and Python 3.4+ are supported.

On most Ubuntu systems you should be able to install Python and virtualenv via the following:

```bash
$ sudo apt update
$ sudo apt install \
    python-pip \
    python-virtualenv
```

## Installation

```bash
$ virtualenv ~/.ihan
$ source ~/.ihan/bin/activate
$ pip install --upgrade ihan
```

## Shipping Logs

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

Once that's running type ``CTRL-A`` and then ``CTRL-D`` to return to your regular shell.

## Backfill Older Log Files

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

Once that's running type ``CTRL-A`` and then ``CTRL-D`` to return to your regular shell.
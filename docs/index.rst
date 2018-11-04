Requirements
############

Python 2.7, Python 3.3, 3.4 or 3.5 are supported.

Installation
############

.. code-block:: bash

    $ virtualenv ~/.ihan
    $ source ~/.ihan/bin/activate
    $ pip install --upgrade ihan

Shipping Logs
#############

Make sure the user account that is running has read access to the main nginx log file. If it doesn't please run the following. Replace ``your_user_name`` with your unix username (found via ``whoami``).

.. code-block:: bash

    $ sudo chown your_user_name:www-data g+r /var/log/nginx/access.log

.. code-block:: bash

    $ sudo apt install screen
    $ screen
    $ ihan live /var/log/nginx/access.log

Backfill Older Log Files
########################

If the file is not compressed, run the following:

.. code-block:: bash

    $ screen
    $ ihan backfill /var/log/nginx/access.log


If it is compressed, run the following:

.. code-block:: bash

    $ screen
    $ gunzip -c /var/log/nginx/access.log.gz | ihan backfill -

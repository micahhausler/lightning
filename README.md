lightning
=========

DjangoCon 2013 - Lightning Talk - Micah Hausler


Installation
=============
To install:
    
    $ git clone git@github.com:micahhausler/lightning.git
    $ sudo apt-get install python-dev python-pip
    $ cd lightning
    $ virtualenv venv
    $ . ./venv/bin/activate
    $ pip install -r requirements.txt 
    $ export AWS_ACCESS_KEY_ID="YOUR_KEY_HERE"
    $ export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY_HERE"
    $ python manage.py syncdb
    $ python manage.py collectstatic
    $ python manage.py runserver


Author
------
@micahhausler  
micah.hausler@akimbo.io  
Sysadmin at Ambition - tryambition.com

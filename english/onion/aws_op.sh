sed -ie 's#DEBUG = True$#DEBUG = False#g' ./settings.py 
rm static/admin
ln -s $HOME/env/lib/python2.7/site-packages/django/contrib/admin static/

#mysql> create database onion;
#mysql -uroot -p onion<data/onion.sql

#service redis stop
#mv -f data/dump.rdb /var/lib/redis/
#service redis start

. ~/env/bin/activate
python manage.py collectstatic --noinput
uwsgi --reload uwsgi.pid 

#echo 1 > /proc/sys/vm/overcommit_memory
#!/usr/bin/env bash

# http://stackoverflow.com/questions/18215973/how-to-check-if-running-as-root-in-a-bash-script
# EUID   Expands to the effective user ID of the current  user,  initialized at shell startup.
# This variable is readonly.
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

pwd
#########################
# Install system packages
#########################

# Enable EPEL repository
yum -y install http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm

yum -y install http://yum.postgresql.org/9.3/redhat/rhel-7-x86_64/pgdg-redhat93-9.3-2.noarch.rpm
yum -y install vim gcc python postgresql93-server python-psycopg2 numpy python-devel
yum -y install postgis2_93
# openssl-devel is required for django-auth-pubtkt
sudo yum -y install openssl-devel

#########################
# Setup PostgreSQL 9.3 and PostGIS 2.93
#########################
/usr/pgsql-9.3/bin/postgresql93-setup initdb
systemctl enable postgresql-9.3
sh -c 'echo "local   all             all   peer" > /var/lib/pgsql/9.3/data/pg_hba.conf'
sh -c 'echo "host    all             all   all    md5">> /var/lib/pgsql/9.3/data/pg_hba.conf'
sh -c "echo listen_addresses = \\'*\\' >> /var/lib/pgsql/9.3/data/postgresql.conf"
systemctl start postgresql-9.3
sudo -u postgres sh -c '/usr/pgsql-9.3/bin/dropdb dw'
sudo -u postgres sh -c '/usr/pgsql-9.3/bin/createdb dw'
sudo -u postgres /usr/pgsql-9.3/bin/psql -c "CREATE USER dw WITH PASSWORD 'dw';"
sudo -u postgres /usr/pgsql-9.3/bin/psql -c "ALTER USER dw WITH CREATEDB;"
sudo -u postgres /usr/pgsql-9.3/bin/psql -c "GRANT ALL PRIVILEGES ON DATABASE dw to dw;"
# Enable PostGIS extension on this database
sudo -u postgres /usr/pgsql-9.3/bin/psql dw -c "CREATE EXTENSION postgis;"
sudo -u postgres /usr/pgsql-9.3/bin/psql dw -c "CREATE EXTENSION postgis_topology;"
# Permissions to access schema created by PostGIS
sudo -u postgres /usr/pgsql-9.3/bin/psql -d dw -c "GRANT ALL PRIVILEGES ON SCHEMA topology to dw;"
sudo -u postgres /usr/pgsql-9.3/bin/psql -d dw -c "GRANT ALL PRIVILEGES ON ALL TABLES in SCHEMA topology to dw;"

systemctl restart postgresql-9.3

curl "https://bootstrap.pypa.io/get-pip.py" | python
sudo pip install -r /vagrant/requirements.txt

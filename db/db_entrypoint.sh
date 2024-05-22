#!/bin/bash

# Trap SIGTERM
trap 'true' SIGTERM

# Start the FreeRadius Server
# /etc/init.d/freeradius restart

# Start the MySQL server

# Enable the server to listen to the remote
sed -e '/bind-address/s/^/#/g' -i /etc/mysql/mysql.conf.d/mysqld.cnf

/etc/init.d/mysql restart

# Enable logs
mysql -u root -p'root' -e "SET GLOBAL general_log = 1; SET GLOBAL general_log_file='/var/log/mysql/mysql.log';"

# Create a user and grant remote access
mysql -u root -p'root' -e "CREATE USER 'admin'@'%' IDENTIFIED BY 'admin';"
mysql -u root -p'root' -e "GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;"
mysql -u root -p'root' -e "FLUSH PRIVILEGES;"

# Initialze database
DB_NAME=locasync
mysql -u root -p'root' -e "CREATE DATABASE $DB_NAME;"
sleep 2

if [ -f host_sql/${DB_NAME}.sql ]; then
    mysql -u root -p'root' $DB_NAME < host_sql/${DB_NAME}.sql
    echo "Import ${DB_NAME}.sql"
fi

# Wait for the container shut down
sleep infinity &
wait $!

# Export database to SQL file
mysqldump -u root -p'root' $DB_NAME > host_sql/${DB_NAME}.sql
echo "Export ${DB_NAME}.sql"
mv /var/log/mysql/mysql.log host_sql/
echo "Export mysql.log"

# MySQL
MySQL is one of the world’s most popular relational database system.

## Install
You can install it on the Raspberry Pi this way:

- sudo apt update
- sudo apt upgrade
- sudo apt install mariadb-server

The MySQL server is now installed, you will now need to secure it by setting a password for the *root* user.

By default, MySQL is installed **without any password** set up meaning you can access the MySQL server without any authentication.

Run the following command to begin the MySQL securing process.

- sudo mysql_secure_installation

Make sure you write down the password you set during this process as we will need to use it to access the MySQL server.

To access your Raspberry Pi’s MySQL server and start making changes to your databases, you can use this command.

    sudo mysql -u root -p

You will be prompted to enter the password that you just created.

**Note:** *Like most Linux password inputs, the password will not show up as you type.*

### Show databases
Execute the following command to see databases present in the you MySQL server.

    show databases;

<div style="page-break-after: always;"></div>

## Enable Remote Access
To be able to connect from any IP address, do the following in the MySQL promt:

    sudo mysql -u root -p
    grant all privileges on *.* to root@'%' identified by 'yourpassword';
    flush privileges;

Allow mysql server to accept remote connections.

Start with editing MySQL config file:

    sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

Find the line starting with *bind-address* and comment it out:

![bind](https://github.com/officegeek/image/raw/main/bind.png)

Restart mysql server

    sudo systemctl restart mysql

<div style="page-break-after: always;"></div>

## Workbench
You can use MySQL Workbench from another computer - *Remember to connect it to the same network as the Raspberry PI.*

![bind](https://github.com/officegeek/image/raw/main/MySQL.png)


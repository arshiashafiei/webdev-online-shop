# electro-shop

## Project Setup

```sh
cd electro-shop-nuxt
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

-- Create a new database
CREATE DATABASE webproject_db;

-- Create a new user with a specified password
CREATE USER webproject_user WITH PASSWORD 'random1234';

-- Set the client encoding to UTF-8
ALTER ROLE webproject_user SET client_encoding TO 'utf8';

-- Set the default transaction isolation level to 'read committed'
ALTER ROLE webproject_user SET default_transaction_isolation TO 'read committed';

-- Set the timezone to UTC
ALTER ROLE webproject_user SET timezone TO 'UTC';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE webproject_db TO webproject_user;

## To create a new user

```sh
./manage.py createsuperuser
```

# Setup Postgresql

> run postgresql with systemctl

### Install postgres

#### latest

`sudo pacman -S postgresql`

##### specific version

> find version & build from source

### Check version

`postgres --version`

### Confirm psql is not running

`sudo systemctl status postgresql`  --> should not be running

### Login as the postgres user

> Note: always do this any time you are doing any type of admin work on psql

`sudo su - postgres`

### Initialize data directory

> Note: default db for psql is /var/lib/postgres/data

`initdb --locale en_US.UTF-8 -D /var/lib/postgres/data`

### Logout of **postgres** user

`exit`

### Confirm psql is still not running

`sudo systemctl status postgresql`  --> should not be running

### Start psql

`sudo systemctl start postgresql`

### Confirm psql is running

`sudo systemctl status postgresql`  --> should be active

## Create user

### Log into postgres

`sudo su - postgres`

### Create a new user

> Note: user can be called anything however if you create a PostgreSQL user with the same name as your Linux username, it allows you to access the PostgreSQL database shell without having to specify a user to login (which makes it quite convenient).

`createuser --interactive`

- Enter name of role to add: `MY_LINUX_USERNAME`
- Shall the new role be a superuser?: `y`

### Logout of **postgres** user

`exit`

### Restart psql

`sudo systemctl restart postgresql`

### Confirm psql is running

> Note: can see that it was restarted by looking at the timestamp on the ***Active*** field

`sudo systemctl status postgresql`

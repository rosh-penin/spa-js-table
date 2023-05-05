# spa_table_test
#### Single Page Application (Not really) with Django

#### Settings
You may want to specify your own .env settings. Basic one are already included in .env file
```sh
DB_ENGINE # If you don't specify engine sqlite will be used and rest of the database related settings ignored.
DB_HOST # Host where db is running. Defaults to docker-compose service name
DB_NAME # Name of your database
DB_PORT # Database port
POSTGRES_USER # Database user
POSTGRES_PASSWORD # Database password
```
If installing full compose orchestra just simply run
```sh
sudo docker-compose up -d
```
Table is populated automatically if empty
#### Usage
Main page should be accessible from url:
```sh
http://{your_server_ip_or_localhost}:8000/
```
### Author: Rosh_penin
### About: Pet project. Just a table with some simple JS sorting-filtering.

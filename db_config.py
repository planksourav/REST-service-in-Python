# We create the below db_config.py Python script under user_crud to setup the MySQL database configurations for connecting to database. 
# We need to configure database connection with flask module and that’s why we have imported app module and setup the MySQL configuration 
# with flask module.

from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'roytuts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

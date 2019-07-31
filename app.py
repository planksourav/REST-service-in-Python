# Create the below app.py script where we import the flask module. 
# This file should be created under user_crud directory. Notice how we create flask instance.
# We have configured a secret key, which is required for your application’s session.

from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_key1234"

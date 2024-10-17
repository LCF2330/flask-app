import os
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_CLUSTER_URL = os.getenv('MONGODB_CLUSTER_URL')  

connection_string = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER_URL}/shop_db?retryWrites=true&w=majority"

print("Connection String:", connection_string)

client = MongoClient(connection_string)
db = client.shop_db
products_collection = db.products

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the E-Commerce Store!"

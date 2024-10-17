from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_CLUSTER_URL = os.getenv('MONGODB_CLUSTER_URL')

from pymongo import MongoClient
connection_string = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER_URL}/shop_db?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return "Welcome to the E-Commerce Store!"

if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_CLUSTER_URL = os.getenv('MONGODB_CLUSTER_URL')

connection_string = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER_URL}/shop_db?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client.shop_db
products_collection = db.products

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_list = products_collection.find()
    return render_template('products.html', products=products_list)

if __name__ == "__main__":
    app.run(debug=True)

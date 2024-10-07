from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB connection string
app.config["MONGO_URI"] = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/shop_db?retryWrites=true&w=majority"

# Initialize PyMongo
mongo = PyMongo(app)

@app.route('/')
def home():
    return 'Flask is working!'

@app.route('/products')
def products():
    products = mongo.db.products.find()
    return f"Number of products: {products.count()}"

if __name__ == '__main__':
    app.run(debug=True)

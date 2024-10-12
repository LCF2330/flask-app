from flask import Flask, render_template # type: ignore
from pymongo import MongoClient # type: ignore

app = Flask(__name__)

client = MongoClient("mongodb+srv://root:V6rOOpMRY1YlGEM5@cluster0.6x6rl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['shop_db']
products_collection = db['products']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

from flask_app.app import app, client, products_collection

def test_home_invalid_method():
    """Test if the home route correctly returns 405 for a POST request."""
    with app.test_client() as client:
        response = client.post('/')  # Attempt a POST request on a GET-only route
        assert response.status_code == 405

def test_mongo_connection():
    """Test MongoDB connection by pinging the database."""
    result = client.admin.command('ping')
    assert result['ok'] == 1

def test_insert_product():
    """Test inserting a document into the products collection and verify its presence."""
    test_product = {"name": "Test Product", "tag": "test", "price": 10, "image_path": "static/images/test.jpg"}
    insert_result = products_collection.insert_one(test_product)
    
    # Verify the document was inserted
    inserted_product = products_collection.find_one({"_id": insert_result.inserted_id})
    assert inserted_product is not None
    assert inserted_product['name'] == "Test Product"
    
    # Clean up by deleting the test document
    products_collection.delete_one({"_id": insert_result.inserted_id})

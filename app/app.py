
from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary inventory storage
inventory = {}

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Inventory Management API",
        "status": "running"
    }), 200


# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200


# Add a new product
@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    required_fields = ["name", "quantity", "price"]

    if any(field not in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    name = data["name"]
    quantity = data["quantity"]
    price = data["price"]

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Invalid product name"}), 400

    if type(quantity) is not int or quantity < 0:
        return jsonify({"error": "Quantity must be a non-negative integer"}), 400

    if type(price) not in (int, float) or price < 0:
        return jsonify({"error": "Price must be a non-negative number"}), 400

    product_id = len(inventory) + 1

    product = {
        "id": product_id,
        "name": name.strip(),
        "quantity": quantity,
        "price": price
    }

    inventory[product_id] = product

    return jsonify({
        "message": "Product added successfully",
        "product": product
    }), 201


# View all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({
        "products": list(inventory.values())
    }), 200


# Get product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = inventory.get(product_id)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200


# Update product
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = inventory.get(product_id)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Valid JSON object required"}), 400

    if "name" in data:
        if not isinstance(data["name"], str) or not data["name"].strip():
            return jsonify({"error": "Invalid product name"}), 400
        product["name"] = data["name"].strip()

    if "quantity" in data:
        if type(data["quantity"]) is not int or data["quantity"] < 0:
            return jsonify({"error": "Invalid quantity"}), 400
        product["quantity"] = data["quantity"]

    if "price" in data:
        if type(data["price"]) not in (int, float) or data["price"] < 0:
            return jsonify({"error": "Invalid price"}), 400
        product["price"] = data["price"]

    return jsonify({
        "message": "Product updated successfully",
        "product": product
    }), 200


# Delete product
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_id not in inventory:
        return jsonify({"error": "Product not found"}), 404

    deleted_product = inventory.pop(product_id)

    return jsonify({
        "message": "Product deleted successfully",
        "product": deleted_product
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

# echo "Products";
# curl -X GET http://127.0.0.1:5000/products;
echo "Get product 1000";
curl -X GET http://127.0.0.1:5000/products/1000;
echo "Patch 1000 to name 'blob'";
curl -H "Content-Type: application/json" --data '{"id":1000, "name":"blob"}' -X PATCH http://127.0.0.1:5000/products/1000;
echo "Get product 1000";
curl -X GET http://127.0.0.1:5000/products/1000;
echo "create new product";
curl  -H "Content-Type: application/json" --data '{  "category": "Accessories",
  "code": "ge30fh0ge",
  "description": "Product Description",
  "id": 9999,
  "image": "bob-watch.jpg",
  "inventoryStatus": "INSTOCK",
  "name": "Chant of Seenar",
  "price": 65,
  "quantity": 24,
  "rating": 5}' -X POST http://127.0.0.1:5000/products;
echo "Product 9999";
curl -X GET http://127.0.0.1:5000/products/9999;

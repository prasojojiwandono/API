
Simple API from flask framework
----

To run this, first run the requirements first
``pip install -r requirements.txt``

second check if there any db.sqlite file or not,
if there is not db.sqlite file
run this in python command
``from app import db``
``db.create_all()``

third To run this simple api 
``python app.py``

To test this api, (prefer) with postman, this is the example
* To insert data, 
``
{
    "name":"product_1",
    "description":"ini product_1",
    "price":123,
    "qty":2
}
``

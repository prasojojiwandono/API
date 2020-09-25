
Simple API from flask framework
----

first of all thankyou for channel Traversy Media from youtube
I can learn something about flask and API

this mini project can happen because one of Traversy Media video's
https://www.youtube.com/watch?v=PTZiDnuC86g

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

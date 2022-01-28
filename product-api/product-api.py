from flask import Flask

from flask_restful import Resource, Api
import mysql.connector
from flask import render_template
from flask import request

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        config = {
        'user': 'root', 'password': 'root',
        'host': 'db-mysql', 'port': '3306',
        'database': 'products'}
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items_on_sale")
        results = [{"item": name, "qty":qty, "price":price} for (name, qty, price) in cursor]
        return {'products':results}
    

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "GET": 
        return render_template('insert.html')
    if request.method == "POST": 
        
        item_name = request.form['item_name']
        item_quantity = request.form['item_quantity']
        item_price =  request.form['item_price']
        config = {
        'user': 'root', 'password': 'root',
        'host': 'db-mysql', 'port': '3306',
        'database': 'products'}
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM items_on_sale WHERE name = %s ', (item_name,))
        objects = cursor.fetchall()

        if (len(objects) > 0):
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            cursor.execute('UPDATE items_on_sale SET qty=%s WHERE name = %s ', (item_quantity,item_name,))
            connection.commit()
        else:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            sql = "INSERT INTO items_on_sale (name, qty, price) VALUES (%s, %s, %s)"
            val = (item_name, int(item_quantity), int(item_price))
            cursor.execute(sql, val)
            connection.commit()
        return render_template('insert.html')

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
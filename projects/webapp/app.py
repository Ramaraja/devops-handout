from flask import Flask, request, jsonify
import mysql.connector
import os
from werkzeug.utils import quote as url_quote


app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB')
    )
    return connection

@app.route('/')
def home():
    return "Welcome to the Web App!"

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    name = data['name']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Data added successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


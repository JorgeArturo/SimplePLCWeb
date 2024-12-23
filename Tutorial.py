from flask import Flask, request, jsonify
import sqlite3

class UserAPI:
    def __init__(self, database):
        self.database = database
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE
                              )''')
            conn.commit()

    def get_users(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return jsonify(users)

    def get_user(self, user_id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            user = cursor.fetchone()
            if user:
                return jsonify(user)
            return jsonify({'error': 'User not found'}), 404

    def create_user(self, new_user):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (new_user['name'], new_user['email']))
            conn.commit()
            return jsonify({'id': cursor.lastrowid}), 201

    def update_user(self, user_id, updated_user):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (updated_user['name'], updated_user['email'], user_id))
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
            return jsonify({'message': 'User updated'})

    def delete_user(self, user_id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
            return jsonify({'message': 'User deleted'})

class CityAPI:
    def __init__(self, database):
        self.database = database
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                user_id INTEGER,
                                FOREIGN KEY (user_id) REFERENCES users (id)
                              )''')
            conn.commit()

    def get_cities(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cities")
            cities = cursor.fetchall()
            return jsonify(cities)

    def get_city(self, city_id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cities WHERE id=?", (city_id,))
            city = cursor.fetchone()
            if city:
                return jsonify(city)
            return jsonify({'error': 'City not found'}), 404

    def create_city(self, new_city):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cities (name, user_id) VALUES (?, ?)", (new_city['name'], new_city['user_id']))
            conn.commit()
            return jsonify({'id': cursor.lastrowid}), 201

    def update_city(self, city_id, updated_city):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE cities SET name=?, user_id=? WHERE id=?", (updated_city['name'], updated_city['user_id'], city_id))
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({'error': 'City not found'}), 404
            return jsonify({'message': 'City updated'})

    def delete_city(self, city_id):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cities WHERE id=?", (city_id,))
            conn.commit()
            if cursor.rowcount == 0:
                return jsonify({'error': 'City not found'}), 404
            return jsonify({'message': 'City deleted'})



app = Flask(__name__)
user_api = UserAPI('users.db')
city_api = CityAPI('users.db')


@app.route('/cities', methods=['GET'])
def get_cities():
    return city_api.get_cities()

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    return city_api.get_city(city_id)

@app.route('/cities', methods=['POST'])
def create_city():
    new_city = request.get_json()
    return city_api.create_city(new_city)

@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    updated_city = request.get_json()
    return city_api.update_city(city_id, updated_city)

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    return city_api.delete_city(city_id)

@app.route('/users', methods=['GET'])
def get_users():
    return user_api.get_users()

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_api.get_user(user_id)

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    return user_api.create_user(new_user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.get_json()
    return user_api.update_user(user_id, updated_user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_api.delete_user(user_id)


if __name__ == '__main__':
    app.run(debug=True)
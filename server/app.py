from flask import Flask, jsonify
import psycopg2

db_params = {
    'database': 'aiworkflow',
    'user': 'postgres',
    'password': '690854Lr',
    'host': 'localhost',  # or your server IP if remote
    'port': 5432  # default PostgreSQL port
}

app = Flask(__name__,
            static_url_path='', 
            static_folder='public')
# app.config['DEBUG'] = False

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/db_helper/tasks/get")
def get_tasks():
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # SQL query to fetch data from the t_tasks table
        query = 'SELECT * FROM t_tasks'

        # Execute the query
        cursor.execute(query)

        # Fetch all the records
        records = cursor.fetchall()
        result = []
        for row in records:
            result.append(row)

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify(result)

    except psycopg2.Error as e:
        print("Error: " + e)
    finally:
        if conn is not None:
            conn.close()
    
    
if __name__ == "__main__":
    app.run(ssl_context='adhoc', port=5000)

# print(get_tasks())
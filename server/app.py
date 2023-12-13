from flask import Flask

app = Flask(__name__,
            static_url_path='', 
            static_folder='public')
# app.config['DEBUG'] = False

@app.route("/")
def hello():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(ssl_context='adhoc', port=5000)


from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])

from app.web import book

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=81)



from flask import current_app

from app import creat_app

app = creat_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=81, threaded=True)


a = current_app
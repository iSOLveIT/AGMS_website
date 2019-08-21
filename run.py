from content import app
import os




# Run WEBAPPS
if __name__ == '__main__':
    app.secret_key  = os.urandom(20)
    app.run(port=2300)
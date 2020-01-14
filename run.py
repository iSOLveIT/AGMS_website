from content import app
import os


# Run WEB APPLICATION
if __name__ == '__main__':
    app.secret_key = os.urandom(255)
    app.run(port=4000, debug=True)
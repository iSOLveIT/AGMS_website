from content import app
import os

app.config['SECRET_KEY'] = os.urandom(75)

# Run WEB APPLICATION
if __name__ == '__main__':
    app.run(debug=True)

from api import app

"""
This file is used to run the app from a WSGI server such as Gunicorn.
"""

if __name__ == "__main__":
    app.run()

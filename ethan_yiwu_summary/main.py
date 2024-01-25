## main.py
from web_interface import FlaskApp

class Main:
    def run(self):
        """
        Create an instance of FlaskApp and run the Flask application.
        """
        app = FlaskApp()
        app.run()

if __name__ == '__main__':
    main = Main()
    main.run()

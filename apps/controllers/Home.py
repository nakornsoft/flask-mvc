from apps import app

class Home(object):
    @app.route('/', methods=['GET', 'POST'])
    def Home():
        return "Welcome Flask MVC"

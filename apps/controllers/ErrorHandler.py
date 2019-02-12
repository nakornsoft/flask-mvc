from apps import app

class Errorhandler(object):
    # 404 Page not found
    @app.errorhandler(404)
    def PageNotFound(e):
        return "The requested URL was not found on the server.", 404

    # 405 Method Not Allowed
    @app.errorhandler(405)
    def MethodNotAllowed(e):
        return "The method is not allowed for the requested URL.", 405

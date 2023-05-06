from werkzeug.serving import run_simple # werkzeug development server
from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix

from website.home_app import app as home_app
from website.officeAdmin_app import app as officeAdmin_app

application = DispatcherMiddleware(home_app, {
    '/officeAdmin': officeAdmin_app
}
)
if __name__ == '__main__':
    run_simple('localhost', 8000,application, use_reloader=True, use_debugger=True, use_evalex=True)
from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix

from .home_app import app as home_app
from .officeAdmin_app import app as officeAdmin_app
# from flask_app_2 import app as flask_app_2
application = DispatcherMiddleware(home_app, {
    '/officeAdmin': officeAdmin_app
}
)
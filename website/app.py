from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix
from .office_admin_app import app as office_admin_app
# from flask_app_2 import app as flask_app_2
application = DispatcherMiddleware(office_admin_app
# , {
#     '/flask_app_2': flask_app_2
# }
)
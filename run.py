from werkzeug.serving import run_simple # werkzeug development server
from website import app as website
if __name__ == '__main__':
    run_simple('localhost', 5000, website.application, use_reloader=True, use_debugger=True, use_evalex=True)
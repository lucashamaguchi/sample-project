import os
from dotenv import load_dotenv, find_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())

from .app import create_app  # noqa

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


if __name__ == "__main__":
    app.run()

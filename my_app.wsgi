# from my_app import app as application
import os, time

def application(environ, start_response):
    from my_app import app as _application
    millis = int(round(time.time() * 1000))
    os.environ["key"] = str(millis)
    return _application(environ, start_response)

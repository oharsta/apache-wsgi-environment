<!--- https://davidhamann.de/2017/08/05/running-flask-with-wsgi-on-macos/ --->
cd wsgi_app
python3 -m venv .venv
source .venv/bin/activate
pip install mod_wsgi
pip install Flask
mod_wsgi-express start-server my_app.wsgi

http://localhost:8000/

# webcamcontroller
v4l2-ctl controller for webcams, tested on C920.
---
- Create new venv:
```bash
python3 -m venv $(pwd)/venv
```
- Install `flask`
```bash
source venv/bin/activate
python3 -m pip install flask
```
- Run webapp
```bash
FLASK_ENV=development FLASK_APP=app python3 -m flask run --port=<ijkl>
```
- Go to website at `localhost:<ijkl>`
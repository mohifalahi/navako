# Setup
Git clone the project and change directory

$ git clone https://github.com/mohifalahi/navako.git

$ cd navako

Create a virtual environment and activate it

$ virtualenv venv

For Windows: $ venv\scripts\activate

For Linux: $ source venv/bin/activate

Install the requirements

(venv)$ pip install -r requirements.txt

$ cd app

# Run the tests
To run the tests

(venv)$ python manage.py test api.tests

# Run the project
To run the project on development server on your local computer

(venv)$ python manage.py runserver

Navigate to http://127.0.0.1:8000/

You can interact with the APIs using both browser and postman collection provided with the project

To check "health" view, browse this url: "http://127.0.0.1:8000/api/health/". If the server is up and running, it should return a json like {"status": "ok"}

To check "predict" view, browse this url: "http://127.0.0.1:8000/api/predict/". You should pass this json to it, {"text": "یک متن دلخواه"}, it should return a json like [{"label": "recommended", "score": 0.9261903762817383}]





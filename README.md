# Experimenting with CSV file

Building a web app using Python, Django REST. It follows typical RESTful API design pattern.

## SETUP

I assume you already installed Python 3.4 or higher and pip.

### Virtual Environment

Install virtualenv via pip:

```
$ pip install virtualenv
```

Create a virtual environment for a project:

```
$ cd this-project
$ virtualenv venv
```

To use the virtual environment, you can activate it with:

```
$ source venv/bin/activate
```

### Installation & Migrations

Install the project packages including Django:

```
(venv) $ pip install -r requirements.txt
```

And you run the migrations:

```
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

### Run server

With this command:

```
(venv) $ python manage.py runserver
```

As you can see, there is no data from the CSV file.

### Populate the database with the data from CSV

With the following command:

```
(venv) $ python manage.py shell < devices/experiment_with_CSV.py
```

Check it now in the browser.

### In Browser

Here is an example of running a url in a browser:

```
GET http://localhost:5000/devices 

{
    "id": 1,
    "device_id": "a4a281ad",
    "timestamp": "2017-05-01T00:00:10Z",
    "device_type": "sensor",
    "status": "offline"
}
```

You populated the database with 5182 datasets. Cool, right?

### Further Development

- there has to be a validation on the data format
- the integration test could make sure that the validation is properly working
- the database should be automatically populated with CSV data after running the migrations
- other http methods are coming if needed


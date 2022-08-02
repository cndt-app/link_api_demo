# Conduit Link API Demo

## Installation & run
python 3.9 & poetry required.  

Once python and poetry is installed - just run `poetry install` to install dependencies.  

Place an API_KEY to the `demo/conduit_api.py:CONDUIT_API_TOKEN`.  
Run migrations by executing `./manage.py migrate`.  

After that execute in console `./manage.py runserver` to launch local server and open http://127.0.0.1/   



### Conduit API request examples:
see `demo/conduit_api.py`

### Usage
see `demo/views.py`

## Use Docker

### Build image

```sh
$ docker build -t link_api_demo .
```

### Run

```sh
$ docker run --rm -p 8000:8000 -t link_api_demo
```

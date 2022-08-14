# Storage security terminal

A webapp for viewing individual employee passcards, storage visits, 
and current employee traffic inside a storage or other facility.

### How to install


Python3 should be already installed. 
Use `pip` to install dependencies:
```
python3 -m pip install -r requirements.txt
```

### How to use
Get the database credentials from your employer. Create a file named '.env' next to 'settings.py' inside the directory /project/ and put the following variables and their values (which should replace the `...`s) into it:
```
DB_ENGINE=...
DB_HOST=...
DB_PORT=...
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_SECRET_KEY=...
```


Run the development server: 
```console
$ python3 manage.py runserver
```
To access the development server, go to http://127.0.0.1:8000/ in your web browser.

For production deployment, follow the instructions of your preferred web hosting.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).

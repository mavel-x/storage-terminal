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
ENGINE=...
HOST=...
PORT=...
NAME=...
DB_USER=...
PASSWORD=...
SECRET_KEY=...
```


Run main.py: 
```console
$ python3 main.py
```
To access the development server, go to http://127.0.0.1:8000/ in your web browser.

For production deployment, follow the instructions of your preferred web hosting.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).

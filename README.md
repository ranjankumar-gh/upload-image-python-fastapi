# Create Image API using FastAPI and Upload the image using Python
This project publish HTTP API in FastAPI and provides python client for uploading a local image to the API.

## How to run?
uvicorn app:app --reload

## URL of the HTTP API
http://127.0.0.1:8000/upload_file/ <br/>
**Note:** When you access the url on the browser, you should get the following response "{"detail":"Method Not Allowed"}". TThis means two things: 1) your API is running fine. 2) This message is coming because the method allowed on this URL is only POST. So either the image can be uploaded by tools like postman or using some http client. In the codebase there is a file "client.py" that can do the job of uploading the image. Otherwise the api can also be accessed by http://127.0.0.1:8000/docs.

## Dependency of this application
python-multipart

## Dependency of uvicorn
bidict==0.21.3 <br/>
click==7.1.2 <br/>
fastapi==0.68.1 <br/>
fastapi-socketio==0.0.8 <br/>
h11==0.9.0 <br/>
httptools==0.1.2 <br/>
pydantic==1.8.2 <br/>
python-engineio==4.2.1 <br/>
python-socketio==5.4.0 <br/>
starlette==0.14.2 <br/>
typing-extensions==3.10.0.2 <br/>
uvicorn==0.11.5 <br/>
uvloop==0.16.0 <br/>
websockets==8.1 <br/>

## How to install dependency?
[sudo] pip install pathon-lib

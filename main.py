from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = "templates")
# @-annotation 'get and post methods' of http protocol 
#root url:http://127.0.0.1:8000/
@app.get('/')
def home():
    '''
    home page
    '''
    return "hello World"

@app.get('/greet')
def greet_user(name):
    '''
    checking username and password
    '''
    
    name = input("Enter your Username: ")
    password = int(input("Enter your Password: "))
    if( password == 227766):
        
        
        return "Successfully sign_in: " +name

@app.get("/service") #http://127.0.0.1:8000/service/
def service_user(name):
    """This service takes username from client and return a greeting msg"""
    name = input("Enter your name: ")
    password = int(input("Enter your password: "))
    if password == 227766:
        return "Welcome " + name
    else:
        return "Failed"
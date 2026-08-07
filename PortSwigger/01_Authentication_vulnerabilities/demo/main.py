from fastapi import FastAPI, Form



app = FastAPI()



users = {
    'azureuser':'password123',
    'admin':'admin123'
}


@app.get('/')
def home():
    return {
        "message":"backend dziala"
    }


@app.post('/login')
def login(
    username: str = Form(...),
    password: str = Form(...)

):
# mamy utaj celową podatnośc
    if username not in users:
        return {
            "message":"Invalid username or password"
        }

    if users[username] != password:
        return {
            "message": "Invalid password"
        }

    return {
        "message": "Login successful"
    }

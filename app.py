import asyncio
from fastapi import FastAPI, Form, status, UploadFile, File, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from twilio.rest import Client

from fastapi.templating import Jinja2Templates
import config

import time

app = FastAPI()
settings = config.Settings()

# homepage
@app.get("/")
async def index():
    return FileResponse("index.html") # returns a webpage upon GET request


# POST request handler - uploadFile()
@app.post("/upload/")
async def uploadFile(file: UploadFile = File(...)):
    print(file)
    success_message = "File uploaded "
    # Read file contents 
    # content = await file.read()

    # Assuming the file contains one phone number per line 
    # phone_numbers = content.decode().splitlines()

    # Create a Twilio account Instance 
    # clinet = Client(settings.twilio_account_sid, settings.twilio_auth_token)

    # Loops through phone numbers 
    # for phone_number in phone_numbers:
    #     print(f"[CONNECTING TO SERVER...] /")
    #     time.sleep(1)
    #     print(f"[INFO] Sending SMS to {phone_number}")
    #     time.sleep(1)
    #     print(f"[SUCCESS] Successfully sent {phone_number} SMS")

        # message = client.message.create(
        #     body="Holla Amigos!",
        #     from_= settings.twilio_phone_number,
        #     to = phone_number
        # )
    
    # return 
    return True
    # return {"Message": f"SMS sent to {len(phone_numbers)} mumbers"}


# @app.get('/')
# async def index():
#     return FileResponse('index.html')

# @app.post('/')
# async def handle_form(phone: str = Form(...)):
#     client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
#     message = client.messages.create(
#         body="Hello from FastAPI!",
#         from_=settings.twilio_phone_number,
#         to=phone
#     )
#     return RedirectResponse(url='/success', status_code=status.HTTP_303_SEE_OTHER)



# from fastapi import FastAPI, File, UploadFile
# from twilio.rest import Client
# import config

# app = FastAPI()
# settings = config.Settings()

# @app.post("/uploadfile/")
# async def upload_file(file: UploadFile = File(...)):
#     # Read the file contents
#     contents = await file.read()
#     # Assuming the file contains one phone number per line
#     phone_numbers = contents.decode().splitlines()
    
#     client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
    
#     for phone in phone_numbers:
#         message = client.messages.create(
#             body="Hello from FastAPI!",
#             from_=settings.twilio_phone_number,
#             to=phone
#         )
    
#     return {"message": f"SMS sent to {len(phone_numbers)} numbers"}

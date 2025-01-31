from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains (or specify specific ones)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def get_info():
    return {
        "email": "apololadanieltolu@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/DannyBaine-Entity/fastAPI"
}
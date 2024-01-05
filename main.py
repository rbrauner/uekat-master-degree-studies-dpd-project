import os
from dotenv import load_dotenv
import uvicorn
from src.app import app

if __name__ == '__main__':
    load_dotenv()
    uvicorn.run(app, host=os.getenv('APP_HOST', '0.0.0.0'), port=int(os.getenv('APP_PORT', 8000)))

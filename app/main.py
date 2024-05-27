import os
from dotenv import load_dotenv

from fastapi import FastAPI
from app.api import endpoints

from openai import OpenAI

load_dotenv()

class Config:
    def __init__(self):
        self.OpenAI_API_Key = os.getenv("OPENAI_API_KEY")

Config = Config()
app = FastAPI()

#openAI client
client = OpenAI(api_key=Config.OpenAI_API_Key)

app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

#make a post request to openAI api to perform sentiment analysis
@app.get("/senti")
def sentiment_analysis():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant which describes the sentiment of the following text."},
        {"role": "user", "content": "I love apples. They are so delicious!"},
    ]
    )

    print(completion.choices[0].message)

    return {"Sentiment": completion.choices[0].message}

    
from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()  # load env variables
client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant."},
        {"role": "user", "content": "When was ChatGPT made?"},
    ]
)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a poetic assistant that likes to rhyme in every response."},
    ]
)

completion = completion.choices[0].message.content
print(completion)

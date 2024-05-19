from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()  # load env variables, and make sure you have your own API key in .env file :) 
client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a poetic assistant that likes to rhyme in every response."},
        {"role": "system", "content": "Your response must be in JSON where there is a 'code' field that has any code and a 'rhyme_explanation' field where the code is explained but in a way that rhymes."},
        {"role": "user", "content": "print hello world in python"},
        {"role": "user", "content": "now do it in java"},
    ]
)

completion = json.loads(completion.choices[0].message.content)
print("Code: ", completion["code"])
print("Expl: ", completion["rhyme_explanation"])

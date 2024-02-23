# this is how the openai api call needs to be structured apparently lol
from openai import OpenAI

# read the OPENAI_API_KEY file to get the api_key
with open('OPENAI_API_KEY', 'r') as file:
    api_key = file.read().strip()


client = OpenAI(
api_key=api_key
)

completion = client.completions.create(model='gpt-3.5-turbo-instruct', prompt="Once upon a time", max_tokens=50)
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
# this is how the openai api call needs to be structured apparently lol
from openai import OpenAI

# read the OPENAI_API_KEY file to get the api_key
with open("OPENAI_API_KEY", "r") as file:
    api_key = file.read().strip()

prompt = "Mere weeks have passed since Arthas Menethil set sail for Northrend, racing towards the Frozen Throne. Sylvanas Windrunner, from being mere moments from claiming her vengeance, finds herself further away from that goal with each passing day. Shunned, distrusted and hated, her Forsaken are without friends in a world that has no place for them. Beset by the Scourge and the rising Scarlet Crusade and with far too few resources, the Dark Lady grows increasingly desperate. She would ally with almost anyone if it would give her people a chance. The sudden arrival of two unlikely visitors inadvertently leads her to consider a small city state across the sea, reputedly ruled by an archmage with a certain history with a certain prince. A story mainly revolving around Sylvanas Windrunner, Jaina Proudmoore and the Dark Rangers."

client = OpenAI(api_key=api_key)

completion = client.completions.create(
    model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=200
)
print(completion.choices[0].text)
print(dict(completion).get("usage"))
print(completion.model_dump_json(indent=2))

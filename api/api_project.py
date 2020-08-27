import requests

import random

topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

res = requests.get(url,
                   headers={"Accept": "application/json"},
                   params={
                       "term": topic
                   }
                   )

data = res.json()

if len(data["results"]) != 0:
    if len(data["results"]) == 1:
        joke = data["results"][0]["joke"]
        print(f"I have 1 joke about {topic}. Here it is:")
        print(joke)
    else:
        length = len(data["results"])
        rand = random.randint(1, length - 1)
        joke = data["results"][rand]["joke"]
        print(f"I have {length} jokes about {topic}. Here's a random one:")
        print(joke)
else:
    print(f"Sorry, I don't have any jokes for {topic}")

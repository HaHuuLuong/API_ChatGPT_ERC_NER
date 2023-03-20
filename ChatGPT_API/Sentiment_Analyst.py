import os
import openai
import time
import pandas as pd
# openai.api_key = "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"  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
# openai.api_key = "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" 
openai.api_key ="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"

data = open("./result_regex.txt",encoding="utf-8").read().splitlines()  # read input file

prompt = """Label each sentence in the following dialogue with one of the labels:: [positive],[negative],[neutral].The returned results include: keep the structure prompt input: label"""

for item in data:
    prompt += f"\n- {item}"

def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:", " AI:"]
    )

    return response.choices[0].text

# print(prompt + ans)
a = time.time()
ans = openai_create(prompt)
b = time.time()
print(f"Request time: {b - a}")  # print request time

print()
print(ans)

# with open("result_ERC.txt", "w", encoding="utf-8") as f:
#     f.write(ans)

# import requests
# import json

# # Define your query
# query = "Hà Vân ơ Vân học với mình à"

# # Define your API key
# api_key = "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"

# # Define your API endpoint
# endpoint = "https://api.openai.com/v1/engines/davinci/completions"

# # Define your parameters
# parameters = {
#   "prompt": "Sentiment (positive, neutral, negative):\n\nTôi rất ưng con chó này!\nSentiment: positive\n\nAnh ấy rất tệ bạc.\nSentiment: negative\n\n",
#   "temperature": 0,
#   "max_tokens": 1,
#   "top_p": 1,
#   "frequency_penalty": 0,
#   "presence_penalty": 0,
#   "stop": "\n"
# }

# # Append the query to the prompt
# parameters["prompt"] += query + "\nSentiment:"

# # Send a post request to the API endpoint with your parameters and API key
# response = requests.post(endpoint, headers={"Authorization": f"Bearer {api_key}"}, data=json.dumps(parameters))

# # Get the JSON data from the response
# data = response.json()

# # Print the result
# print(data["choices"][0]["text"])
import openai
import json

# Set up the OpenAI API key
openai.api_key = "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"

# Read input from a .txt file
with open("./result_regex.txt", "r",encoding="utf-8") as f:
    input_text = f.read().splitlines() 

# # Set up the parameters for the API request
# params = {
#     "model": "text-davinci-002",
#     "prompt": input_text,
#     "temperature": 0.5,
#     "max_tokens": 1024,
#     "top_p": 1,
#     "frequency_penalty": 0,
#     "presence_penalty": 0
# }

# # Call the API to generate a response
# response = openai.Completion.create(**params)

# # Parse the response to get the output text
# output_text = response.choices[0].text

# # Print the output text
# print(output_text)

# # Perform name entity recognition
# response = openai.Completion.create(
#     engine="davinci",
#     prompt=input_text,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# # Parse the response to get the entities
# entities = response.choices[0].text

# # Print the entities
# print(entities)

# Perform emotion recognition
response = openai.Completion.create(
    engine="davinci",
    prompt=input_text,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    frequency_penalty=0,
    presence_penalty=0
)

# Parse the response to get the emotions
emotions = response.choices[0].text

# Print the emotions
print(emotions)

# Write the output to a .txt file
# with open("output_combine.txt", "w") as f:
#     f.write("Output Text:\n\n")
#     f.write(output_text)
#     f.write("\n\nEntities:\n\n")
#     # f.write(json.dumps(entities))
#     f.write("\n\nEmotions:\n\n")
#     # f.write(json.dumps(emotions))
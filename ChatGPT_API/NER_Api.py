import openai
import os
import re
import ast

openai.api_key = "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"

SYSTEM_PROMPT = "You are a smart and intelligent Named Entity Recognition (NER) system. I will provide you the definition of the entities you need to extract, the sentence from where your extract the entities and the output format with examples."

USER_PROMPT_1 = "Are you clear about your role?"

ASSISTANT_PROMPT_1 = "Sure, I'm ready to help you with your NER task. Please provide me with the necessary information to get started."
GUIDELINES_PROMPT = (
    "Entity Definition:\n"
    "1. PERSON: Short name or full name of a person from any geographic regions.\n"
    "2. DATE: Any format of dates. Dates can also be in natural language.\n"
    "3. LOC: Name of any geographic location, like cities, countries, continents, districts etc.\n"
    "\n"
    "Examples:\n"
    "\n"
    "1. Sentence: Mr. Jacob lives in Madrid since 12th January 2015.\n"
    "Output: [Mr. Jacob](PERSON) lives in [Madrid](LOC) since [12th January 2015](DATE).\n"
    "\n"
    "2. Sentence: Mr. Rajeev Mishra and Sunita Roy are friends and they meet each other on 24/03/1998.\n"
    "Output: [Mr. Rajeev Mishra](PERSON) and [Sunita Roy](PERSON) are friends and they meet each other on [24/03/1998](DATE)\n"
    "\n"
    "3. Sentence: [Hà Vân] : Vũ Khánh Uyên ủa :v t học ca 9h50 sao k biết m\n"
    "Output: [Hà Vân](PERSON) : [Vũ Khánh Uyên](PERSON) ủa :v t học ca [9h50](DATE) sao k biết m\n"
)


def openai_chat_completion_response(final_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_1},
            {"role": "assistant", "content": ASSISTANT_PROMPT_1},
            {"role": "user", "content": final_prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip(" \n")

my_sentence=""
data = open("./result_regex.txt",encoding="utf-8").read().splitlines()  # read input file
for item in data:
    my_sentence += f"\n- {item}"
# my_sentence = "2----> [Hà Vân] : Vũ Khánh Uyên ơ vch sao k biết nhau z trời,ở Hà Nội nhé"

GUIDELINES_PROMPT = GUIDELINES_PROMPT.format(my_sentence)
ners = openai_chat_completion_response(GUIDELINES_PROMPT)

print(ners)

# import openai
# import json

# openai.api_key = "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"

# def get_named_entities(text):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=f"Extract named entities from the following text: {text}",
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     named_entities = json.loads(response.choices[0].text)
#     return named_entities

# text = "2----> [Hà Vân] : Vũ Khánh Uyên ơ vch sao k biết nhau z trời"

# named_entities = get_named_entities(text)
# print(named_entities)
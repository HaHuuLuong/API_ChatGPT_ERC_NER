# Define a function to classify emotion based on keywords
def classify_emotion(text):
    # Define a dictionary of keywords for each emotion
    keywords = {
        "[vui vẻ]": ["=))", "😂", "😊", "😍", "❤️", "🥰"],
        "[buồn chán]": ["😭", "😢", "🥲", "🙁", "😞"],
        "[tức giận]": ["🫠", "👿", "😡", "🤬"],
        "[sợ hãi]": ["😱", "😨", "😰"],
        "[ngạc nhiên]": ["😮", "😯", "🤯"],
        "[khinh thường]": ["🙄", "😒"]
    }
    # Loop through each emotion and keyword
    for emotion, words in keywords.items():
        # Check if any keyword is in the text
        if any(word in text for word in words):
            # Return the emotion as the label
            return emotion
    # If no keyword is found, return unknown as the label
    return "[không rõ]"
    
# Create a list of texts with conversations
texts = [
    "1--> [Quỳnh Ly-100005561651963] (25/04/2022 9:01:11 am): 2. thầy Quyết dậy thì A hoặc A+ trong tầm tay =))))",
    "1--> [Đức Béo-100003149258548] (25/04/2022 8:35:29 am): 1. Học mông lung lắm e ah. Bỏ đi :)))",
    "2----> [Thanh Thư-100004196402607] (25/04/2022 10:22:12 am): Đức Béo a vùi dập e thế",
    # ... add more texts here ...
]

# Loop through each text and apply the function to get the label
for text in texts:
    label = classify_emotion(text)
    print(text, label)
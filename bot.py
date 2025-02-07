import string
import pickle
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from util import JSONParser
import re
import inflect

p = inflect.engine()

def convert_number_to_text(text):
    words = text.split()
    converted_words = [p.number_to_words(word) if word.isdigit() else word for word in words]
    return ' '.join(converted_words)

def preprocess(chat):
    chat = chat.lower()
    chat = re.sub(r'[^\w\s\d]', '', chat)
    chat = convert_number_to_text(chat)  
    # tandabaca = tuple(string.punctuation)
    # chat = ''.join(ch for ch in chat if ch not in tandabaca)
    return chat

def bot_response(chat, pipeline, jp):
    chat = preprocess(chat)
    res = pipeline.predict_proba([chat])
    max_prob = max(res[0])
    if max_prob < 0.1:
        return "Maaf saya tidak paham maksud Anda" , None
    else:
        max_id = np.argmax(res[0])
        pred_tag = pipeline.classes_[max_id]
        return jp.get_response(pred_tag), pred_tag

# load data
path = "data/intents.json"
jp = JSONParser()
jp.parse(path)
df = jp.get_dataframe()

# preprocess data
df['text_input_prep'] = df.text_input.apply(preprocess)

# modeling
pipeline = make_pipeline(CountVectorizer(),
                        MultinomialNB(alpha=0.5))

# training
print("[INFO] Training Data ...")
pipeline.fit(df.text_input_prep, df.intents)
 
# accuracy
accuracy = pipeline.score(df.text_input_prep, df.intents)
print(f"Akurasi training: {accuracy:.4f}")


# saved model
with open("model_chatbot.pkl", "wb") as model_file:
    pickle.dump(pipeline, model_file)


# print("[INFO] Halo, Aku siap membantu kamu!")
# while True:
#     chat = input("YOU >> ")
#     res, tag = bot_response(chat, pipeline, jp)
#     print(f"RRIBot >> {res}")
#     if tag == 'bye':
#         break

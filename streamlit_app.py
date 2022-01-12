import streamlit as st
import nltk
from nltk.corpus import words
import re

st.title("Wordle ResCLUEr")

nltk.download('words')

five_letters = [word for word in words.words() if len(word)==5 ]

[a,b,c,d,e] = st.columns(5)
with a:
    first_letter = st.text_input(label="1st")
with b:
    second_letter = st.text_input(label="2nd")
with c:
    third_letter = st.text_input(label="3rd")
with d:
    fourth_letter = st.text_input(label="4th")
with e:
    fifth_letter = st.text_input(label="5tth")

clue = first_letter+second_letter+third_letter+fourth_letter+fifth_letter

st.markdown("### clue")

st.write(clue)

exclusions = st.text_input(label="exclusions")

for word in five_letters:
 if all(c in word for c in clue) and not any(c in word for c in exclusions):
   st.write(word)
  
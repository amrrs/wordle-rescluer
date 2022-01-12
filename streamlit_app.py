import streamlit as st
import nltk
from nltk.corpus import words
import re

st.title("Wordle ResCLUEr")

@st.cache
def download():
    nltk.download('words')
download()

five_letters = [word for word in words.words() if len(word)==5 ]

[a,b,c,d,e] = st.columns(5)
with a:
    first_letter = st.text_input(label="1st",value = 'a')
with b:
    second_letter = st.text_input(label="2nd", value = 'b')
with c:
    third_letter = st.text_input(label="3rd", value = 'e')
with d:
    fourth_letter = st.text_input(label="4th", value = '')
with e:
    fifth_letter = st.text_input(label="5tth", value = 't')

clue = first_letter+second_letter+third_letter+fourth_letter+fifth_letter

st.markdown("### clue")

st.write(clue)

st.markdown("# Exclusion letters")

exclusions = st.text_input(label="exclusions")

st.markdown("# Wordle Clues")

clue_result = []

for word in five_letters:
 if all(c in word for c in clue) and not any(c in word for c in exclusions):
   clue_result.append(word)

st.write(clue_result)
  
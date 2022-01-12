import streamlit as st # this is for web app
import nltk # nltk for english words
from nltk.corpus import words # nltk words is to get five letter words

st.title("Wordle ResCLUEr") # this is the title of the app

# this is to display the image of wordle game
st.image("https://www.dexerto.com/wp-content/uploads/2022/01/08/wordle-tweets.jpg.webp")

# download the english words dictionary 

@st.cache # cache the download process 
def download():
    nltk.download('words')
download()


# create a new list with only five letter words

five_letters = [word for word in words.words() if len(word)==5 ]

# create a five column grid

[a,b,c,d,e] = st.columns(5)

# get user input currently doesnt handle number of characters

with a:
    first_letter = st.text_input(label="1st",value = 'a')
with b:
    second_letter = st.text_input(label="2nd", value = 'b')
with c:
    third_letter = st.text_input(label="3rd", value = 'e')
with d:
    fourth_letter = st.text_input(label="4th", value = '')
with e:
    fifth_letter = st.text_input(label="5th", value = 't')

# combine all the letters 

clue = first_letter+second_letter+third_letter+fourth_letter+fifth_letter

st.markdown("### clue")

st.write(clue)

st.markdown("### Exclusion letters")

# exclusion letters where the grey grids are 

exclusions = st.text_input(label="exclusions")

st.markdown("# Wordle Clues")


# this is an empty list to show all the clue words

clue_result = []


for word in five_letters:
 if all(c in word for c in clue) and not any(c in word for c in exclusions):
   clue_result.append(word)

# print the output list of clues

st.write(clue_result) 
  
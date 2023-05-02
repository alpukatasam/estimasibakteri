import pickle
import streamlit as st

model = pickle.load(open('estimasibakteri.sav', 'rb'))
#'aluminium','arsenic','barium','cadmium','chloramine','chromium','copper','flouride','viruses'
# ,'lead','nitrates','nitrites','mercury','perchlorate','radium','selenium','silver','uranium'
st.title('Estimasi pada kandungan air per liternya')
aluminium = st.number_input('Input aluminium')
arsenic = st.number_input('Input arsenic')
barium = st.number_input('Input barium')
cadmium = st.number_input('Input cadmium')
chloramine = st.number_input('Input chloramine')
chromium = st.number_input('Input chromium')
copper = st.number_input('Input copper')
flouride = st.number_input('Input flouride')
viruses = st.number_input('Input viruses')
lead = st.number_input('Input lead')
nitrates = st.number_input('Input nitrates')
nitrites = st.number_input('Input nitrites')
mercury = st.number_input('Input mercury')
perchlorate = st.number_input('Input perchlorate')
radium = st.number_input('Input radium')
selenium = st.number_input('Input selenium')
silver = st.number_input('Input silver')
uranium = st.number_input('Input uranium')

predict = ''

if st.button('Estimasi Bakteri'):
    predict = model.predict(
        [[[aluminium,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium]]]
    )
    st.write ('Estimasi Bakteri: ', predict)
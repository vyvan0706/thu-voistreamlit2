import streamlit as st
import gTTS 
from ftlangdetect import detect as lang_detector
from deep_translator import GoogleTranslator

st.title(':blue[Lồng tiếng với chị Google]')
user_input= st.text_area('Nhập văn bản muốn lồng tiếng')
language_code_mapping={
     'Tiếng Việt':'vi',
     'Tiếng Anh':'en',
     'Tiếng Hàn':'ko',
     'Tiếng Nhật':'ja'
} 
translate = st.toggle('Dịch văn bản')
if translate:
     target_language= st.selectbox(
    'Chọn ngôn ngữ của bản dịch',
    ('Tiếng Việt','Tiếng Anh','Tiếng Hàn','Tiếng Nhật'))
     target_language_code=language_code_mapping[target_language]
submitbut=st.button('Xác nhận')
if user_input and submitbut:
     language_code=lang_detector(user_input)['lang']
     result= gtts.gTTS(text=user_input, lang=language_code)
     result.save('S2/result.mp3')
     col1,col2=st.columns(2)
     with col1:
       st.subheader('Văn bản gốc')
       st.audio('S2/result.mp3')
     if translate:
          translated_input = GoogleTranslator(source='auto', target=target_language_code).translate(user_input)  
          trans_result= gtts.gTTS(text=translated_input, lang=target_language_code)
          trans_result.save('S2/trans_result.mp3')
          with col2:
            st.subheader('Văn bản dịch')
            st.audio('S2/trans_result.mp3')


 

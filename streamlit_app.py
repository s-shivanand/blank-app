import streamlit as st

st.title("My new app")

# st.write("Sascha, you want to guess what my favourite cuisine is")

st.button("Reset", type="primary")
if st.button("Sascha, you want to guess what my favourite cuisine is?"):
    st.write("Of course, it is Indian")

if st.button("Next guess. Do you know how many languages I can read, write and speak?"):
    st.write("4 - Kannada, English, Hindi, German")
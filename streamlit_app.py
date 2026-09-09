import streamlit as st

st.title("Who wants to guess?")

# st.write("Sascha, you want to guess what my favourite cuisine is")

#st.button("Reset", type="primary")
#if st.button("Sascha, you want to guess what my favourite cuisine is?"):
 #   st.write("Of course, it is Indian")

#if st.button("Next guess. Do you know how many languages I can read, write and speak?"):
    #st.write("4 - Kannada, English, Hindi, German")


with st.expander("You want to guess what my favourite cuisine is?"):
    if st.button("Italian", type="tertiary"):
        st.write("*Nope!* 👎")
    if st.button("Chinese", type="tertiary"):
        st.write("*Nope!* 👎")
    if st.button("Japanese", type="tertiary"):
        st.write("*Nope!* 👎")
    if st.button("Indian", type="tertiary"):
        st.write("You are right!")
        st.balloons()
        with st.expander("Next guess. Do you know how many cuisines are within Indian cuisine?"):        
            st.write("Several regional-based-cuisines exist. Don't know the exact number -- atleast 30")
        with st.expander("What style of Indian cuisine do I mostly cook/eat?"):        
            st.write("South Indian. Specifically from Karnataka. Yum yum!")






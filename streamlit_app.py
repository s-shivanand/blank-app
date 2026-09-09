import streamlit as st

st.title("Who wants to guess?")

st.button("Reset", type="primary")

with st.expander("🍛 Guess my favourite cuisine"):
    if st.button("Italian", type="tertiary"):
        st.write("*Nope!* 👎")
        st.snow()

    if st.button("Chinese", type="tertiary"):
        st.write("*Nope!* 👎")
        st.snow()

    if st.button("Japanese", type="tertiary"):
        st.write("*Nope!* 👎")
        st.snow()

    if st.button("Indian", type="tertiary"):
        st.success("You are right! 🎉")
        st.balloons()

        # Question 2
with st.expander("🇮🇳 How many regional cuisines exist within Indian cuisine?"):

    num = st.selectbox(
        "Choose one:",
        [
            "Select an option...",
            "5-10",
            "10-20",
            "20-30",
            "30+"
        ],
        key="num_cuisines"
    )

    if st.button("Check answer", key="check_num"):
        if num == "30+":
            st.success("Correct! 🎉 There are 30+ well-known regional cuisines.")
        elif num == "Select an option...":
            st.warning("Please select an option first.")
        else:
            st.error("Not quite!")

# Question 3
with st.expander("👩‍🍳 What style of Indian cuisine do I mostly cook/eat?"):

    cuisine = st.selectbox(
        "Choose one:",
        [
            "Select an option...",
            "North Indian",
            "South Indian",
            "Bengali",
            "Gujarati",
            "Goan"
        ],
        key="fav_style"
    )

    if st.button("Check answer", key="check_style"):
        if cuisine == "South Indian":
            st.success("Correct! 😄")
            st.write(
                "Specifically **Karnataka cuisine**. "
                #"Think dosa, idli, bisi bele bath, ragi mudde, and delicious home-cooked meals!"
            )
        elif cuisine == "Select an option...":
            st.warning("Please select an option first.")
        else:
            st.error("Not quite!")
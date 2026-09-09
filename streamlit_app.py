import streamlit as st
import pandas as pd
import random

st.title("Who wants to guess?")

# ============================================================
# RESET BUTTON
# ============================================================

if st.button("Reset", type="primary"):
    for key in [
        "trivia_cuisine",
        "ingredient_options",
        "michelin_question",
        "ingredient_question"
    ]:
        st.session_state.pop(key, None)

    st.rerun()


# ============================================================
# QUESTION 1
# ============================================================

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


# ============================================================
# QUESTION 2
# ============================================================

with st.expander("🇮🇳 How many regional cuisines exist within Indian cuisine?"):

    num = st.selectbox(
        "Choose one:",
        [
            "Select an option...",
            "5–10",
            "10–20",
            "20–30",
            "30+"
        ],
        key="num_cuisines"
    )

    if st.button("Check answer", key="check_num"):

        if num == "30+":
            st.success(
                "Correct! 🎉 There are 30+ well-known regional cuisines."
            )

        elif num == "Select an option...":
            st.warning("Please select an option first.")

        else:
            st.error("Not quite!")


# ============================================================
# QUESTION 3
# ============================================================

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
                "Specifically from **Karnataka**."
            )

        elif cuisine == "Select an option...":
            st.warning("Please select an option first.")

        else:
            st.error("Not quite!")


# ============================================================
# CUISINE TRIVIA
# ============================================================

st.divider()

st.header("🌎 Cuisine Trivia")


# ============================================================
# DATA
# ============================================================

df = pd.DataFrame({
    "Cuisine": [
        "🇮🇹 Italian",
        "🇨🇳 Chinese",
        "🇯🇵 Japanese",
        "🇮🇳 Indian"
    ],
    "Michelin-starred restaurants": [
        783,
        233,
        846,
        181
    ],
    "Common/characteristic ingredient": [
        "Tomato",
        "Soy sauce / Soybean",
        "Rice",
        "Spices"
    ]
})


# ============================================================
# RANDOM CUISINE
# Keep the same cuisine until Reset is clicked
# ============================================================

if "trivia_cuisine" not in st.session_state:
    st.session_state.trivia_cuisine = df.sample(1).iloc[0]

random_cuisine = st.session_state.trivia_cuisine

selected_cuisine = random_cuisine["Cuisine"]
selected_michelin = random_cuisine["Michelin-starred restaurants"]
selected_ingredient = random_cuisine["Common/characteristic ingredient"]


# ============================================================
# NUMERICAL TRIVIA
# ============================================================

# Four answer ranges for each possible Michelin count
number_ranges = {
    181: [
        "50–100",
        "100–150",
        "150–200",
        "200–250"
    ],

    233: [
        "100–150",
        "150–200",
        "200–250",
        "250–300"
    ],

    783: [
        "500–600",
        "600–700",
        "700–800",
        "800–900"
    ],

    846: [
        "500–600",
        "600–700",
        "700–800",
        "800–900"
    ]
}


number_options = number_ranges[selected_michelin]


# Find the correct range
def get_correct_range(number):

    for option in number_ranges[number]:

        low, high = option.split("–")

        low = int(low)
        high = int(high)

        if low <= number <= high:
            return option

    return None


correct_number_range = get_correct_range(selected_michelin)


# ============================================================
# NUMERICAL TRIVIA QUESTION
# ============================================================

with st.expander(
    f"🔢 How many Michelin-starred restaurants are associated with "
    f"{selected_cuisine} cuisine?"
):

    number_answer = st.selectbox(
        "Choose a range:",
        ["Select an option..."] + number_options,
        key="michelin_question"
    )

    if st.button(
        "Check answer",
        key="check_michelin"
    ):

        if number_answer == "Select an option...":

            st.warning("Please select an option first.")

        elif number_answer == correct_number_range:

            st.success(
                f"🎉 Correct! The number is approximately "
                f"**{selected_michelin}**."
            )

        else:

            st.error(
                f"❌ Not quite! The answer is approximately "
                f"**{selected_michelin}**."
            )


# ============================================================
# CATEGORICAL TRIVIA
# Keep the same options until Reset is clicked
# ============================================================

if "ingredient_options" not in st.session_state:

    ingredient_options = [selected_ingredient]

    other_ingredients = df[
        df["Common/characteristic ingredient"] != selected_ingredient
    ]["Common/characteristic ingredient"].tolist()

    ingredient_options.extend(
        random.sample(other_ingredients, 3)
    )

    random.shuffle(ingredient_options)

    st.session_state.ingredient_options = ingredient_options

else:

    ingredient_options = st.session_state.ingredient_options


# ============================================================
# CATEGORICAL TRIVIA QUESTION
# ============================================================

with st.expander(
    f"Which is a common/characteristic ingredient "
    f"of {selected_cuisine} cuisine?"
):

    ingredient_answer = st.selectbox(
        "Choose an ingredient:",
        ["Select an option..."] + ingredient_options,
        key="ingredient_question"
    )

    if st.button(
        "Check answer",
        key="check_ingredient"
    ):

        if ingredient_answer == "Select an option...":

            st.warning("Please select an option first.")

        elif ingredient_answer == selected_ingredient:

            st.success(
                f"🎉 Correct! **{selected_ingredient}**."
            )

        else:

            st.error(
                f"❌ Not quite! The answer is "
                f"**{selected_ingredient}**."
            )
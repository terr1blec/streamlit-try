import streamlit as st
from datetime import datetime, time

st.header("st.slider")
st.subheader("Slider")

age = st.slider("How old are you?", min_value=0, max_value=100, value=25, step=1)
st.write("I'm ", age, "years old")

st.subheader("Range slider")

range = st.slider(
    "Select a range of values",
    min_value=0,
    max_value=100,
    value=(25, 75),
)
st.write("The selected range is from", range[0], "to", range[1])

appointment = st.slider(
    "Schedule your appointment:",
    min_value=datetime(2022, 1, 1, 9, 30),
    max_value=datetime(2022, 1, 1, 12, 0),
    value=datetime(2022, 1, 1, 10, 0),
    format="MM/DD/YYYY HH:mm",
)
st.write("Your appointment is scheduled for", appointment)

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

st.subheader("Range time slider")

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

st.subheader("When do you want to wake up?")

wakeup = st.slider(
    "What's the earliest time you can wake up?",
    value=(time(6, 0), time(8, 0)),
    format="HH:mm",
)

import streamlit as st
from datetime import datetime

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

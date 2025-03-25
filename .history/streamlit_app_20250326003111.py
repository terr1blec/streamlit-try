import streamlit as st
from datetime import datetime

st.header("st.slider")
st.subheader("Slider")

age = st.slider("How old are you?", min_value=0, max_value=100, value=25, step=1)

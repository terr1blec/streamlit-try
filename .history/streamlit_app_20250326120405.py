import streamlit as st
from datetime import datetime, time
import pandas as pd
import numpy as np

st.header("st.line_chart")

chart_data = pd.DataFrame(np.random.randn(30, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

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

st.subheader("Datetime slider")

start_time = st.slider(
    "When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm"
)
st.write("Start time:", start_time)

import streamlit as st

st.write("st.button")

if st.button(label="say hello"):
    st.write("why hello there")
else:
    st.write("goodbye")

st.write("st.button can be used with")

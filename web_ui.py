import streamlit as st
from streamlit import checkbox

import functions

todos =functions.get_todos()
st.title("My Todos App")
st.write("This App is designed to increase your productivity")

st.checkbox("test")
# def add_todos():
#     pass

for todo in todos:
    st.checkbox(todo)


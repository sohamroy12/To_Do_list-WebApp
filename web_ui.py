import streamlit as st
from streamlit import checkbox

import functions

todos = functions.get_todos()
todos = [t for t in todos if t.strip() != ""]   # Remove empty entries

def add_todo():
    todo = st.session_state["new_todo"] = "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todos App")
st.write("This App is designed to increase your productivity")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=f"todo_{i}")

st.text_input(label=" ", label_visibility="collapsed", placeholder="Add new To Do here!",
              on_change=add_todo, key='new_todo')


st.session_state
import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open('todos.txt', 'w') as file:
        pass

todos = functions.get_todos()
# todos = [t for t in todos if t.strip() != ""]   # Remove empty entries

st.title("My Todos App")
st.write("This App is designed to increase your productivity")

def add_todo():
    todo = st.session_state["new_todo"]
    if todo.strip():  # Avoid empty input
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear the input

st.text_input(label=" ", label_visibility="collapsed", placeholder="Add new To Do here!",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox_key = f"todo_{index}"
    if st.checkbox(todo, key=checkbox_key):
        todos.pop(index)
        functions.write_todos(todos)
        if checkbox_key in st.session_state:
            del st.session_state[checkbox_key]
        st.rerun()


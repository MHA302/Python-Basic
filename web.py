import streamlit as st
import functions



todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.add_todos(todos)


st.title("My ToDO app")
st.subheader("This is my todo app.")
st.write("This Application is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")


import streamlit as st
import functions


todos = functions.get_todos()
st.title("My ToDO app")
st.subheader("This is my todo app.")
st.write("This Application is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Add new todo...")


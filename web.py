# To run streamlit run web.py
# pip freeze > requirements.txt
# to have packages on requirements file
import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# Creating a title
st.title("My To-Do App.")
# Creating sub header
st.subheader("This is my todo app.")
# Creating write
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(
    label="Enter a todo: ",
    placeholder="Add a new todo",
    on_change=add_todo,
    key="new_todo",
)

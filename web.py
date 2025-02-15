import streamlit as st
import functions as fn

todo_list = fn.file_read()

def get_todo():
    add_todo = st.session_state["Add"]
    todo_list.append(add_todo + "\n")
    fn.file_write(todo_list)


st.title("To-Do App")
st.subheader("This is my todo app")
st.write("This app is to increase my productivity.")

for todo in todo_list:
    st.checkbox(todo, key = todo)
    if(st.session_state[todo] == True):
        todo_list.remove(todo)
        fn.file_write(todo_list)
        del st.session_state[todo]
        st.rerun()


st.text_input(label = "",placeholder ="Enter a to-do",on_change = get_todo, key = "Add")

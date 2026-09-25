import streamlit as st

import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# to run it i have to go to terminal
# then write the streamlit run web.py
# pip freeze > requirements.txt

st.title("My todo App")
st.subheader("this is my todo App.")
st.write("this app is to increase your productivity")
# st.checkbox("Buy Grocery Store")
# st.checkbox("Buy Apple Store")

for index,item in enumerate(todos):
    checkbox = st.checkbox(item,key=item)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

test_input = st.text_input(on_change=add_todo,key="new_todo",label="Enter a Label",placeholder="Enter a Todo")

print("Hello")

# while True:
#     list = functions.get_todos()
#     list.append(test_input)
#     print(list)
#     functions.get_todos(list)
#     break

st.session_state


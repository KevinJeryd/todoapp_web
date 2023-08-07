import streamlit as st

import backend
import helper_functions


def add_todo():
    backend.add_todo(helper_functions.get_todolist(), st.session_state['new_todo'])
    st.session_state['new_todo'] = ''


st.title('Todo Application')
st.subheader('Current todos:')

for todo in helper_functions.get_todolist():
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        backend.complete_todo(helper_functions.get_todolist(), todo)
        del st.session_state[todo]
        st._rerun()

st.text_input(label='Add Todo', label_visibility='hidden', placeholder='Add a new todo...', key='new_todo',
              on_change=add_todo)

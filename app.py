import streamlit as st
# app title
st.title("To-Do List App")

# installation session state for task
if "task" not in st.session_state:
  st.session_state.task = []

  # side header
st.sidebar.header("Manage your task")

# text input
new_task = st.sidebar.text_input("Add a new task:", placeholder = "Enter your task here...")
if st.sidebar.button("Add task"):
  if new_task.strip():
    st.session_state.task.append({"task": new_task, "completed":False})
    st.success("Task add successfully")
  else:
     st.warning("Task can not be empty")


#displa task
st.subheader("Your To-Do List")
if not st.session_state.task:
  st.info("No task added yet")
else:
  for index, task in enumerate(st.session_state.task):
    col1, col2, col3 = st.columns([0.7,0.15,0.15])

    # mark as completed
    completed = col1.checkbox(f"**{task['task']}**", task['completed'], key=f"check_{index}")
    if completed != task["completed"]:
      st.session_state.task[index]["completed"] = completed

      # updated task
    if col2.button("Edit", key=f"edit_{index}"):  
        new_task = st.text_input("Edit task", task["task"], key=f"edit_{index}")  
        if new_task and st.button("Save", key=f"save_{index}"):
          st.session_state.task[index]["task"] = new_task
          st.experimental_rerun() 

   # delete task

    if col3.button("Delete", key=f'delete_{index}'):
      del st.session_state.task[index]
      st.experimental_rerun()

  # clear all task
  if st.button("Clear all"):
      st.session_state.task = []
      st.success("All task deleted successfully!!")

  # footer
  st.markdown('---')
  st.caption("Stay organized and productive with this simple To-Do app")
   


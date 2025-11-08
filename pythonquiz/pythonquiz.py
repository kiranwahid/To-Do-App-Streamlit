import streamlit as st
import time

# Inject custom CSS for background and animations
st.markdown("""
    <style>
        body {
            background-color: #f0f4c3;
            background-image: url('https://www.transparenttextures.com/patterns/wood-pattern.png');
            animation: backgroundAnimation 10s infinite alternate;
            color: #333;
            font-family: 'Arial', sans-serif;
        }

        @keyframes backgroundAnimation {
            0% {background-color: #f0f4c3;}
            100% {background-color: #c3f4f0;}
        }

        .question {
            padding: 20px;
            margin-bottom: 15px;
            background-color: #fff;
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        .correct {
            color: green;
            font-weight: bold;
        }

        .wrong {
            color: red;
            font-weight: bold;
        }

        .header {
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
            color: #fff;
        }

        .final-score {
            font-size: 24px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Quiz questions
questions = [
    {"question": "Which of the following is used to define a function in Python?", "choices": ["func", "def", "function", "define"], "answer": "def"},
    {"question": "What is the output of `print(2 ** 3)`?", "choices": ["6", "8", "9", "16"], "answer": "8"},
    {"question": "What is the correct file extension for Python files?", "choices": [".pyt", ".pt", ".py", ".pyth"], "answer": ".py"},
    {"question": "Which keyword is used to create a class in Python?", "choices": ["class", "def", "struct", "object"], "answer": "class"},
    {"question": "How do you insert comments in Python code?", "choices": ["//", "/* */", "#", "<!-- -->"], "answer": "#"},
    {"question": "What does the 'len()' function do in Python?", "choices": ["Returns the length", "Deletes an object", "Creates a list", "Opens a file"], "answer": "Returns the length"},
    {"question": "Which of the following is used to handle exceptions?", "choices": ["if-else", "try-except", "loop", "break-continue"], "answer": "try-except"},
    {"question": "What is the output of `print('Hello' + 'World')`?", "choices": ["Hello World", "HelloWorld", "Hello", "Error"], "answer": "HelloWorld"},
    {"question": "What data type is the result of `10 / 3`?", "choices": ["Integer", "Float", "String", "Boolean"], "answer": "Float"},
    {"question": "Which method is used to add an element to a list?", "choices": ["add()", "append()", "insert()", "push()"], "answer": "append()"},
    {"question": "How do you create a variable in Python?", "choices": ["$var", "var:", "var =", "declare var"], "answer": "var ="},
    {"question": "What is the output of `type(3.14)`?", "choices": ["int", "float", "str", "bool"], "answer": "float"},
    {"question": "Which of the following can be used to create a loop?", "choices": ["if-else", "for", "class", "def"], "answer": "for"},
    {"question": "What is the keyword used to define a lambda function?", "choices": ["lambda", "func", "def", "anon"], "answer": "lambda"},
    {"question": "How do you start a comment in Python?", "choices": ["//", "#", "/*", "<!--"], "answer": "#"},
    {"question": "What is the result of `10 % 3`?", "choices": ["1", "3", "0", "2"], "answer": "1"},
    {"question": "Which of the following is not a valid variable name?", "choices": ["my_var", "2var", "var2", "_myvar"], "answer": "2var"},
    {"question": "How do you create a dictionary?", "choices": ["()", "{}", "[]", "<>"], "answer": "{}"},
    {"question": "Which function is used to get input from the user?", "choices": ["input()", "raw_input()", "get()", "scan()"], "answer": "input()"},
    {"question": "How do you remove an element from a list?", "choices": ["delete()", "remove()", "pop()", "Both remove() and pop()"], "answer": "Both remove() and pop()"}
]

# Title
st.markdown("<div class='header'>Python Quiz 🎉</div>", unsafe_allow_html=True)

# Initialize score and question index
score = 0
index = 0
total_questions = len(questions)

# Loop through the questions
for q in questions:
    with st.container():
        st.markdown(f"<div class='question'><b>{q['question']}</b></div>", unsafe_allow_html=True)
        
        # Capture user input as a select box for choices
        user_answer = st.radio("Choose the correct answer:", q['choices'], key=index)

        # Check if the answer is correct
        if st.button(f"Submit Answer for Q{index+1}", key=f"submit_{index}"):
            if user_answer == q["answer"]:
                st.markdown("<div class='correct'>✅ Correct!</div>", unsafe_allow_html=True)
                score += 1
            else:
                st.markdown(f"<div class='wrong'>❌ Incorrect! The correct answer was {q['answer']}.</div>", unsafe_allow_html=True)
        index += 1
        st.markdown("---")  # Line separator for each question

# Show the final score
if st.button("Show Final Score"):
    st.markdown(f"<div class='final-score'>🎯 You answered {score} out of {total_questions} questions correctly!</div>", unsafe_allow_html=True)

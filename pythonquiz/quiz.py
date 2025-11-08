import time

questions = [
{
        "question": "1. Which of the following is used to define a function in Python? 🐍",
        "choices": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "question": "2. What is the output of `print(2 ** 3)`? 🔢",
        "choices": ["A) 6", "B) 8", "C) 9", "D) 16"],
        "answer": "B"
    },
    {
        "question": "3. What is the correct file extension for Python files? 📂",
        "choices": ["A) .pyt", "B) .pt", "C) .py", "D) .pyth"],
        "answer": "C"
    },
    {
        "question": "4. Which keyword is used to create a class in Python? 🏷️",
        "choices": ["A) class", "B) def", "C) struct", "D) object"],
        "answer": "A"
    },
    {
        "question": "5. How do you insert comments in Python code? 💬",
        "choices": ["A) //", "B) /* */", "C) #", "D) <!-- -->"],
        "answer": "C"
    },
    {
        "question": "6. What does the 'len()' function do in Python? 📏",
        "choices": ["A) Returns the length of an object", "B) Deletes an object", "C) Creates a list", "D) Opens a file"],
        "answer": "A"
    },
    {
        "question": "7. Which of the following is used to handle exceptions in Python? ⚠️",
        "choices": ["A) if-else", "B) try-except", "C) loop", "D) break-continue"],
        "answer": "B"
    },
    {
        "question": "8. What is the output of `print('Hello' + 'World')`? 🌍",
        "choices": ["A) Hello World", "B) HelloWorld", "C) Hello", "D) Error"],
        "answer": "B"
    },
    {
        "question": "9. What data type is the result of `10 / 3` in Python? ➗",
        "choices": ["A) Integer", "B) Float", "C) String", "D) Boolean"],
        "answer": "B"
    },
    {
        "question": "10. Which method is used to add an element to a list in Python? 📋",
        "choices": ["A) add()", "B) append()", "C) insert()", "D) push()"],
        "answer": "B"
    },
    {
        "question": "11. How do you create a variable in Python? 📝",
        "choices": ["A) $var", "B) var:", "C) var =", "D) declare var"],
        "answer": "C"
    },
    {
        "question": "12. What is the output of `type(3.14)`? 📐",
        "choices": ["A) int", "B) float", "C) str", "D) bool"],
        "answer": "B"
    },
    {
        "question": "13. Which of the following can be used to create a loop in Python? 🔄",
        "choices": ["A) if-else", "B) for", "C) class", "D) def"],
        "answer": "B"
    },
    {
        "question": "14. What is the keyword used to define a lambda function in Python? 🏷️",
        "choices": ["A) lambda", "B) func", "C) def", "D) anon"],
        "answer": "A"
    },
    {
        "question": "15. How do you start a comment in Python? 💬",
        "choices": ["A) //", "B) #", "C) /*", "D) <!--"],
        "answer": "B"
    },
    {
        "question": "16. What is the result of `10 % 3` in Python? ➗",
        "choices": ["A) 1", "B) 3", "C) 0", "D) 2"],
        "answer": "A"
    },
    {
        "question": "17. Which of the following is not a valid variable name in Python? 🚫",
        "choices": ["A) my_var", "B) 2var", "C) var2", "D) _myvar"],
        "answer": "B"
    },
    {
        "question": "18. How do you create a dictionary in Python? 📚",
        "choices": ["A) ()", "B) {}", "C) []", "D) <>"],
        "answer": "B"
    },
    {
        "question": "19. Which function is used to get input from the user in Python? 🖥️",
        "choices": ["A) input()", "B) raw_input()", "C) get()", "D) scan()"],
        "answer": "A"
    },
    {
        "question": "20. How do you remove an element from a list in Python? 📋",
        "choices": ["A) delete()", "B) remove()", "C) pop()", "D) Both B and C"],
        "answer": "D"
    }

]


# Initialize score value
score = 0
time_limit = 10

# Welcome message
print("🎉 Welcome to the Python Quiz! 🎉\n")
print(f"⏳You have {time_limit} seconds to answer each question \n")

start_quiz = input("🚀 Are you ready to  start the quiz? (yes/no)").lower()

if start_quiz == "yes":
  # Loop through each question
  for q in questions:
    print(q["question"])
    for choice in q["choices"]:
        print(choice)
    
    start_time = time.time()
    # Get user input
    user_input = input("📝 Enter the correct option: ").upper()
    
    time_taken = time.time() - start_time
    
    if time_taken > time_limit:
      print(f"⏰ Time's up! You took {int(time_taken)} seconds. Moving to the next question.\n")
      continue
    # Check answer
    if user_input == q["answer"]:
        print("Congratulation 🎉 the answer is Correct! ✅\n")
        score += 1
    else:
        print(f"❌Wrong! The correct answer was {q['answer']}\n")

    # Display final score
  print(f"🎯 You answered {score} out of {len(questions)} questions correctly!\n")
  print("🙌 Thank you for playing the Python Quiz! Goodbye! 🎉\n")
else:
  print("\n Maybe nexttime. Goodbye!👋")
    
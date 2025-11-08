# import streamlit as st
# import random
# import string

# def password_generator(length, digit, special_character):
#     character = string.ascii_letters
    
#     if digit:
#         character += string.digits
        
        
        
#     if special_character:
#         character += string.punctuation
        
        
#     return ''.join(random.choice(character) for _ in range(length))

# st.title("Password Generator🔒")
# length = st.slider("Password Length", min_value=6, max_value=32, value=12)
# digit = st.checkbox("Addd Digits")
# special_character = st.checkbox("Add Special Character")
# if st.button("Generate Password"):
#     password = password_generator(length, digit, special_character)
#     st.write(f"Your Generated Password is here {password}🔢")

        

# st.markdown("""---
#             Build by kiran wahid❤️
#             """)


import streamlit as st
import random
import string

# Set the page background color
st.markdown(
    """
    <style>
    .stApp {
        background-color:#ffeaa7;
    }
    </style>
    """, unsafe_allow_html=True
)

def password_generator(length, digit, special_character):
    character = string.ascii_letters
    
    if digit:
        character += string.digits
        
    if special_character:
        character += string.punctuation
        
    return ''.join(random.choice(character) for _ in range(length))

# Title with emoji

st.title("🔒 Password Generator 💻")
# Add a fun subtitle

# Custom styling for headers
st.markdown("<h3 style='color: #d63031;'>Generate your strong, unique password with a few clicks! 🔑</h3>", unsafe_allow_html=True)

# Sliders and checkboxes
length = st.slider("🔢 Password Length", min_value=6, max_value=32, value=12)
digit = st.checkbox("🔡 Add Digits")
special_character = st.checkbox("🔠 Add Special Characters")

# Button to generate password
if st.button("🔄 Generate Password ✨"):
    password = password_generator(length, digit, special_character)
    st.markdown(f"<h4 style='color: green;'>🎉 Your Generated Password is: </h4><h2 style='color:#d35400 ;font-size:24px;'>{password}</h2>", unsafe_allow_html=True)
    
# Footer
st.markdown("""---""")
st.markdown("<h5 style='text-align: center;'>🔑 Built with ❤️ by Kiran Wahid</h5>", unsafe_allow_html=True)

import streamlit as st

def unit_converter_fun(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers":0.001,                       #   1 meter = 0.001 kilometer
        "kilometers_meters": 1,                            #   1 kilometer = 1000 meter
        "grams_kilograms":0.001,                           #   1 gram = 0.001 kilogram
        "kilograms_grams":1000                              #   1 kilogram = 1000 gram
    }
    
    #  Generate a key based on the input output units
    key = f"{unit_from}_{unit_to}"  
    
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return 'Conversion not found'
    
    st.title("Unit Converter")
    value = st.number_input("Enter the value to convert: ")
    unit_from = st.selectbox("Convert From: ", ["meters", "kilometers", "grams", "kilograms"])
    unit_to = st.selectbox("Convert To: ", ["meters", "kilometers", "grams", "kilograms"])
    
    if st.button("Convert"):
        result = unit_converter_fun(value, unit_from, unit_to)
        st.write(f"Converted Value is here: {result}")
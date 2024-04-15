import streamlit as st

def calculator():
    st.title("Simple Calculator")
    
    num1 = st.number_input("Enter the first number:")
    operation = st.selectbox("Select operation", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter the second number:")
    
    if st.button("Calculate"):
        if operation == "+":
            result = num1 + num2
            st.success(f"{num1} {operation} {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            st.success(f"{num1} {operation} {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            st.success(f"{num1} {operation} {num2} = {result}")
        elif operation == "/":
            if num2 == 0:
                st.error("Error: Division by zero!")
            else:
                result = num1 / num2
                st.success(f"{num1} {operation} {num2} = {result}")

calculator()

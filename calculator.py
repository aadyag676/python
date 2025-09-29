#streamlit run calculator.py
import streamlit as st

st.title("simple calculator")
#st.subheader("perform basic arithmetic operations")
st.markdown("this is a simple calculator app built with streamlit")

#input fields for numbers
c1,c2 = st.columns(2)
fnum = c1.number_input("enter the first number",value=0)
snum = c2.number_input("enter the second number",value=0)

options =["addition","subtraction","multiplication","division"]
choice = st.radio("select an operation", options)

button = st.button("calculate")

result = 0
if button:
    if choice=="addition":
       result = fnum+snum
    if choice=="subtraction":
       result = fnum-snum
    if choice=="multiplication":
       result = fnum*snum
    if choice=="division":
       result = fnum/snum
st.success(f"result is  : {result}")

st.balloons()
st.snow()
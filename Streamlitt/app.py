import streamlit as st
import pandas as pd


# Ttile
st.title("My Application")

# text
st.write("This is just a single text")
st.write(pd.DataFrame({"First Col": [1,2,3], "Second Col": [1,4,9]}))

# Text_input
name =st.text_input("Enter Your Name: ")
if name:
    st.write(f"Hy {name}")


# make slider
# min, max, default
age =st.slider("Select age", 0, 100, 25)
st.write(f"Your age: {age}")


# selectbox
selected =st.selectbox("Select yout fvt field", ["Data Science", "ML", "Web Development"])
st.write(f"Your fvt field {selected}")

# upload file
uploaded =st.file_uploader("Upload File", type="csv")
if uploaded:
    st.write(pd.read_csv(uploaded, sep=","))




data =pd.DataFrame({"First Col": [1,2,3], "Second Col": [1,4,9]})
# display line chart
st.line_chart(data)

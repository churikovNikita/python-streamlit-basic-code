import streamlit as st

# Basic Streamlit Command
st.header("It's Header")
st.title("That is a title")
st.subheader("This is a subheader")
st.text("This is a text")

# Some example on Markdown
st.markdown("### That is header3 markdown")
st.markdown("> It's also some future about makrdown")


# That is about how to write a code to easy copy-paste
str = "print('Hello World')"
st.text('That is about use "code"')
st.code(str)

# Horizontal line
st.markdown("---")

# Link using Markdown
st.markdown("[That is a google link, on Markdown](https://google.com)")

# Creating a table using Markdown
table = """
| That is a | Table |
| ----------- | ------- |
| also | on |
| Markdown | Text | 
"""
st.markdown(table)

# Emojie using Markdown
st.markdown(":joy: Emojie is also work, Markdown")


# Specific data, like Wind, Money can be present with this tool. Somethink volatility
st.text('That is about use "metric"')
st.metric(label="Wind Speed", value="70ms", delta="5.8")

# original Streamlink Table Example 2Column 5 Rows
tableNormal = {
    "Streamlit Column1": [1, 2, 3, 4, 5],
    "Streamlit Column2": [6, 7, 8, 9, 10],
}
st.table(tableNormal)

# LIKE SQL Table is very intresting by sorting data3
tableLikeSQL = {
    "Streamlit Like SQL Col1": [1, 2, 3, 4, 5],
    "Streamlit Like SQL Col2": [6, 7, 8, 9, 10],
}
st.dataframe(tableLikeSQL)

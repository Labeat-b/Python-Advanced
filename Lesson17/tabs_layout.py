import streamlit as st

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("content for tab 1")
    st.write("This is the content of Tab 1.")

with tab2:
    st.header("content for tab 2")
    st.write("This is the content of Tab 2.")

with tab3:
    st.header("content for tab 3")
    st.write("This is the content of Tab 3.")
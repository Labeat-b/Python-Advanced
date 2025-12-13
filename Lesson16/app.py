import streamlit as st

def main():
    st.title("Hello, World!")

    if st.button("Click Me"):
        st.write("Button Clicked!")

    st.checkbox("Check Me")

    if st.checkbox("Check me to show some text"):
        st.write("You are seeing this text because you checked the check box!")

    user_input = st.text_input("Enter text:", "Sample Text")
    st.write(f"You entered: {user_input}")

    age= st.number_input("Enter your age:", min_value=0 , max_value=120)
    st.write(f"Your age is: {age}")

    message = st.text_area("Enter a message:")
    st.write(f"Your message: {message}")
    
    choice = st.radio("Pick one:", ("Choice 1", "Choice 2", "Choice 3"))
    st.write(f"You chose: {choice}")

    if st.button("Success"):
        st.success("Operation was successful! The patient has died")

    try:
        1/0
    except Exception as e:
        st.exception(e)

if __name__ == "__main__":
    main()


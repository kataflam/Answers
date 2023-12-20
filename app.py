import streamlit as st

# Define the list of items
items = {
 1: "In the museum where Ross works",
2: "Beach house",
3: "Weekend at Bernies",
4: "مونا - Mona"
}

def main():
    # Add a background image
    st.markdown(
        """
        <style>
            body {
                background-image: url('web1.png');  /* Updated to use web1.png in the same directory */
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Number Text Answer")

    user_input = st.number_input("Enter a number from 1 to 300:", min_value=1, max_value=300, step=1)
    show_answer = st.button("Show Answer")

    if show_answer:
        answer = items.get(int(user_input), 'No information available for this number.')
        st.write(f'Text answer: {answer}')

if __name__ == '__main__':
    main()

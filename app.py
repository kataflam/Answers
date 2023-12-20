
import streamlit as st

# Define the list of items
items = {
    1: "In the museum where Ross works",
    2: "Beach house",
    3: "Weekend at Bernies",
    4: "مونا - Mona",
    5: "Bicycle",
    6: "Frank Jr. Jr., Leslie, Chandler",
    7: "Dentist",
    8: "Bonnie and Julie",
    9: "Brad Pitt",
    10: "Van Damme",

}

def main():
    st.title("Number Text Answer")

    user_input = st.number_input("Enter a number from 1 to 300:", min_value=1, max_value=300, step=1)
    answer = items.get(int(user_input), 'No information available for this number.')

    st.write(f'Text answer: {answer}')

if __name__ == '__main__':
    main()




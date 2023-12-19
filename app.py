from flask import Flask, render_template, request

app = Flask(__name__)

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
   

    299: "رايتشيل",
    300: "د. جرين أبو رايتشيل",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        try:
            user_input = int(request.form['user_input'])
            if 1 <= user_input <= 300:
                # Check if the user input exists in the items dictionary
                if user_input in items:
                    answer = items[user_input]
                else:
                    answer = 'No information available for this number.'
            else:
                answer = 'Please enter a number between 1 and 300.'
        except ValueError:
            answer = 'Invalid input. Please enter a valid number.'

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

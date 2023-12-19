from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        try:
            user_input = int(request.form['user_input'])
            if 1 <= user_input <= 300:
                # Your logic to generate the text answer based on user_input
                answer = f'Text answer for {user_input}'
            else:
                answer = 'Please enter a number between 1 and 300.'
        except ValueError:
            answer = 'Invalid input. Please enter a valid number.'

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

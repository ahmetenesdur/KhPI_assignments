from flask import Flask, render_template

# Initializing the Flask application
app = Flask(__name__)

# Setting up a route for the home page


@app.route('/')
def home():
    # Example data dictionary which will be passed to the template
    data = {'example_data': [1, 2, 3, 4, 5]}

    # Rendering the template with the data
    return render_template('template.html', data=data)


# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)

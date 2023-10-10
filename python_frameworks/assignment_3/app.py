from flask import Flask, render_template, request, abort, flash, redirect, url_for

trips = [
    {"country": "Turkey", "tour_operator": "Operator1",
        "price": 1000, "number_of_days": 7},
    {"country": "Spain", "tour_operator": "Operator1",
        "price": 700, "number_of_days": 5},
    {"country": "Greece", "tour_operator": "Operator2",
        "price": 1200, "number_of_days": 10},
    {"country": "Italy", "tour_operator": "Operator3",
        "price": 800, "number_of_days": 6},
    {"country": "France", "tour_operator": "Operator4",
        "price": 900, "number_of_days": 5},
    {"country": "Turkey", "tour_operator": "Operator5",
        "price": 1500, "number_of_days": 8},
    {"country": "Japan", "tour_operator": "Operator1",
        "price": 2000, "number_of_days": 14},
    {"country": "Australia", "tour_operator": "Operator2",
        "price": 2500, "number_of_days": 15},
    {"country": "Canada", "tour_operator": "Operator3",
        "price": 1800, "number_of_days": 12},
    {"country": "USA", "tour_operator": "Operator4",
        "price": 2200, "number_of_days": 10},
    {"country": "Turkey", "tour_operator": "Operator5",
        "price": 1800, "number_of_days": 10},
]


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', trips=trips)


@app.route('/tour', methods=['GET'])
def tour():
    operator = request.args.get('operator')
    days = request.args.get('days')

    if operator:
        result = [trip for trip in trips if trip['tour_operator'].lower()
                  == operator.lower()]
    elif days:
        result = [
            trip for trip in trips if trip['number_of_days'] >= int(days)]
    else:
        result = trips

    if result:
        return render_template('tour.html', trips=result)
    else:
        return render_template('tour.html', msg="No data")


@app.route('/expensive_turkey_tour')
def expensive_turkey_tour():
    turkey_trips = [
        trip for trip in trips if trip['country'].lower() == 'turkey']
    if turkey_trips:
        most_expensive_trip = max(turkey_trips, key=lambda x: x['price'])
        return render_template('tour.html', trips=[most_expensive_trip])
    else:
        return render_template('tour.html', msg="No data")


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/process_form', methods=['POST'])
def process_form():
    input_data = request.form['inputField']
    if not input_data:
        flash('Input field cannot be empty', 'danger')
        return redirect(url_for('form'))
    return render_template('result.html', data=input_data)


@app.route('/additional_form')
def additional_form():
    return render_template('additional_form.html')


@app.route('/process_additional_form', methods=['POST'])
def process_additional_form():
    # Adjusted to match the name attribute in the form
    country = request.form['country']
    preferred_duration = request.form['otherOptions']
    # Determine the minimum and maximum number of days based on the preferred_duration
    min_days, max_days = {
        'short': (1, 3),
        'medium': (4, 7),
        'long': (8, float('inf'))
    }[preferred_duration]
    # Filter the trips based on the selected country and preferred tour duration
    filtered_trips = [
        trip for trip in trips
        if country.lower() == trip['country'].lower()
        and min_days <= trip['number_of_days'] <= max_days
    ]
    return render_template(
        'additional_form_result.html',
        country=country,  # Adjusted from region=country to country=country
        preferred_duration=preferred_duration,
        trips=filtered_trips
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

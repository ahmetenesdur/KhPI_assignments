from flask import Flask, render_template, request, abort
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

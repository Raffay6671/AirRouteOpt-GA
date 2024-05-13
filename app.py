from flask import Flask, render_template, request, jsonify
from main import Manager  # Importing Manager from main.py
from main import convert_date_format

app = Flask(__name__)

# Initialize the Manager
manager = Manager('aircrafts.csv', 'airports.csv', 'weathers.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_optimized_path', methods=['POST'])
def calculate_optimized_path():
    data = request.get_json()
    source = data['source']
    destination = data['destination']
    date = data['date']

    # Here, integrate the logic to find the optimized route
    optimized_route = manager.find_optimized_route(source, destination, date)

    # Format the optimized route into a readable format
    formatted_route = format_optimized_route(optimized_route)
    return jsonify(optimized_route=formatted_route)

def format_optimized_route(route):
    # Format the route for frontend display
    # Assuming the route is a list of airport names or city names
    return ' -> '.join(route)

if __name__ == '__main__':
    app.run(debug=True)

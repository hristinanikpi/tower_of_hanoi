from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for API access

# Recursive function for Tower of Hanoi
def tower_of_hanoi(n, source, destination, auxiliary, moves):
    if n == 1:
        moves.append(f"Take disk 1 from rod {source} to rod {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination, moves)
    moves.append(f"Take disk {n} from rod {source} to rod {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source, moves)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# API to solve the Tower of Hanoi puzzle, accepting JSON input
@app.route('/solve_hanoi', methods=['POST'])
def solve_hanoi():
    data = request.get_json()
    disks = data.get('disks')

    if not isinstance(disks, int) or disks < 1:
        return jsonify({"error": "Invalid number of disks"}), 400

    moves = []
    tower_of_hanoi(disks, 'A', 'C', 'B', moves)

    return jsonify({"disks": disks, "moves": moves})

if __name__ == '__main__':
    app.run(debug=True)

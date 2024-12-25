from flask import Flask, render_template, jsonify
import random
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        "processed": random.randint(1000, 5000),
        "users": random.randint(100, 500),
        "errors": random.randint(0, 50)
    })

@app.route('/api/chart')
def chart():
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
    values = [random.randint(50, 200) for _ in labels]
    return jsonify({
        "labels": labels,
        "values": values
    })

@app.route('/api/table')
def table():
    entries = [
        {"id": i, "name": f"User {i}", "status": random.choice(["Active", "Inactive"]), 
         "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        for i in range(1, 11)
    ]
    return jsonify({"entries": entries})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

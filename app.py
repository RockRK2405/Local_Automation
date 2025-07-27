from flask import Flask, jsonify
from automator import simulate_launch_instance, fetch_output, simulate_terminate_instance

app = Flask(__name__)
instance_active = False

@app.route("/start", methods=["POST"])
def start_instance():
    global instance_active
    simulate_launch_instance()
    instance_active = True
    return jsonify({"message": "Instance started and script executed."})

@app.route("/output", methods=["GET"])
def get_output():
    if not instance_active:
        return jsonify({"error": "No running instance."})
    output = fetch_output()
    return jsonify({"output": output})

@app.route("/stop", methods=["POST"])
def stop_instance():
    global instance_active
    if not instance_active:
        return jsonify({"error": "No instance to terminate."})
    msg = simulate_terminate_instance()
    instance_active = False
    return jsonify({"message": msg})

if __name__ == "__main__":
    print("🚀 Starting Flask API for local cloud simulation...")
    app.run(debug=True)

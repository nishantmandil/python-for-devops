import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)  # 1-second average
    print(f"CPU Usage: {cpu_percent}%")

    # Get Memory usage percentage
    mem_percent = psutil.virtual_memory().percent
    print(f"Memory Usage: {mem_percent}%")
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or memory utilization detected!"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)
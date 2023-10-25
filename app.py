from flask import Flask, render_template, request, redirect, url_for
import redis
import time

app = Flask(__name__)
redis_db = redis.StrictRedis(host='redis', port = 6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_data():
    data = request.form.get('data')

    # Simulate some data processing (eg: storing data after a delay)
    time.sleep(2)
    result = f"Processed Data: {data}"

    # Store the processed data in Redis
    redis_db.set('processed_data', result)

    return redirect(url_for('result'))


@app.route('/result')
def result():
    processed_data = redis_db.get('processed_data')
    if processed_data:
        return render_template('result.html', result=processed_data.decode('utf-8'))
    return 'No processed data found.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

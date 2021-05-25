from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/cyberpunktrip')
def cyberpunktrip():
    return render_template('cyberpunktrip.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')

import flask from Flask, render_template, request
import os

app = Flask(__name__)
@app.route('/')
def index():
return render_template('index.html')

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__:
  app.run(host='0.0.0.0', port=port, debug=True)

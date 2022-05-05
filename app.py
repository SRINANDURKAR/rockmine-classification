from flask import Flask, request, jsonify
import pickle
import sklearn
model = pickle.load(open('model_pickle','rb'))
print('Model is loaded')

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True)

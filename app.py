from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sklearn.datasets import load_iris

app = Flask(__name__)

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Load the trained models
model = joblib.load('models/model.joblib')
model_rf = joblib.load('models/model_rf.joblib')
model_knn = joblib.load('models/model_knn.joblib')

# Display model information
model_accuracy = 0.95  # Replace with the actual accuracy

@app.route('/')
def home():
    return render_template('index.html', accuracy=model_accuracy)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    model_name = data['model']
    selected_model = None

    if model_name == 'default':
        selected_model = model
    elif model_name == 'random_forest':
        selected_model = model_rf
    elif model_name == 'knn':
        selected_model = model_knn

    if selected_model is None:
        return jsonify({'error': 'Invalid model selection'})

    features = np.array(data['features']).reshape(1, -1)
    prediction = selected_model.predict(features)[0]

    return jsonify({'prediction': int(prediction)})  # Convert prediction to int

@app.route('/visualization')
def visualization():
    plt.figure(figsize=(8, 6))
    # Create a scatter plot of sepal length vs. sepal width
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Sepal Length vs. Sepal Width')

    # Convert the plot to base64 image for embedding in HTML
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    img_base64 = base64.b64encode(img_stream.read()).decode('utf-8')
    plt.close()

    return render_template('visualization.html', plot_img=img_base64)

if __name__ == '__main__':
    app.run(debug=True)

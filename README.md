# Flask Machine Learning Web App

This is a simple web application built with Flask that allows users to make predictions using trained machine learning models and visualize data using a scatter plot.

## Project Structure

The project is organized as follows:

project_folder/
│
├── app.py
│
├── models/
│ ├── model.joblib
│ ├── model_rf.joblib
│ └── model_knn.joblib
│
├── templates/
│ ├── index.html
│ ├── visualization.html
│ └── layout.html
│
├── static/
│ ├── css/
│ │ └── style.css
│ │
│ ├── js/
│ │ └── predict.js
│ │
│ └── images/ (if needed)
│
└── train_model.py


## Features

- Predict using different machine learning models: Choose from the default model, Random Forest, and K-Nearest Neighbors.
- Data Visualization: View a scatter plot of sepal length vs. sepal width for the Iris dataset.

## Getting Started

1. Clone this repository: `git clone https://github.com/your-username/your-flask-ml-app.git`
2. Navigate to the project folder: `cd your-flask-ml-app`
3. Set up a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows PowerShell)
5. Install dependencies: `pip install -r requirements.txt`
6. Run the Flask app: `python app.py`

The app will be accessible at `http://localhost:5000/`.

## Usage

1. Open your web browser and navigate to `http://localhost:5000/`.
2. Enter values for sepal length, sepal width, petal length, and petal width.
3. Select a model from the dropdown menu (default, Random Forest, K-Nearest Neighbors).
4. Click the "Predict" button to see the predicted class.

To view the data visualization, click on the "View Data Visualization" link.

## Dependencies

- Flask
- scikit-learn
- joblib
- matplotlib
- jQuery (included via CDN in `layout.html`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

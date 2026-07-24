SQL Query Performance Prediction using Machine Learning
📌 Project Overview

The SQL Query Performance Prediction project is a Machine Learning web application that predicts whether an SQL query will perform Fast or Slow based on various query characteristics. The model is trained using a Decision Tree Classifier and deployed using Flask.

This project demonstrates the complete Machine Learning workflow, including data preprocessing, model training, evaluation, and deployment as a web application.

🚀 Features
Predict SQL query performance (Fast/Slow)
User-friendly Flask web interface
Decision Tree Machine Learning model
Real-time predictions
Clean and responsive UI
Easy to use
🛠 Tech Stack
Programming Language
Python
Machine Learning
Scikit-learn
Pandas
NumPy
Web Framework
Flask
Frontend
HTML
CSS
Bootstrap
Deployment
Flask Local Server
📂 Project Structure
SQL-Query-Performance-Prediction/
│
├── static/
│   ├── style.css
│
├── templates/
│   ├── index.html
│
├── sql_query_performance_prediction.ipynb
├── app.py
├── model.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
└── dataset.csv
📊 Input Features

The model predicts performance using the following features:

Feature	Description
Query Length	Length of SQL query
Number of Joins	Total JOIN operations
Number of WHERE Clauses	WHERE conditions used
Number of Subqueries	Number of nested queries
GROUP BY Used	Yes/No
ORDER BY Used	Yes/No
Index Used	Yes/No
Table Size	Small / Medium / Large
Estimated Rows	Expected rows scanned
Execution Memory (MB)	Estimated memory usage
🎯 Target Variable

Performance

Fast
Slow
⚙️ Machine Learning Workflow
Import Dataset
Data Cleaning
Handle Missing Values
Remove Duplicate Records
Encode Categorical Variables
Exploratory Data Analysis (EDA)
Split Dataset into Training & Testing
Train Decision Tree Classifier
Evaluate Model
Save Trained Model
Deploy using Flask
📈 Model Used

Decision Tree Classifier

Evaluation Metrics:

Accuracy Score
Confusion Matrix
Classification Report
▶️ Installation

Clone the repository

git clone https://github.com/yourusername/SQL-Query-Performance-Prediction.git

Move into the project folder

cd SQL-Query-Performance-Prediction

Install dependencies

pip install -r requirements.txt

Run the Flask application

python app.py

Open your browser and visit

http://127.0.0.1:5000/
📸 Application Preview
<img width="900" alt="SQL Query Performance Prediction" src="images/project_screenshot.png">

Replace the image path with your actual screenshot stored in the repository.

💡 Future Improvements
Support additional Machine Learning algorithms
Add Random Forest and XGBoost comparison
Display prediction probability
Store prediction history
Deploy on Render or Railway
Improve UI with charts and analytics
📚 Libraries Used
Flask
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Pickle
📌 Learning Outcomes
Data Preprocessing
Feature Engineering
Decision Tree Classification
Model Evaluation
Flask Web Development
Machine Learning Model Deployment
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a new branch
Commit your changes
Push the branch
Create a Pull Request
👩‍💻 Author

Mayuri Shete

B.Sc. Computer Science Graduate

Passionate about Machine Learning, Python, SQL, and Backend Development.

⭐ If you like this project

Give this repository a ⭐ Star and feel free to share your feedback!

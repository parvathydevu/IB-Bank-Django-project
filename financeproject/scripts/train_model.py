import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
data = pd.read_csv(r'data\loan_amount_prediction_dataset_v2.csv')

# Define features and target
X = data[['Age', 'Monthly_Income', 'Credit_Score', 'Loan_Tenure_Years', 'Existing_Loan_Amount', 'Num_of_Dependents']]
y = data['Loan_Amount']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
with open(r'scripts/trained_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

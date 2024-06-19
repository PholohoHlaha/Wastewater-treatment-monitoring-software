import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
import pickle  

data_path = './records.csv'

df = pd.read_csv(data_path)

# Spliting features and target variable
x = df.drop("disposal", axis=1)
y = df["disposal"]

# Preprocessing data 
scaler = StandardScaler()
x = scaler.fit_transform(x)

# Splitting the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#training the model
model_lr = LogisticRegression()
model_lr.fit(x_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model_lr, f)

print("Model training complete!")

# Make predictions
predict_lr = model_lr.predict(x_test)

# Calculate accuracy
accuracy_score_lr = accuracy_score(y_test, predict_lr)
print(f"Model accuracy: {accuracy_score_lr:.2f}")

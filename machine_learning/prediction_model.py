import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the data
df = pd.read_csv('training_data.csv', parse_dates=['timestamp'])

# Preprocess the data
df = df.dropna()  # Drop rows with missing values
df = pd.get_dummies(df, columns=['category'])  # One-hot encode categorical variables
scaler = StandardScaler()  # Scale the numerical features
df[['num_feature_1', 'num_feature_2']] = scaler.fit_transform(df[['num_feature_1', 'num_feature_2']])
df['new_feature'] = df['num_feature_1'] * df['num_feature_2']  # Create a new feature

# Select the features
X = df.drop(['temperature', 'timestamp'], axis=1)
y = df['temperature']
selector = SelectKBest(f_regression, k=5)
selector.fit(X, y)
X = selector.transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the models to try
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(random_state=42)
}

# Define the hyperparameters to search over
params = {
    'Linear Regression': {},
    'Random Forest': {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, None]
    }
}

# Train and evaluate the models
for name, model in models.items():
    grid = GridSearchCV(model, params[name], cv=5)
    grid.fit(X_train, y_train)
    model = grid.best_estimator_
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(name + ':')
    print('R2 score:', r2)
    print('Mean Absolute Error:', mae)
    print('Mean Squared Error:', mse)
    print('Selected features:', selector.get_support())
    print()

# Save the best model
joblib.dump(models['Random Forest'], 'temperature_model.pkl')

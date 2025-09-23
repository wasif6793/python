# Task 1: Implementing the mathematical formula for linear regression.

import numpy as np


# Generate Synthetic data
X = 2  * np.random.rand(100,1)
y = 4 + 3 * X + np.random.rand(100,1)

# Add bias term to feature matrix
X_b = np.c_[np.ones((100,1)),X]

# Initialize parameters
theta = np.random.rand(2,1)
learning_rate = 0.1
iteration = 1000


def predict(X, theta):
    return np.dot(X,theta)

# Task 2: Use gradient to optimise the model parameters

def grad_desc(X, y, theta, learning_rate, iteration):
    m = len(y)
    for _ in range(iteration):
        grad = (1/m) * np.dot(X.T, (np.dot(X, theta) - y))
        theta -= learning_rate * grad
    return theta

# Task 3: Calculate Evaluation metrics

def mean_sq_error(y_true, y_pred):
    return np.mean((y_true - y_pred) **2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res/ss_tot)

    #  Perform the gradient descent
theta_optim = grad_desc(X_b, y , theta, learning_rate, iteration)

#  Predictions and evaluations
y_pred = predict(X_b, theta_optim)
mse = mean_sq_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimized parameters (Theta): ", theta_optim)
print("MSE: ", mse)
print("R-Squared: ", r2)
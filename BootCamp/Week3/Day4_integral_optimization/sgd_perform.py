import numpy as np

# Generate Synthetic data
X = 2 * np.random.rand(100,1)
y = 4 + 3 * X + np.random.rand(100,1)

#add some bias term to X
X_b = np.c_[np.ones((100,1)),X]


# SGD Implementation
def sgdperform(X,y,theta, learning_rate,n_epocs):
    m = len(y)
    for n_epoch in range(n_epocs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X[random_index:random_index+ 1]
            yi = y[random_index:random_index + 1]
            gradients = 2 * xi.T @ (xi @ theta -yi)
            theta -= learning_rate * gradients

    return theta

# Initialising parameter
theta = np.random.rand(2,1)
learning_rate = 0.01
n_epochs = 50

# Perform SGD
theta_opt = sgdperform(X_b,y,theta,learning_rate,n_epochs)
print("Optimised: ",theta_opt)
import numpy as np


#  define the gradient descent function
def gradient_descent(x,y, theta, learning_rate, iterations):
    m = len(y)

    for _ in range(iterations):
        predictions = np.dot(x,theta)
        errors = predictions - y
        grad = (1/m) * np.dot(x.T,errors)
        theta -= learning_rate * grad
    return theta

#  sample data
x = np.array([[1,1],[1,2],[1,3]])
y = np.array([2,2.5,3.5])
theta = np.array([0.1,0.1])

learning_rate = 0.1
iteration  = 1000

# Perform gradient descent
optimized_theta = gradient_descent(x,y,theta,learning_rate,iteration)

print("Optimised theta: ",optimized_theta)


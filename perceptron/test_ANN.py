import numpy as np

# input data
input_vector = [0.4, 0.6, 0.1, 0.3]

# weight to be applied to input data
weigths = [0.4, 0.3, 0.6, 0.1]

threshold = 0.5

# define the activation function
# this will determine if the output is 1 or 0
def step(weighted_sum):
    if weighted_sum > threshold:
        return 1
    else:
        return 0

def perceptron():
    weighted_sum = 0
    # There are 2 ways to multiple the inputs by their weights
    # for x, w in zip(input_vector, weights):
    # weighted_sum += x * w
    weighted_sum = np.dot(input_vector, weigths)

    # weighted sum is total of inputs * weights e.g. 0.43
    return step(weighted_sum)

# main perceptron
result = perceptron()

print(f"The perceptron output is {str(result)}")

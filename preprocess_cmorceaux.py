# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:23:53 2019

@author: viniv
"""

""" Initialization of the training sets.
"""
import numpy as np
import pickle as pkl

# Number of points on which the value of the function is known.
N = 2000

def g(x: float):
    """ The piecewise continuous function that will be used to check
    the quality of the approximation.

    Arguments:
        x {float} -- Will be taken in [0, 1]

    Returns:
        int -- the digit of the first decimal of x.
    """
    return int(x * 10)

# Creation of the training sets
list_abscissa = np.linspace(0, 1, N)
data_g = [(x, g(x)) for x in list_abscissa]
np.random.shuffle(data_g)

# Spliting of the sets : 80% used for training, 10% for validation
# and 10% for testing
index_80pc = int(len(list_abscissa) * 0.8)
index_90pc = int(len(list_abscissa) * 0.9)
training_set_g, validation_set_g, test_set_g = (
    data_g[:index_80pc],
    data_g[index_80pc:index_90pc],
    data_g[index_90pc:],
)
# We save the sets
dictionary_g = {"train": training_set_g, "valid": validation_set_g, "test": test_set_g}
with open("data_g.pkl", "wb") as f:
    pkl.dump(dictionary_g, file)
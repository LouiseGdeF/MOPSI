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


def h(x: float):
    return(1)


# Creation of the training sets
list_abscissa = np.linspace(0, 1, N)
data_h = [(x, h(x)) for x in list_abscissa]
np.random.shuffle(data_h)

# Spliting of the sets : 80% used for training, 10% for validation
# and 10% for testing
index_80pc = int(len(list_abscissa) * 0.8)
index_90pc = int(len(list_abscissa) * 0.9)
training_set_h, validation_set_h, test_set_h = (
    data_h[:index_80pc],
    data_h[index_80pc:index_90pc],
    data_h[index_90pc:],
)
# We save the sets
dictionnary_h = {"train": training_set_h, "valid": validation_set_h, "test": test_set_h}
with open("data_h.pkl", "wb") as file:
    pkl.dump(dictionnary_h, file)
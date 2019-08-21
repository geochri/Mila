# -*- coding: utf-8 -*-
"""Layers that act as activation functions.
"""

# Import Necessary Modules
import tensorflow as tf
from tensorflow.keras.layers import Layer


class Mila(Layer):
    '''
    Mila Activation Function.
    .. math::
        Mila(x) = x * tanh(ln(1 + e^{\\beta + x})) = x * tanh(softplus(\\beta + x)
    Shape:
        - Input: Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.
        - Output: Same shape as the input.
    Arguments:
        - beta: scale to control the concavity of the global minima of the function (default = -0.25)
    References:
        -  https://github.com/digantamisra98/Mila
    '''

    def __init__(self, beta):
        super(Mila, self).__init__()
        self.beta = beta
    
    def call(self, inputs):
        return inputs * tf.math.tanh(tf.math.softplus(inputs + self.beta))
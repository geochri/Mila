# -*- coding: utf-8 -*-
"""Function Definition for Mila in Keras.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from keras.engine.base_layer import Layer
from keras import backend as K

class mila(Layer):
    """Mila Activation Function.
    It follows:
    `f(x) =  x*tanh(ln(1+exp(\\beta + x))) = x*tanh(softplus(\\beta + x))`.
    # Input shape
        Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.
    # Output shape
        Same shape as the input.
    # Arguments
        beta: scale to control the concavity of the global minima of the function (default = -0.25)
    # References
        - [Mila: Controlling Minima Concavity in Activation Function](
           https://github.com/digantamisra98/Mila)
    """

    def __init__(self, beta=-0.25, **kwargs):
        super(mila, self).__init__(**kwargs)
        self.supports_masking = True
        self.beta = K.cast_to_floatx(beta)

    def call(self, inputs):
        return inputs*K.tanh(K.softplus(inputs + self.beta))

    def get_config(self):
        config = {'beta': float(self.beta)}
        base_config = super(mila, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    def compute_output_shape(self, input_shape):
        return input_shape

'''
Script provides functional interface for Mila activation function.
'''

# import pytorch
import torch
import torch.nn.functional as F

def mila(input, beta=1.0):
    '''
    Applies the Mila function element-wise:
    Mila(x) = x * tanh(softplus(1 + β)) = x * tanh(ln(1 + exp(x+β)))

    See additional documentation for mila class.
    '''
    return input * torch.tanh(F.softplus(input+beta))

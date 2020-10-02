'''
Applies the Mila function element-wise:
Mila(x) = x * tanh(softplus(1 + β)) = x * tanh(ln(1 + exp(x+β)))
'''

# import pytorch
from torch import nn

# import activation functions
import Mila.Torch.functional as Func

class mila(nn.Module):
    '''
    Applies the Mila function element-wise:
    Mila(x) = x * tanh(softplus(1 + β)) = x * tanh(ln(1 + exp(x+β)))

    Shape:
        - Input: (N, *) where * means, any number of additional
          dimensions
        - Output: (N, *), same shape as the input

    Examples:
        >>> m = mila(beta=1.0)
        >>> input = torch.randn(2)
        >>> output = m(input)

    '''
    def __init__(self, beta=1.0):
        '''
        Init method.
        '''
        super().__init__()
        self.beta = beta

    def forward(self, input):
        '''
        Forward pass of the function.
        '''
        return Func.mila(input, self.beta)

[![HitCount](http://hits.dwyl.io/digantamisra98/Mila.svg)](http://hits.dwyl.io/digantamisra98/Mila)
[![Donate](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/digantamisra98/Mila/issues)
[![CircleCI](https://circleci.com/gh/digantamisra98/Mila.svg?style=svg)](https://circleci.com/gh/digantamisra98/Mila)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b8ed6f5451c14f57871154d460304dc5)](https://www.codacy.com/app/digantamisra98/Mila?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=digantamisra98/Mila&amp;utm_campaign=Badge_Grade)

# Mila

*Mila* is an uniparametric activation function inspired from the Mish Activation Function. The parameter β is used to control the concavity of the Global Minima of the Activation Function where β=0 is the baseline Mish Activation Function. Varying β in the negative scale reduces the concavity and vice versa. β is introduced to tackle gradient death scenarios due to the sharp global minima of Mish Activation Function. 

The mathematical function of Mila is shown as below:
<div style="text-align:center"><img src ="Observations/function.png"  width="450"/></div>

It's partial derivatives:
<div style="text-align:center"><img src ="Observations/dev1.png"  width="500"/></div>
<div style="text-align:center"><img src ="Observations/dev2.png"  width="260"/></div>

1<sup>st</sup> derivative of Mila when β=-0.25:
<div style="text-align:center"><img src ="Observations/dev3.png"  width="560"/></div>

Function and it's derivatives graphs for various values of β:
<div style="text-align:center"><img src ="Observations/All.png"  width="1000"/></div>

Contour Plot of Mila and it's 1<sup>st</sup> derivative:
<div style="text-align:center"><img src ="Observations/Contour.png"  width="700"/></div>

## Benchmarks:

### CIFAR-10:

#### ResNet v1:

##### ResNet-20:

|Activation Function| Top-1 Accuracy| Loss|
|---|---|---|
|Mish|91.81%|4.47284%|
|Swish-1|**91.95%**|**4.440651%**|
|ReLU|91.5%|4.94356%|
|β-Mish (β = 1.5)|91.75%|4.4894%|
|Mila (β = 1)|91.85%|4.5375%|
|Mila (β = -0.25)|91.9%|4.4655%|
|Mila (β = 1.5)|91.44%|4.8906%|
|Mila (β = 0.5)|91.48%|4.5398%|

<div style="text-align:center"><img src ="Observations/res20.png"  width="1000"/></div>

##### ResNet-32: 

|Activation Function| Top-1 Accuracy| Loss|
|---|---|---|
|Mish|92.29%|4.3543639%|
|ReLU|91.78%|4.51267568%|
|Swish-1|92.3%|4.31110565%|
|β-Mish (β = 1.5)|92.49%|4.49838%|
|Mila (β = 1)|92.38%|4.36164%|
|Mila (β = -0.25)|**92.47%**|**4.2691%**|
|Mila (β = 1.5)|92.33%|4.58325%|
|Mila (β = 0.5)|92.42%|4.39018%|

<div style="text-align:center"><img src ="Observations/res32v1_c10.png"  width="1000"/></div>

## Try it

Run the demo.py file to try out Mila in a simple network for Fashion MNIST classification.

- First clone the repository and navigate to the folder using the following command. 

> cd \path_to_Mila_directory

- Install dependencies

> pip install requirements.txt

- Run the Python demo script. 

> python3 demo.py --activation mila --model_initialization class

*Note: The demo script is initialized with Mila having a β to be -0.25. Change the β ('beta' variable) in the script to try other beta values*

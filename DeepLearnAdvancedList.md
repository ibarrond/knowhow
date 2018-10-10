The list of techniques to apply in Deep Learning keeps increasing everyday. Rediscovering older papers of discovering new ones provides us with a constant flow of modern techniques. To keep it simple, I'm saving a list of things to check out when seeking the best performance. Basically, this is a list of terms you should be familiar with. It is well known at the beginning, but it gets mysterious later on.

## On Layers
- __Dropout__: Switch of random neurons during training.
- __Batch Normalization__: Normalize input of a layer.
- __ReLU__: Rectified Linear Units, an activation function that avoids gradient explosion.
- __ELU/PReLU/lReLU__: Variants of ReLU, Exponential linear unit, parametrized ReLU and leaky ReLU.
- __No more One Hot Encoding__: [link](http://course.fast.ai/lessons/lesson4.html) Decompose categorical data into vectors instead of single numbers.

## On Architecture
- __Transfer Learning__: Take pretrained networks or parts of them as a base model for your training.
- __Neural Architecture Search__: Use ML to search for the best architecture for your Deep Learning task.

## On Learning Process
- __L1 & L2 Regularization__: keep your weights small in your cost function.
- __AdamW__: Adam weight Decay [link](http://www.fast.ai/2018/07/02/adam-weight-decay/), better than Adam optimizer.
- __Gradient Clipping__: Do not allow the gradient to go beyond a certain threshold.
- __Differential Learning rates__: Use different learning rates for each set of layers (small for first layers, bigger for last). 
- __Cyclical Learning Rates__: [link](https://arxiv.org/abs/1506.01186) Search for the perfect learning rate by applying an exponentially increasing rate and keeping minimum loss. 
- __Cosine annealing__: Gradual decrease of learning rate using cosine function.
- __SDG with restarts__: [link](https://arxiv.org/pdf/1608.03983.pdf) restart the learning rate every several epochs.

## On Training techniques:
- __Several Sizes__: Train first on small, then on bigger images/text/..., shown in Yolov3.
- __ Data Augmentation__: Create modified copies of your training data.
- __TTA__: test time augmentation, you run several modifications of an input (image?) over the network and average them as the output.

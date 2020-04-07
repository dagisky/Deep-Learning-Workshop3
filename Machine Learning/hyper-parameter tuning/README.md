# Machine Learning
## Doing XGBoost hyper-parameter tuning the smart way 
Here we introduce three general purpose discrete optimization algorithms aimed at search for the optimal hyper-param combination: grid-search, coordinate descent and genetic algorithms. we will focus on optimizing XGBoost hyper-parameters in our experiment However, pretty much all of what is discussed here applies to any other advanced ML algorithms.

Usually, the more flexible and powerful an algorithm is, the more design decisions and adjustable hyper-parameters it will have. These are parameters specified by “hand” to the algo and fixed throughout a training pass.

 In tree-based models, hyper-parameters include things like the maximum depth of the tree, the number of trees to grow, the number of variables to consider when building each tree, the minimum number of samples on a leaf, the fraction of observations used to build a tree, and a few others. For neural networks, the list includes the number of hidden layers, the size (and shape) of each layer, the choice of activation function, the drop-out rate and the L1/L2 regularization constants.

 ![hyper param eq](https://miro.medium.com/max/1084/1*WjmgwZBjiWfbUmgCAwPvMg.png)


#### Introducing the Hyper-Parameter Grid

One important thing to note about hyper-parameters is that, often, they take on discrete values, with notable exceptions being things like drop-out rates or regularization constants. Thus, for practical reasons and to avoid the complexities involved in doing hybrid continuous-discrete optimization, most approaches to hyper-parameter tuning start off by discretizing the ranges of all hyper-parameters in question. For example, for our XGBoost experiments below we will fine-tune five hyperparameters. The ranges of possible values that we will consider for each are as follows:

```sh
{"learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ] }
```

This discrete subspace of all possible hyper-parameters is called the hyper-parameter grid. In what follows, we will use the vector notation symbol h = [h0, h1, …, hp] to denote any such combination, that is, any point in the grid.

#### Exhaustive Grid Search (GS)
Exhaustive grid search (GS) is nothing other than the brute force approach that scans the whole grid of hyper-param combinations h in some order, computes the cross-validation loss for each one and finds the optimal h* in this manner. An interesting alternative is scanning the whole grid in a fully randomized way that is, according to a random permutation of the whole grid . With this type of search, it is likely that one encounters close-to-optimal regions of the hyper-param space early on

#### Coordinate descent (CD)
Coordinate descent (CD) is one of the simplest optimization algorithms. It’s an iterative algorithm, similar to gradient descent, but even simpler! The basic idea is that, at each iteration, only one of the coordinate directions of our search vector h is altered. To pick which one, we examine each coordinate direction turn and minimize the objective function by varying that coordinate and leaving all the other constant. Then we pick the direction that yields the most improvement.

### Genetic algorithm
Genetic algorithms (GAs) are a whole class of optimization algorithms of rather general applicability and are particularly well adapted for high-dimensional discrete search spaces. A genetic algorithm tries to mimic nature by simulating a population of feasible solutions to a(n optimization) problem as they evolve through several generations and survival of the fittest is enforced. 


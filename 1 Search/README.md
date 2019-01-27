# Search Algorithms

In this part of the course you will learn about different types of 
search algorithms, and will see their implementation in python. 

Given a model of the world, and the possible action space we can take, 
the search algorithm is used to find a path to the goal state. The model 
of the world includes every last detail of the environment. We take a 
subset of that to search over for computational efficiency. We only keep 
the information that is required for the search. A Search State keeps 
only the details needed for planning. The more simplified your search 
problem is, the easier is it to search over it, but there is a risk of 
over simplification when the search would not be good enough.

## A search problem consists of -
- State space
- Start state
- Successor Function
- A goal test

The solution to a search problem is a sequence of actions(a Plan) 
which transforms the start state to the goal state.
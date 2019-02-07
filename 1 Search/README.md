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

A **Search State** can simply be thought of as an abstraction of the 
world. It keeps just the data required for the search.

## A Search State consists of -
- State space
- Start state
- Successor Function
- A goal test

The solution to a search problem is a sequence of actions(a Plan) 
which transforms the start state to the goal state.

Search operate over a model of the world -
- The agent does not actually try all the plans out in the real world. Planning 
is all done in Simulation.
- Your search is only as good as your model of the world.

So, selecting a good abstraction of the world to search over is very important.

## State Space Graph
It is a mathematical representation of a search problem. In a search 
graph each node(state) only occurs once. We can rarely build this full 
graph in memory, but it is a useful idea. We usually build on demand 
to save computation.

## Search Tree
This can be thought of as an expanded version of a State space Graph. 
Start state is the root node and the children are the successors. Nodes 
show states but actually correspond plans that achieve those states. 
There are a lot of repeated structure in a search tree. When you have 
cycles in a State Space Graph the corresponding search tree can be 
infinite. But still this is a very useful idea for search.

## Tree Search
- Expand potential plans.
- Maintain a Fringe of partial plans under consideration.
- Try to expand as few tree nodes as possible

##### Some of the important terms to look into -
- Fringe
- Expansion
- Exploration Strategy

A Fringe can be thought of as a priority queue kind of data structure 
that stores all the nodes that could be expanded next. Each search 
algorithm has a different way of selecting the next node(strategy) to expand from 
the fringe and rest of the algorithm remains the same. We will try to 
find the goal state with least expansion of tree nodes.

#### General Tree search algorithm
This is a basic prototype of how a general tree search algorithm works.
```html
function Tree_Search(problem, Strategy) {returns a solution or failure}
    initialize search tree using initial state of problem
    loop do:
        if there are no candidates for expansion then return failure
        else choose a  leaf node for expansion according to the stratergy
        
        if the node contains goal state then return the corresponding solution
        else expand the node and add all the resulting nodes to the search tree
    end
```

Search algorithms can be categorized into two main types - 
- Uninformed Search
- Informed Search

## Uninformed Search
This is the kind of search when we do not know anything about the goal state or 
we do not make any assumptions about where the goal state could be and we search 
in every possible direction for the goal state. These algorithms waste a lot of time 
searching in the wrong direction but this is a good way to start with learning 
search algorithms. So lets get started with the search algorithms.
 
#### Depth First Search
As the name suggests, the expansion strategy of this algorithm is depth first. 
Depth is given higher priority. The tree nodes deeper are selected from the fringe
to be expanded first and if two nodes have the same depth the one that came in 
first will be given higher priority. It may seem a little complicated now but once 
you go through the code and implement it yourself, you will get a clear idea of 
how it works. This algorithm is not guaranteed to find an optimal solution.

Some implementation details - 
- Strategy : Expand deepest node first.
- Implementing : Fringe is a STACK. As a stack follows LIFO(Last in First out) 
strategy, it is prefect for this algorithm.

#### Breadth First Search
This algorithm gives breadth higher priority. The shallower nodes are expanded 
first. The shallow first strategy helps this algorithm find the optimal solution, 
but it can take up a lot of space in memory as the fringe can be really large for 
this in the worst case. 

Some implementation details - 
- Strategy : Expand the shallowest node first.
- Implementing : Fringe is a QUEUE. As a Queue follows FIFO(First in First out) 
strategy, it is prefect for this algorithm.

#### Uniform-Cost Search
When each of the state transitions or paths have different weights the Uniform cost 
search is a really useful algorithm to use. This algorithms expansion strategy is 
to expand the cheapest node first. We use a priority queue in this case where the 
priority is given by the cost of the path. The cheapest node on the fringe is the 
one that is expanded first.

Some implementation details - 
- Strategy : Expand the cheapest node first.
- Implementing : Fringe is a PRIORITY QUEUE. Where priority is given by the cost 
of the path to that node.


## Informed Search
All the previous algorithms worked in a similar manner, with a small change in the
data structure for the fringe being used(stack, queue or priority queue). They all 
followed the same general tree search algorithm, and searched in every direction 
for the goal. These uninformed search algorithms are useful when we do not know 
anything about the goal.

When we have some knowledge about the goal, we can use that to reduce the required 
computation for the search. If we know that the goal is towards the east, then we 
should give east a higher priority while searching, so as to reduce the number of 
steps taken towards the west, ie. in the opposite direction.   

#### Search Heuristics
A heuristic is nothing but a mapping from states to numbers. It is a function that
estimates how close a state is to a goal. A heuristic is specially designed for a 
the problem in hand. A good example for this can be the path finding problem we 
saw in uninformed search. We know the coordinated of the goal state so our heuristic 
in that case could be the 
- [Euclidean_distance](https://en.wikipedia.org/wiki/Euclidean_distance) 
- [Manhattan distance](https://en.wiktionary.org/wiki/Manhattan_distance)

With every step we are planning to take we could feed it to our heuristic function
and that would give us a numerical distance to goal state if we take that step. 
We can use this to give the states that take us close to the goal higher priority.
Using this heuristic will reduce the computation required to find the goal as we 
dont search much in the wrong direction, that takes us away from the goal. We only
move in the direction of the goal.

#### Greedy Search (Best First Strategy)
In this algorithm we use just the heuristic value to find the path to the goal. 
We expand the node that seems closest to the goal according to the heuristic. 
There is a problem if we do this. What if there are barriers in the way? This 
algorithm would not find the optimal path to the goal is there are obstacles in
the path to the goal. It would be like a badly guided Depth first search. 

#### A* Search 
###### (Uniform Cost Search + Greedy Search = A* Search)
We add a controller of path cost, that controls the greedy search from choosing 
a non optimal goal path. The greedy search gives direction to the Uniform cost 
search algorithm. 

We use two function in this -
- g(state) -- Cumulative cost Function (UCS)
- h(state) -- Heuristic Function (Greedy)

A* algorithm orders it search by the sum
- f(state) = g(state) + h(state)

A* search gives us the optimal path given the condition that the heuristic function
used is-
- Admissible and
- Consistent

#### Admissible Heuristic
Inadmissible heuristics (also known as pessimistic) break optimality by trapping 
good plans on the fringe. Admissible(optimistic) heuristics slow down bad plans but
never overweight true costs. 

A heuristic H is admissible(optimistic) if :

``` 0 <= H(state) <= H*(state) ```

What this formula says is the Heuristic cost to the goal state, ie. predicted 
cost from that state to goal, should not be greater than the true cost to the 
nearest goal state. 

Coming up with a admissible heuristic is most of what is involved in using A* in
practice. A* search expands mainly towards the goal, but does hedge its bets 
to ensure optimality. 

#### Consistency of Heuristics
Main idea: ```estimated_heuristic_cost <= actual_cost(for each arc)```
- Admissibility : ```heuristic_cost <= actual_cost(to goal)```
- Consistency : ```heuristic_arc_cost <= actual_cost(for arc)```

example A and C are two intermediate states, which are not goal state. 
H is the heuristic being used. For H to be consistent it should satisfy the following
condition for each of its arcs : 

```(H(A) - H(C)) <= cost(A to C)```

F values along a path never decreases:
```H(A) <= [ cost(A to C) + H(C) ]```

If this condition is satisfied be a heuristic, then A* search is guaranteed to be 
optimal. In general, most of the admissible heuristics tend to be consistent, especially
if from a relaxed problem.

#### Creating a Heuristic
Most of the work in solving hard search problems optimally is in coming up with 
an Admissible Heuristic. Often admissible heuristics are solution to relaxed 
problems where new actions are available(an example of a relaxed problem can be
for finding the path between two points you can draw a straight line between 
the two points, that is the relaxed solution to the problem, without considering
the barriers and the action space, the shortest distance you can find). Inadmissible
heuristics are often useful too, but optimality is not guaranteed. 

We should not make a heuristic too complicated too. The main aim of introducing 
a heuristic is to reduce the computation required for finding the goal, but if 
we increase the computation per state too much that would reduce the unnecessary 
steps explored but that would be very costly per state. With A*, we trade off 
between quality of estimate and work per node.

#### Some areas where A* search is used:
- Pathing/Routing problems
- Resource Planning problem
- Robot motion planning
- Language analysis
- Machine Translation
- Speech Recognition


## Graph Search
#### Idea : Never expand a state twice
#### Implementation :
- Tree search + set of expanded nodes(closed set)

Expand the search tree node by node, but before expanding the node check to make 
sure it has never been expanded before. If not new skip the node, if new then add
it to the closed set and expand the node. Store the closed set as a set(), that
does not allow duplicate values in it, not a list. 

This addition of the closed set prevents the algorithm from being stuck in cycles.


# Artificial Intelligence

## AI_Algorithms Repo

One stop for learning most of the important algorithms 
for building your Artificial Intelligence Application.
This repository contains coded examples of all the 
algorithms that will help you learn not just the theory of 
how the algotithm works but also the implementation of 
it in python programming language.

## What is AI?
Artificial Intelligence is about making systems that 
**ACT RATIONALLY**. We build Agents that perceive the 
environment through sensors and process the information to 
act rationally.

Until the 1970's humans used to try to mimic the human 
brain, but did not turn out to be much successful. The 
lessons learnt from the brain were -
> Memory and Simulation are key to decision making.

## What is an Agent?
An agent is an entity that perceives and acts accordingly. 
A rational agent selects actions that maximize its expected 
utility. Characteristics of the percepts, environment and 
action space dictate techniques for selecting rational actions.

There are two types of agents - 
- Reflex agents
    
    >Reflex agents are Agents that dont plan at all. They 
    just take a decision about their next action based on 
    their current state. They do not consider the future 
    consequences of their actions and so are not Rational. 
    They just consider how the world is now and do not have 
    a model of the world.

- Planning agents

    >Planning agents ask the question "What if?", and this is 
    what makes its decision intelligent. Its decisions are 
    based on hypothesized consequences of actions. These 
    agents consider how the world would be, if the take this 
    action. They need a model of how the environment/world 
    would evolve in response to their actions. There are two 
    types of these planning agents -
    
    - Complete planning agents
        
        >These agents compute their complete path before 
        starting execution. These agents can take up a 
        long time before making their first move, as they 
        look through all possible states of the world. The 
        path these agent find is the optimal one, but the 
        process of planning can be slow.
    
    - Re-planning agents
    
        >These agents plan on each step they take. These 
        are faster and are guaranteed to find the goal 
        but the solution may not be optimal.



There are a lot of new terms that were introduced in the 
previous definition. I will go through all of them, and as
we go on and start implementing the algorithms, you will
understand these concepts even better.

#### Environment 
Environment is nothing but the world for which the agent was
created. An example for this can be, the game environment. 
Imagine you were building an agent to play the game of pacman. 
The environment includes of everything in the pacman world, 
the dots, walls, ghosts, power-ups and the pacman itself.

#### Action space
Action space is the possible set of actions the agent can take.
Like in the previous example of pacman, the action space was 
(UP, DOWN, LEFT, RIGHT). The agent will be the pacman itself 
and the action space is the possible actions the agent can 
select.

### State Space
Like action space, state space is the possible set of states the world
can be in. With the same example of pacman, each position of the agent 
could correspond to a different game state and a set of all possible 
such states is what corresponds as State Space. Some special kind of 
states are goal state, start state and current stat.

## Conclusion
Hope this gives you a good introduction to the world of AI.
You will get a better idea these concepts as the course progresses.
Hope you have a great time doing this course and I am looking 
forward to see the intelligent application that you build 
learning the basics from this course. 
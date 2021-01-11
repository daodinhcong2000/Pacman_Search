# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from util import Stack

    stackXY = Stack()

    visited = []
    path = []

    if problem.isGoalState(problem.getStartState()):
        return []

    stackXY.push((problem.getStartState(),[]))

    while(True):
        if stackXY.isEmpty():
            return []

        xy,path = stackXY.pop() 
        visited.append(xy)
        if problem.isGoalState(xy):
            return path

        successors = problem.getSuccessors(xy)

        if successors:
            for item in successors:
                if item[0] not in visited:
                    newPath = path + [item[1]]
                    stackXY.push((item[0],newPath))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    queueXY = Queue()

    visited = []
    path = [] 

    if problem.isGoalState(problem.getStartState()):
        return []

    queueXY.push((problem.getStartState(),[]))

    while(True):

        if queueXY.isEmpty():
            return []

        xy,path = queueXY.pop()
        visited.append(xy)

        if problem.isGoalState(xy):
            return path

        successors = problem.getSuccessors(xy)

        if successors:
            for item in successors:
                if item[0] not in visited and item[0] not in (state[0] for state in queueXY.list):
                    newPath = path + [item[1]]
                    queueXY.push((item[0],newPath))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue

    queueXY = PriorityQueue()

    visited = []
    path = []

    if problem.isGoalState(problem.getStartState()):
        return []
    queueXY.push((problem.getStartState(),[]),0)

    while(True):
        if queueXY.isEmpty():
            return []
        xy,path = queueXY.pop()
        visited.append(xy)
        if problem.isGoalState(xy):
            return path
        successors = problem.getSuccessors(xy)
        if successors:
            for item in successors:
                if item[0] not in visited and (item[0] not in (state[2][0] for state in queueXY.heap)):
                    newPath = path + [item[1]]
                    pri = problem.getCostOfActions(newPath)

                    queueXY.push((item[0],newPath),pri)

                elif item[0] not in visited and (item[0] in (state[2][0] for state in queueXY.heap)):
                    for state in queueXY.heap:
                        if state[2][0] == item[0]:
                            oldPri = problem.getCostOfActions(state[2][1])

                    newPri = problem.getCostOfActions(path + [item[1]])

                    if oldPri > newPri:
                        newPath = path + [item[1]]
                        queueXY.update((item[0],newPath),newPri)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

from util import PriorityQueue
class MyPriorityQueueWithFunction(PriorityQueue):
    def  __init__(self, problem, priorityFunction):
        self.priorityFunction = priorityFunction
        PriorityQueue.__init__(self)
        self.problem = problem
    def push(self, item, heuristic):
        PriorityQueue.push(self, item, self.priorityFunction(self.problem,item,heuristic))

def f(problem,state,heuristic):

    return problem.getCostOfActions(state[1]) + heuristic(state[0],problem)

def aStarSearch(problem, heuristic=nullHeuristic):
    "*** YOUR CODE HERE ***"
    queueXY = MyPriorityQueueWithFunction(problem,f)

    path = []
    visited = []

    if problem.isGoalState(problem.getStartState()):
        return []

    element = (problem.getStartState(),[])

    queueXY.push(element,heuristic)

    while(True):
        if queueXY.isEmpty():
            return []

        xy,path = queueXY.pop()

        if xy in visited:
            continue

        visited.append(xy)

        if problem.isGoalState(xy):
            return path

        successors = problem.getSuccessors(xy)

        if successors:
            for item in successors:
                if item[0] not in visited:
                    newPath = path + [item[1]]
                    element = (item[0],newPath)
                    queueXY.push(element,heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# Instructions

## Command Line Operation

To run the program using the command line, follow these steps:

1. Navigate to the folder containing the `search.exe` file and the `input.txt` file.
2. Open the Command Prompt.
3. Execute the command: `search <Input_File> <Method>`, where `<Input_File>` is the name of the input file with the required format, and `<Method>` is the name of the search algorithm to execute.

## GUI

There are two methods for accessing the Graphical User Interface (GUI) of the application:

1. Open GUI without an input file:
   - Type `search` in the terminal to open the GUI without any input file.
   - Inside the GUI, you can create a maze by right-clicking on the grid to set the initial location of the robot, goals, and walls.
   - Use the available buttons to interact with the GUI, such as removing cells, clearing paths and walls, adjusting grid size, and more.
   - Click the "Start" button or press the "spacebar" on the keyboard to initiate the search algorithm.

2. Open GUI with an input file:
   - Specify the input file's name as the only parameter of the command line: `search <Input_File>`.
   - The GUI will read the input file and generate a visualization of it.
   - Interact with the GUI using the provided buttons and functionalities.

For a more detailed explanation of using the GUI, refer to the figures and descriptions provided in the document.

# Search Algorithm detail
The readme describes six search algorithms implemented in the application:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Greedy Best First Search (GBFS)
- A-Star Search
- Bidirectional Search
- Bidirectional A-Star Search

For each algorithm, the report explains its mechanism, time and space complexity, and optimality. It also includes pseudocode for each algorithm's implementation.

## Implementation

The report includes the pseudocode for implementing each of the six search algorithms: BFS, DFS, GBFS, A-Star, Bidirectional Search, and Bidirectional A-Star. It explains the key differences and optimizations for each algorithm.

[103178955.pdf](https://github.com/emyeucanha5/COS30019-Robot-Navigation/files/11828448/103178955.pdf)

Please refer to the complete report for more detailed information on each algorithm's implementation and the Robot Navigation application.

## Specific feature

### Bidirectional Search

The Bidirectional Search algorithm starts by initializing a queue `S` and pushing the start node to the queue with a Boolean value of True to indicate that it belongs to the start tree. The algorithm also initializes the visited array for the start node with a tuple value of `(True, True)` to indicate that it has been visited by the start tree. Similarly, the algorithm pushes all goal nodes to the queue with a Boolean value of False to indicate that they belong to the goal tree and initializes their visited array with a tuple value of `(True, False)` to indicate that they have been visited by the goal tree. For each iteration, if an adjacent node has not been visited by the same tree, the algorithm pushes it to the queue with the same Boolean value as the current node and updates its visited array accordingly. If an adjacent node has been visited by the other tree, the algorithm returns the path by using the path information stored in the path array.

### Bidirectional A-Star Search

This algorithm utilizes two priority queues, `S_F`, and `S_B` to keep track of the frontier nodes in the forward and backward searches, respectively. Additionally, it maintains two arrays, `explore_F` and `explore_B`, to store the nodes that have been explored by the forward and backward searches, respectively. The mu (μ) value is also set to infinity initially, which represents the shortest path found so far by the algorithm. During each iteration, the algorithm pops a node from both priority queues and explores its adjacent nodes. If the popped node called v from one direction of search has been explored by the other direction of search, the mu (μ) value is updated as the minimum of its current value and the sum of its cost in both directions of search.

μ = min(μ, cost_b(v) + cost_f(v))

The algorithm terminates either when the mu value cannot be lowered anymore or when the maximum f_value of the nodes in both priority queues is smaller than or equal to the current mu value. The reason for using the maximum of the two smallest f(n) values is to ensure that only nodes that are near the intersection point of the two search trees are considered for finding the shortest path. It will terminate when:

μ ≤ max(PQ_f.top(), PQ_b.top())

## Visualization
![image](https://github.com/emyeucanha5/COS30019-Robot-Navigation/assets/57170354/e6b74cee-d4bf-4c01-b141-64de8dc0feb0)

![image](https://github.com/emyeucanha5/COS30019-Robot-Navigation/assets/57170354/9bbbd23f-f385-4d80-bfe3-e550411f9ad7)

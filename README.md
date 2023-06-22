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

# Introduction

## Objective

This report aims to provide a comprehensive overview of the Robot Navigation problem and the implementation of six search strategies. It also includes instructions on using the GUI.

## Problem Introduction

The Robot Navigation problem involves a grid with empty cells and wall cells. The robot's goal is to find a path from its initial location to the nearest goal with the smallest path cost. The robot can only move up, left, down, and right. The problem provides the initial coordinates of the robot and multiple goal coordinates. The search strategies implemented in this application aim to solve this problem.

## Glossary

The glossary provides definitions for key terms used in the report, such as graph, priority queue, heuristic function, tree, and frontier.

## Search Algorithms

The report describes six search algorithms implemented in the application:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Greedy Best First Search (GBFS)
- A-Star Search
- Bidirectional Search
- Bidirectional A-Star Search

For each algorithm, the report explains its mechanism, time and space complexity, and optimality. It also includes pseudocode for each algorithm's implementation.

## Comparison

The report provides a comparison between the six search algorithms based on the number of nodes and the time required for execution. The comparison is conducted using five test cases with different grid sizes.

## Implementation

The report includes the pseudocode for implementing each of the six search algorithms: BFS, DFS, GBFS, A-Star, Bidirectional Search, and Bidirectional A-Star. It explains the key differences and optimizations for each algorithm.

Please refer to the complete report for more detailed information on each algorithm's implementation and the Robot Navigation application.

## Visualization

![image](https://github.com/emyeucanha5/COS30019-Robot-Navigation/assets/57170354/72be0915-339e-47db-848b-13657c3eb534)

**Note:** The figures mentioned in this Readme are not included. Please refer to the original document for the complete content.

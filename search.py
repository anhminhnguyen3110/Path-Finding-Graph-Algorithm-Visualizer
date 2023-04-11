import sys
from maze import Maze
from robot import Robot
from search_function import execute_search
def read_file_and_create_mize(file_name):
    try:
        file = open(file_name, "r")
    except IOError:
        print("File not found")
        return 1
    
    inputs = file.read().splitlines()
    for index,input in enumerate(inputs):
        if(index==0):
          str = input[1:-1].split(",")
          if(str[1][-1] == ")" or str[1][-1] == "]"):
              str[1] = str[1][:-1]
          maze.set_size(int(str[1]), int(str[0]))
          
        if(index==1):      
          str = input[1:-1].split(",")
          if(str[1][-1] == ")" or str[1][-1] == "]"):
              str[1] = str[1][:-1]
          robot.set_location(int(str[1]), int(str[0]))
          
        if(index == 2):
            goals_in_string = input[1:-1].split(") | (",)
            for goal_in_string in goals_in_string:
                goal = goal_in_string.split(",")
                if(goal[1][-1] == ")" or goal[1][-1] == "]"):
                    goal[1] = goal[1][:-1]
                maze.set_goal(int(goal[0]), int(goal[1]))
        if(index > 2):
            strs = input[1:-1].split(",")
            block_input = []
            for index, str in enumerate(strs):
                if(str[-1] == ")" or str[-1] == "]"):
                    str = str[:-1]
                block_input.append(int(str))
                # print(str, end = " ")
            # print()
            maze.set_maze_block(block_input[0], block_input[1], block_input[2], block_input[3])
    file.close()
    # maze.__str__()
    return 0
def main():
    file_name = sys.argv[1]
    method = sys.argv[2]
    read_file_and_create_mize(file_name)
    answer = execute_search(robot, maze, method)
    print(file_name, ' ',method, ' ',answer.split('; ').__len__(), answer)
    print()
robot = Robot(0,0)
maze = Maze(0,0)    
main()

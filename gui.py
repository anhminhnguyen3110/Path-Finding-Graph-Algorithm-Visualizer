"""This module contains the GUI for the project."""
import pygame
from button_container import ButtonContainer
from constants import DEFAULT_COLS, DEFAULT_ROWS, GUI_FONT, INSTRUCTIONS, WHITE, WIDTH, WIN
from maze import Maze
from maze_gui import MazeGui
from robot import Robot
from search_function import execute_search
from text_box import TextBox

pygame.display.set_caption("RoboNavigation")
textBox = TextBox("", "", "", 230, 100, (WIDTH + 30, 15), WIN, GUI_FONT)

def execute_search_gui(
    draw_func, maze_gui: MazeGui
):
    def wait(wait_variable: int = maze_gui.wait_variable):
        pygame.time.wait(wait_variable)

    def check_forbid_event():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
    #execute search
    (ans, number_of_steps) = execute_search(maze_gui.robot, maze_gui.maze,
                                            maze_gui.search_method, (draw_func, maze_gui.grid, wait, check_forbid_event))
    print(ans)
    #print path
    instruction_list = ans.split("; ")
    trace_col, trace_row = maze_gui.robot.col, maze_gui.robot.row
    while instruction_list.__len__() - 1:
        instruction = INSTRUCTIONS[instruction_list.pop(0)]
        trace_row += instruction[0]
        trace_col += instruction[1]
        maze_gui.grid[trace_col][trace_row].assign_path()
        draw_func()
        wait(20)
    textBox.update_third_line(str(number_of_steps))
    
def execute_command(
    command: str,
    maze_gui: MazeGui,
    draw_func,
) -> None:
    maze_gui.clear_path()
    match command:
        case "Start":
            if(maze_gui.search_method != '' and maze_gui.start and len(maze_gui.end)):
                execute_search_gui(draw_func, maze_gui)
        case "Clear Path":
            maze_gui.clear_path()
        case "Clear Wall":
            maze_gui.clear_wall()
        case "Increase No Goal":
            maze_gui.increase_no_of_goals()
        case "Decrease No Goal":
            maze_gui.decrease_no_of_goals()
        case "Increase Grid Size":
            maze_gui.increase_grid_size()
        case "Decrease Grid Size":
            maze_gui.decrease_grid_size()
        case _:
            return
    return

def draw(win, maze_gui: MazeGui, button_container: ButtonContainer):
    win.fill(WHITE)
    maze_gui.draw_grid(win)
    maze_gui.draw_visual_grid(win)
    button_container.draw()
    textBox.draw()
    pygame.display.update()

def main(win, width):
    # initialize gui for maze
    maze_gui = MazeGui(Maze(10, 10), Robot(-1, -1))
    maze_gui.assign_grid(DEFAULT_ROWS, DEFAULT_COLS, width)
    textBox.update(str(DEFAULT_ROWS), str(DEFAULT_COLS), str(0))

    # initialize gui for buttons
    button_container = ButtonContainer()
    
    # to keep the gui alive
    run = True
    start_algorithm = False

    while run:
        draw(win, maze_gui, button_container)
        textBox.update_first_line(str(maze_gui.rows))
        textBox.update_second_line(str(maze_gui.number_of_goals))
        maze_gui.check_wait_time()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            if pygame.mouse.get_pressed()[0]:  # left pointer
                # if the algorithm is running, then we cannot interact with the grid or buttons
                if start_algorithm:
                    continue
                pos = pygame.mouse.get_pos()

                if button_container.pointer_in_search_button(pos):
                    result = button_container.get_clicked_search_buttons(
                        pos, maze_gui
                    )
                    if result is not None:
                        maze_gui.search_method = result
                    continue
                
                if button_container.pointer_in_functional_button(pos):
                    start_algorithm = True
                    command = button_container.get_clicked_pos_of_functional_buttons(pos)
                    execute_command(command, maze_gui, lambda: draw(win, maze_gui, button_container))
                    start_algorithm = False
                    
                if (maze_gui.pointer_in_grid(pos)):
                    square = maze_gui.get_clicked_pos_of_grid(pos)
                    if not square:
                        continue
                    else:
                        maze_gui.execute_grid_left_click(square)

            elif pygame.mouse.get_pressed()[2]:  # right pointer
                if start_algorithm:
                    continue
                pos = pygame.mouse.get_pos()
                if (maze_gui.pointer_in_grid(pos)):
                    square = maze_gui.get_clicked_pos_of_grid(pos)
                    if not square:
                        continue
                    else:
                        maze_gui.execute_grid_right_click(square)

            if event.type == pygame.KEYDOWN:
                if start_algorithm:
                    continue
                if event.key == pygame.K_SPACE:
                    start_algorithm = True
                    maze_gui.clear_path()
                    if(maze_gui.start and len(maze_gui.end)):
                        execute_search_gui(lambda: draw(win, maze_gui, button_container), maze_gui)
                    start_algorithm = False
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    maze_gui.clear_all()
    pygame.quit()

main(WIN, WIDTH)

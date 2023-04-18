"""This module contains the GUI for the project."""
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hide welcome prompt from pygame
import pygame
from button_container import ButtonContainer
from constants import DEFAULT_COLS, DEFAULT_ROWS, GUI_FONT, INSTRUCTIONS, WHITE, WIDTH, WIN
from maze import Maze
from maze_gui import MazeGui
from robot import Robot
from search_function import execute_search
from text_box import TextBox

pygame.display.set_caption("RoboNavigation")
textBox = TextBox("", "", "", 215, 100, (WIDTH + 62, 15), WIN, GUI_FONT)


def execute_search_gui(draw_func, maze_gui: MazeGui, file_name: str = ""):
    def wait(wait_variable: int = maze_gui.wait_variable):
        pygame.time.wait(wait_variable)

    def check_forbid_event():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # execute search
    (ans, number_of_steps) = execute_search(
        maze_gui.robot, maze_gui.maze, maze_gui.search_method, (draw_func, maze_gui.grid, wait, check_forbid_event)
    )
    print(file_name, maze_gui.search_method, number_of_steps)
    print(ans)
    # print path
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
    file_name: str,
) -> None:
    maze_gui.clear_path()
    match command:
        case "Start":
            if maze_gui.search_method != "" and maze_gui.start and len(maze_gui.end):
                execute_search_gui(draw_func, maze_gui, file_name)
        case "Clear Path":
            maze_gui.clear_path()
        case "Clear Wall":
            maze_gui.clear_wall()
        case "Increase Goal":
            maze_gui.increase_no_of_goals()
        case "Decrease Goal":
            maze_gui.decrease_no_of_goals()
        case "Increase Column":
            maze_gui.increase_grid_size_col_size()
        case "Decrease Column":
            maze_gui.decrease_grid_size_col_size()
        case "Increase Row":
            maze_gui.increase_grid_size_row_size()
        case "Decrease Row":
            maze_gui.decrease_grid_size_row_size()
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


def gui(
    maze: Maze,
    robot: Robot,
    row_size: int = DEFAULT_ROWS,
    col_size: int = DEFAULT_COLS,
    width=WIDTH,
    is_call_independent=True,
    file_name="",
    search_method="BFS",
):
    win = WIN
    # initialize gui for maze
    maze_gui = MazeGui(Maze(DEFAULT_ROWS, DEFAULT_COLS), Robot(-1, -1), col_size, row_size, width)
    maze_gui.search_method = search_method

    # initialize gui for buttons
    button_container = ButtonContainer()
    button_container.turn_on_a_search_button(search_method)
    # to keep the gui alive
    run = True
    start_algorithm = False
    wait = 0
    if not is_call_independent:
        maze_gui.adapt_new_maze(maze, robot)

    textBox.update(str(row_size), str(col_size), str(0))

    while run:
        draw(win, maze_gui, button_container)
        textBox.update_first_line(str(maze_gui.rows), str(maze_gui.cols))
        textBox.update_second_line(str(maze_gui.number_of_goals))
        maze_gui.check_wait_time()
        if not wait and not is_call_independent:
            pygame.time.wait(300)
            execute_search_gui(lambda: draw(win, maze_gui, button_container), maze_gui, file_name)
            wait = 1
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
                    result = button_container.get_clicked_search_buttons(pos, maze_gui)
                    if result is not None:
                        maze_gui.search_method = result
                    continue

                if button_container.pointer_in_functional_button(pos):
                    start_algorithm = True
                    command = button_container.get_clicked_pos_of_functional_buttons(pos)
                    execute_command(command, maze_gui, lambda: draw(win, maze_gui, button_container), file_name)
                    start_algorithm = False

                if maze_gui.pointer_in_grid(pos):
                    square = maze_gui.get_clicked_pos_of_grid(pos)
                    if not square:
                        continue
                    else:
                        maze_gui.execute_grid_left_click(square)

            elif pygame.mouse.get_pressed()[2]:  # right pointer
                if start_algorithm:
                    continue
                pos = pygame.mouse.get_pos()
                if maze_gui.pointer_in_grid(pos):
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
                    if maze_gui.start and len(maze_gui.end):
                        execute_search_gui(lambda: draw(win, maze_gui, button_container), maze_gui)
                    start_algorithm = False
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    maze_gui.clear_all()
    pygame.quit()

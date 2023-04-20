from maze_gui import MazeGui
from constants import GREEN, GUI_FONT, RED, WIDTH, WIN
from button import Button


class ButtonContainer:
    def __init__(self) -> None:
        self.search_buttons = self.assign_search_methods()
        self.functional_buttons = self.assign_functional_button(self.search_buttons)

    def assign_search_methods(self):
        search_methods = [
            "BFS",
            "DFS",
            "GBFS",
            "ASTAR",
            "Bidirectional Search",
            "Bidirectional A*",
        ]
        buttons = []
        for i, search_method in enumerate(search_methods):
            buttons.append(Button(search_method, 220, 40, (WIDTH + 300, 60 + i * 70), WIN, GREEN, GUI_FONT))
        buttons[0].is_selected = True
        return buttons

    def turn_on_a_search_button(self, search_method: str):
        search_method = search_method.lower()
        if search_method == "cus1":
            search_method = "bidirectional search"
        elif search_method == "cus2":
            search_method = "bidirectional a*"
        elif search_method == "as":
            search_method = "astar"
        for button in self.search_buttons:
            if button.text.lower() == search_method.lower():
                button.is_selected = True
            else:
                button.is_selected = False

    def assign_functional_button(self, search_methods):
        top_buttons = ["Start"]
        second_buttons = ["Clear Path", "Clear Wall", "Clear All"]
        third_buttons = [ "Increase Goal", "Decrease Goal", "Increase Column"]

        fourth_buttons = ["Increase Row", "Decrease Row", "Decrease Column"]
        buttons = []
        buttons.append(
            Button(
                top_buttons[0],
                180,
                40,
                (WIDTH + 300 + (220 - 180) / 2, 80 + search_methods.__len__() * 70),
                WIN,
                RED,
                GUI_FONT,
            )
        )

        for i, button in enumerate(second_buttons):
            buttons.append(
                Button(
                    button, 180, 40, (WIDTH + 130 + i * 190, 150 + search_methods.__len__() * 70), WIN, RED, GUI_FONT
                )
            )
        for i, button in enumerate(third_buttons):
            buttons.append(
                Button(
                    button, 180, 40, (WIDTH + 130 + +i * 190, 220 + search_methods.__len__() * 70), WIN, RED, GUI_FONT
                )
            )
        for i, button in enumerate(fourth_buttons):
            buttons.append(
                Button(
                    button, 180, 40, (WIDTH + 130 + +i * 190, 290 + search_methods.__len__() * 70), WIN, RED, GUI_FONT
                )
            )
        return buttons

    def get_clicked_search_buttons(self, pos: tuple[int, int], maze_gui: MazeGui) -> str:
        # to do convert maze_gui to have a clear function
        for button in self.search_buttons:
            # If the button is clicked
            if button.is_clicked(pos):
                # Deselect all other buttons
                for other_button in self.search_buttons:
                    other_button.is_selected = False
                # Select the clicked button
                button.is_selected = True
                maze_gui.clear_path()
                return button.text
        # Not clicked on any button
        return None

    def get_clicked_pos_of_functional_buttons(self, pos: tuple[int, int]) -> str:
        for button in self.functional_buttons:
            if button.is_clicked(pos):
                return button.text
        return None

    def pointer_in_search_button(self, pos: tuple[int, int]) -> bool:
        return pos[0] > WIDTH + 60 and pos[1] < 450 and pos[1] > 60

    def pointer_in_functional_button(self, pos: tuple[int, int]) -> bool:
        return pos[0] > WIDTH + 10 and pos[1] > 450

    def draw(self):
        for button in self.search_buttons:
            button.draw()
        for button in self.functional_buttons:
            button.draw()

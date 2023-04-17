import pygame


class TextBox:
    def __init__(
        self,
        text1: str,
        text2: str,
        text3: str,
        width: int,
        height: int,
        pos: tuple[int, int],
        screen: pygame.Surface,
        gui_font: pygame.font.Font,
    ):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.screen = screen
        self.rectangle = pygame.Rect(pos, (width, height))
        self.color = (255, 0, 0)
        self.gui_font = gui_font
        # text
        self.text_1_surf = self.gui_font.render(
            ("Grid size: " + text1 + " x " + text1), True, (255, 0, 0)
        )
        self.text_1_rect = self.text_1_surf.get_rect(
            center=(self.rectangle.center[0] - 35, self.rectangle.center[1] - 30)
        )

        self.text_2_surf = self.gui_font.render(
            ("Number of Goal: " + text2), True, (255, 0, 0)
        )
        self.text_2_rect = self.text_2_surf.get_rect(
            center=(self.rectangle.center[0] - 33, self.rectangle.center[1])
        )

        self.text_3_surf = self.gui_font.render(
            ("Number of Steps: " + text3), True, (255, 0, 0)
        )
        self.text_3_rect = self.text_3_surf.get_rect(
            center=(self.rectangle.center[0] - 28, self.rectangle.center[1] + 30)
        )

    def draw(self):
        pygame.draw.rect(
            self.screen, self.color, self.rectangle, width=2, border_radius=10
        )
        self.screen.blit(self.text_1_surf, self.text_1_rect)
        self.screen.blit(self.text_2_surf, self.text_2_rect)
        self.screen.blit(self.text_3_surf, self.text_3_rect)

    def update(self, text1: str, text2: str, text3: str):
        self.text_1_surf = self.gui_font.render(
            ("Grid size: " + text1 + " x " + text1), True, (255, 0, 0)
        )
        self.text_1_rect = self.text_1_surf.get_rect(
            center=(self.rectangle.center[0] - 35, self.rectangle.center[1] - 30)
        )

        self.text_2_surf = self.gui_font.render(
            ("Number of Goal: " + text2), True, (255, 0, 0)
        )
        self.text_2_rect = self.text_2_surf.get_rect(
            center=(self.rectangle.center[0] - 33, self.rectangle.center[1])
        )

        self.text_3_surf = self.gui_font.render(
            ("Number of Steps: " + text3), True, (255, 0, 0)
        )
        self.text_3_rect = self.text_3_surf.get_rect(
            center=(self.rectangle.center[0] - 28, self.rectangle.center[1] + 30)
        )
        
    def update_first_line(self, text1: str):
        self.text_1_surf = self.gui_font.render(
            ("Grid size: " + text1 + " x " + text1), True, (255, 0, 0)
        )
        self.text_1_rect = self.text_1_surf.get_rect(
            center=(self.rectangle.center[0] - 35, self.rectangle.center[1] - 30)
        )
    
    def update_second_line(self, text2: str):
        self.text_2_surf = self.gui_font.render(
            ("Number of Goal: " + text2), True, (255, 0, 0)
        )
        self.text_2_rect = self.text_2_surf.get_rect(
            center=(self.rectangle.center[0] - 33, self.rectangle.center[1])
        )
    
    def update_third_line(self, text3: str):
        self.text_3_surf = self.gui_font.render(
            ("Number of Steps: " + text3), True, (255, 0, 0)
        )
        self.text_3_rect = self.text_3_surf.get_rect(
            center=(self.rectangle.center[0] - 28, self.rectangle.center[1] + 30)
        )
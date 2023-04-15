import pygame

class Button:
	def __init__(self,text,width,height,pos,screen, is_pressed_color):
		#Core attributes 
		self.text = text
		self.gap = 5
		self.screen = screen
		self.is_pressed_color = is_pressed_color
		self.original_y_pos = pos[1]
		self.is_selected = False
		# top rectangle 
		self.top_rectangle = pygame.Rect(pos,(width,height))
		self.top_color = (71, 95, 119)

		# bottom rectangle 
		self.bottom_rectangle = pygame.Rect(pos,(width,height))
		self.bottom_color = (53, 75, 94)
		#text
		self.text_surf = gui_font.render(text,True,(255, 255, 255))
		self.text_rect = self.text_surf.get_rect(center = self.top_rectangle.center)

	def draw(self):
		# elevation logic 
		self.top_rectangle.y = self.original_y_pos - self.gap
		self.text_rect.center = self.top_rectangle.center 

		self.bottom_rectangle.midtop = self.top_rectangle.midtop
		self.bottom_rectangle.height = self.top_rectangle.height + self.gap

		pygame.draw.rect(self.screen,self.bottom_color, self.bottom_rectangle,border_radius = 12)
		pygame.draw.rect(self.screen,(self.top_color) if (not self.is_selected) else (self.is_pressed_color), self.top_rectangle,border_radius = 12)
		self.screen.blit(self.text_surf, self.text_rect)

	def is_clicked(self,pos):
		if self.top_rectangle.collidepoint(pos):
			return True
		return False
pygame.init()
gui_font = pygame.font.Font(None,27)
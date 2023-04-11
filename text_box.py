import pygame

class TextBox:
	def __init__(self,text1, text2, text3,width,height,pos,screen: pygame.Surface):
		self.text1 = text1
		self.text2 = text2
		self.text3 = text3
		self.screen = screen
		self.rectangle = pygame.Rect(pos,(width,height))
		self.color = (255, 0, 0)
		#text
		self.text_1_surf = gui_font.render(('Grid size: ' + text1 + ' x '+ text1),True,(255, 0, 0))
		self.text_1_rect = self.text_1_surf.get_rect(center = (self.rectangle.center[0] - 35, self.rectangle.center[1] - 30))

		self.text_2_surf = gui_font.render(('Number of Goal: ' + text2),True,(255, 0, 0))
		self.text_2_rect = self.text_2_surf.get_rect(center = (self.rectangle.center[0] - 35, self.rectangle.center[1]))
  
		self.text_3_surf = gui_font.render(('Number of Steps: ' + text3),True,(255, 0, 0))
		self.text_3_rect = self.text_3_surf.get_rect(center = (self.rectangle.center[0] - 35, self.rectangle.center[1] + 30))
	def draw(self):
		# self.text_1_rect.center = self.rectangle.center 
		pygame.draw.rect(self.screen,self.color, self.rectangle, width=2,border_radius = 10)
		self.screen.blit(self.text_1_surf, self.text_1_rect)
		self.screen.blit(self.text_2_surf, self.text_2_rect)
		self.screen.blit(self.text_3_surf, self.text_3_rect)
	
	def update(self, text1, text2, text3):
		self.text_1_surf = gui_font.render(('Grid size: ' + text1 + ' x '+ text1),True,(255, 0, 0))
		self.text_1_rect = self.text_1_surf.get_rect(center = (self.rectangle.center[0] - 35, self.rectangle.center[1] - 30))

		self.text_2_surf = gui_font.render(('Number of Goal: ' + text2),True,(255, 0, 0))
		self.text_2_rect = self.text_2_surf.get_rect(center = (self.rectangle.center[0] - 35, self.rectangle.center[1]))
  
		self.text_3_surf = gui_font.render(('Number of Steps: ' + text3),True,(255, 0, 0))
		self.text_3_rect = self.text_3_surf.get_rect(center = (self.rectangle.center[0] - 35, self.rectangle.center[1] + 30))
pygame.init()
gui_font = pygame.font.Font(None,20)
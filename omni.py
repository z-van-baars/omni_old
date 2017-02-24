import pygame
import carto
import colors


class Session(object):
	def __init__(self, x_tiles, y_tiles):
		self.game_map = carto.GameMap(x_tiles, y_tiles)

class DisplayContainer(object):
	def __init__(self, x_resolution, y_resolution):
		self.screen = pygame.display.set_mode([x_resolution, y_resolution])
		self.screen.fill(colors.black)


def draw_to_screen(session, screen):
	screen.blit(session.game_map.display_layer, [0, 0])
	pygame.display.flip()


def event_processing(event, session):
	if event.type == pygame.QUIT:
		pygame.display.quit()
		pygame.quit()


def main():
	playing = True
	new_session = Session(100, 100)
	session_display = DisplayContainer(400, 300)
	pygame.init()
	pygame.display.set_mode([400, 300])
	while playing:
		for event in pygame.event.get():
			event_processing(event, session)
		draw_to_screen(new_session, session_display.screen)





import pygame
from constants import *
#Class defines
from circleshape import *
from player  import *
from asteroid import *
from AsteroidField import *



def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	groupupdate = pygame.sprite.Group()
	groupdraw = pygame.sprite.Group()
	groupASS = pygame.sprite.Group()
	Player.containers = (groupdraw, groupupdate)
	Asteroid.containers = (groupASS, groupdraw, groupupdate)
	AsteroidField.containers = groupupdate
	asteroid_field = AsteroidField()

	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Thank you for Playing Asteroids")
				return
		groupupdate.update(dt)
		for asteroid in groupASS:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()


		screen.fill("black")
		for obj in groupdraw:
			obj.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) /1000



if __name__ == "__main__":
    main()

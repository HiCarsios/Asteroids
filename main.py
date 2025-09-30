import pygame
from constants import *
#Class defines
from circleshape import *
from player  import *
from asteroid import *
from AsteroidField import *
from shot import *


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	groupupdate = pygame.sprite.Group()
	groupdraw = pygame.sprite.Group()
	groupASS = pygame.sprite.Group()
	groupshot = pygame.sprite.Group()
	Player.containers = (groupdraw, groupupdate)
	Asteroid.containers = (groupASS, groupdraw, groupupdate)
	Shot.containers = (groupshot, groupdraw, groupupdate)
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
			if asteroid.collision(player):
				print("Game over!")
				return

			for shot in groupshot:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.kill()

		screen.fill("black")
		for obj in groupdraw:
			obj.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) /1000



if __name__ == "__main__":
    main()

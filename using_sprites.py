# sprites are an easy way to create a 2D bitmapped object in Arcade
# Arcade has methods that make it easy to draw, move and animate sprites
# can also easily use sprites to DETECT COLLISIONS between objects

# now let's create a sprite
# sprites are normally organized into lists
# the lists make it easier to manage the sprites
# sprites in a list will use OpenGL to batch-draw the sprites as a group

import arcade
import random

# set sprite here
# set to be 15% of the original size
SPRITE_SCALING_COIN = 0.3
SPRITE_SCALING_PLAYER = 0.1
COINT_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "jungkook_collecting_coins"

class Coin(arcade.Sprite):
	# this class represents the coins on the screen
	# child class of the arcade library's "Sprite" class
	def reset_pos(self):
		# to reset the coin to a random spot above the screen
		self.center_y = random.randrange(SCREEN_HEIGHT + 20,
			SCREEN_HEIGHT + 100)
		self.center_x = random.randrange(SCREEN_WIDTH)

	def update(self):
		# move the coin
		self.center_y -= 5

		# if coin falls off the bottom of the screen, reset it
		if self.top < 0:
			self.reset_pos()


class FirstGame(arcade.Window):

	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

		# set variables that will hold sprite lists
		self.player_list = None
		self.coin_list = None

		# set up player info
		self.player_sprite = None
		self.score = 0

		# make the mouse cursor invisible
		self.set_mouse_visible(False)

		arcade.set_background_color(arcade.color.BLACK)

	def setup(self):
		# set up your game here and initialize variables

		# this will set up a game with a player and a bunch of coins
		# for the player to collect
		# we use TWO lists: one for player and one for coins
		# now, wecreate sprite lists
		self.player_list = arcade.SpriteList()
		self.coin_list = arcade.SpriteList()

		# score
		self.score = 0

		# now set up player
		# let's choose jungkook character image :p
		self.player_sprite = arcade.Sprite("jungkook.png", SPRITE_SCALING_PLAYER)
		self.player_sprite.center_x = 50 # starting position
		self.player_sprite.center_y = 50
		self.player_list.append(self.player_sprite)

		# now create the coins
		for i in range(COINT_COUNT):
			# create the coin instance
			coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

			# now position the coin
			coin.center_x = random.randrange(SCREEN_WIDTH)
			coin.center_y = random.randrange(SCREEN_HEIGHT)

			# now you wanna add the coin to the lists
			self.coin_list.append(coin)

	def on_draw(self):
		# drawing commands go here
		arcade.start_render()
		self.coin_list.draw()
		self.player_list.draw()

		# put the score text on the screen!
		output = f"Jungkook's score: {self.score}"
		arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

	def on_mouse_motion(self, x, y, dx, dy):
		# this handles mouse motion!

		# move the center of the player sprite to match the mouse x, y
		self.player_sprite.center_x = x
		self.player_sprite.center_y = y

	def update(self, delta_time):
		# all the game logic like, movement

		# call update on all sprites
		self.coin_list.update()

		# generate a list of all coin sprites that collide with jungkook
		coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

		# now, loop through each sprite which collided with jungkook
		# remove it and add it to score!
		for coin in coins_hit_list:
			# coin.remove_from_sprite_lists()
			self.score += 1
			coin.center_y = random.randrange(SCREEN_HEIGHT + 20,
				SCREEN_HEIGHT + 100)
			coin.center_x = random.randrange(SCREEN_WIDTH)


def main():
	game = FirstGame()
	game.setup()
	arcade.run()

if __name__ == "__main__":
	main()

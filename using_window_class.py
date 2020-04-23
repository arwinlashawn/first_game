# learn how to use the Window class
# typically you wanna use this when making a game

### NOTES ###
# The Window class has several method that your programs can override
# to provide functionality to the program. Commonly used ones:
# 1. on_draw: for codes that draw
# 2. update: for codes to move items and perform game logic
# 3. on_key_press: handle events when a key is pressed
# 4. on_key_release: handle events when a key is released
# 5. on_mouse_motion: called every time the mouse moves
# 6. on_mouse_press: called when a mouse button is pressed
# 7. set_viewport: use in scrolling games, when you have a world much 
#    larger than what can be seen on one screen. Calling set_viewport
# 	 allows a programmer to set what part of that world is currently
#    visible



import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class FirstGame(arcade.Window):

	def __init__(self, width, height):
		super().__init__(width, height)

		arcade.set_background_color(arcade.color.BLACK)

	def setup(self):
		# set up your game here
		pass

	def on_draw(self):
		arcade.start_render()
		# drawing commands here

	def update(self, delta_time):
		# all the game logic like, movement
		pass


def main():
	game = FirstGame(SCREEN_WIDTH, SCREEN_HEIGHT)
	game.setup()
	arcade.run()

if __name__ == "__main__":
	main()




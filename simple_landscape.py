# drawing a landscape with trees using functions

import arcade

# define some important constants 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "simple_landscape"


# let's draw the sky and ground
def draw_background():
	# let's make the sky in the top two-thirds
	arcade.draw_lrtb_rectangle_filled(0,
		SCREEN_WIDTH,
		SCREEN_HEIGHT,
		SCREEN_HEIGHT * (1/3),
		arcade.color.SKY_BLUE)

	# now draw the fround in the bottom third
	arcade.draw_lrtb_rectangle_filled(0,
		SCREEN_WIDTH,
		SCREEN_HEIGHT/3,
		0,
		arcade.color.SACRAMENTO_STATE_GREEN)

def draw_bird(x, y):
	# draw a bird using arcs
	arcade.draw_arc_outline(x, y, 40, 20, arcade.color.BLACK, 0, 90, 5)
	arcade.draw_arc_outline(x + 40, y, 40, 20, arcade.color.BLACK, 90, 180, 5)

def draw_pine_tree(x, y):
	# simply draw a triangle on top of the trunk
	arcade.draw_triangle_filled(x + 40, y,
		x, y - 100,
		x + 80, y - 100,
		arcade.color.PASTEL_GREEN)

	# now, the trunk
	arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
		arcade.color.DARK_BROWN)

# this the main program
def main():
	# to open window
	arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

	# to start render process
	# must be done before any drawing commands
	arcade.start_render()

	# now call the drawing commands
	draw_background()
	draw_pine_tree(50, 250)
	draw_pine_tree(350, 320)
	draw_bird(70, 400)
	draw_bird(470, 450)

	# to finish render
	arcade.finish_render()

	# to keep window open until you hit 'exit'
	arcade.run()

if __name__ == "__main__":
	main()






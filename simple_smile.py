import arcade

# set constants for screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# open the window
# set window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "simple_smile")

# set background color to white
# for full list of colors: http://arcade.academy/arcade.color.html
arcade.set_background_color(arcade.color.WHITE)

# to start render process
# must be done before any drawing commands
arcade.start_render()

# time to draw the face
# determine x and y positions
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# now, draw the right eye
x = 370
y = 350
radius = 25
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# now, draw the left eye
x = 230
y = 350
radius = 25
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# draw the smile
x = 300
y = 250
width = 150
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 13)

# finish drawing and display result : )
arcade.finish_render()

# keep window open until you hit 'exit'
arcade.run()



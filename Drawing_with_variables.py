import arcade


WIDTH = 640
HEIGHT = 480

x = 320
y = 240
r = 75
arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, r, arcade.color.MEDIUM_RED_VIOLET)
arcade.draw_rectangle_filled(x, y, r, 100,  arcade.color.RED)
# End drawing
arcade.finish_render()
arcade.run()

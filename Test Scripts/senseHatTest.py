from sense_hat import SenseHat
sense = SenseHat()

blue = (0,0,255)
yellow = (255, 255, 0)
red = (255, 0, 0)
while True:
	sense.show_message("Asser Ibrahim", text_colour=blue, back_colour=red,scroll_speed=0.05)

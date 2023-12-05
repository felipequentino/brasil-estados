# The first step to make this game with your country, is paste a image of the states of your country in this file,
# after that, run this code and point click the states and write in the box the name of the states.

import turtle
import csv

# Creating the file to save the states cords
csv_file = open('estados_coords.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Estado', 'Coordenada X', 'Coordenada Y'])

# Dimensios of turtle
screen = turtle.Screen()
image = "mapa.gif"
screen.addshape(image)
turtle.shape(image)

# Function to write in the doc the coords by your click
def get_mouse_click_coords(x, y):
    estado = screen.textinput("Estado", "Insira o nome do estado:")
    if estado:
        csv_writer.writerow([estado, x, y])

turtle.onscreenclick(get_mouse_click_coords)

turtle.mainloop()

# Closing csv file after conclusion, good practice.
csv_file.close()

# Librerias necesarias
# Instalar con:
# sudo apt-get install python3-pil
# sudo apt-get install python3-numpy
from PIL import Image
from numpy import complex, array
import colorsys

# Tamanio de la imagen
# Cuanto mas resolucion mas demora en generar
WIDTH = 1024
# Cuantos elementos de la serie se computan como maximo
# Un valor mas grande produce mayor definicion de colores pero
# Demora mas en generar
L_SERIE = 4096

# Retornar una tupla de valores como color RGB
def rgb_conv(i):
	color = 255 * array(colorsys.hsv_to_rgb(0.5, 1.0, i / (L_SERIE/4)))
	return tuple(color.astype(int))

# Funcion para determinar mandelbrot
def mandelbrot(x, y):
	c0 = complex(x, y)
	c = 0
	for i in range(1, L_SERIE):
                #La serie no converge
		if abs(c) > 2:
			return rgb_conv(i)
		c = c * c + c0
        #La serie converge devuelve color negro
	return (0, 0, 0)

# Crear nueva imagen
img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()

# Definir Zoom para la imagen
# y centrarla en un punto
CNTR_X = -0.748
CNTR_Y = 0.1
ZOOM = 75

# Recorrer los puntos en el plano complejo y dibujar Mandelbrot
# En negro los puntos que pertenecen al conjunto
for x in range(img.size[0]):
	print("%.2f %%" % (x / WIDTH * 100.0))
	for y in range(img.size[1]):
		pixels[x, y] = mandelbrot(CNTR_X + (-img.size[0]/2. + x)/(ZOOM*img.size[0]), CNTR_Y + (-img.size[1]/2. + y)/(ZOOM*img.size[0]))
                #print(CNTR_X + (-img.size[0]/2. + x)/(ZOOM*img.size[0]), CNTR_Y + (-img.size[1]/2. + y)/(ZOOM*img.size[1]))

img.save("/home/amartino/mandelbrot3.png")
img.show()

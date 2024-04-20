import matplotlib.pyplot as plt


def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx


    if steep:
        x1, y1 = y1, x1  # Intercambia las coordenadas x y y
        x2, y2 = y2, x2


    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True


    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx / 2
    ystep = 1 if y1 < y2 else -1


    y = y1
    points = []






    for x in range(x1, x2 + 1):
        if steep:
            points.append((y, x))
        else:
            points.append((x, y))


        error -= dy
        if error < 0:
            y += ystep
            error += dx


    if swapped:
        points.reverse()


    return points


# Coordenadas de inicio y fin de la línea
x1, y1 = 1, 1
x2, y2 = 8, 5


# Obtener los puntos en la línea usando Bresenham
points = bresenham_line(x1, y1, x2, y2)


# Dibujar la línea
x_values, y_values = zip(*points)
plt.plot(x_values, y_values, marker='o', linestyle='-')


# Configurar los ejes
plt.xlim(0, 10)
plt.ylim(0, 10)


# Etiquetar los ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')


# Título del gráfico
plt.title('Algoritmo de Bresenham para Dibujar una Línea')


# Mostrar el gráfico
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
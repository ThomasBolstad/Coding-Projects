import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)


    def __calculate_displacement(self):
        v = self.__speed
        o = self.__angle
        h = self.__height
        g = GRAVITATIONAL_ACCELERATION
        d = (v * math.cos(o) * (v * math.sin(o) + math.sqrt((v ** 2 * math.sin(o) ** 2) + (2 * g * h)))) / g
        return d
    def __str__(self):
        output = '\nProjectile details:\n'
        v = self.__speed
        o = int(math.degrees(self.__angle))
        h = self.__height
        d = self.__calculate_displacement()
        speed_line = f'speed: {v} m/s\n'
        output += speed_line
        height_line = f'height: {h} m\n'
        output += height_line

        angle_line = f'angle: {o}\N{DEGREE SIGN}\n'
        output += angle_line
        d_line = f'displacement: {d:.1f} m\n'
        output += d_line
        return output

    def __calculate_y_coordinate(self, x):
        g = GRAVITATIONAL_ACCELERATION
        y0 = self.__height
        v0 = self.__speed
        o = self.__angle
        y = y0 + (x * math.tan(o)) - (g * x ** 2)/(2 * v0 ** 2 * math.cos(o) ** 2)
        return y
    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]  


ball1 = Projectile(100, 3, 45)
ball = Projectile(10, 3, 45)
print(ball1)

print(ball)
displacement_of_ball = ball._Projectile__calculate_displacement()
y_coord = ball._Projectile__calculate_y_coordinate(4)
print(y_coord)
coordinates = ball.calculate_all_coordinates()
print(coordinates)
print()


        
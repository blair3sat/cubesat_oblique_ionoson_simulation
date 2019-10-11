import math
import matplotlib.pyplot as plt

cubesat_velocity = 290  # km/s
cubesat_height = 250  # km
cubesat_x = 0

beam_size = math.pi / 4
beam_angle = math.pi

chirp_rate = 100  # khz/s


x1 = 0  # km
y1 = 0  # km

x2 = 100  # km
y2 = 0  # km

ionosphere_height = 300

t = 0
t_step = 0.1


def getFreq(t):
    return t * chirp_rate


def calculateBounceHeight(freq):
    return ionosphere_height  # todo


def getBounds(beam_angle, beam_size, height):
    return (
        height / math.tan(beam_angle + beam_size),
        height / math.tan(beam_angle)
    )


def calculatebounds():
    global t, t_step, beam_size, beam_angle, cubesat_height, cubesat_x, cubesat_velocity, ionosphere_height
    data_points = []
    while True:
        t += t_step

        cubesat_x += cubesat_velocity * t_step

        freq = getFreq(t)
        bounceHeight = calculateBounceHeight(freq)

        print(freq, bounceHeight)

        (normal_upper, normal_lower) = getBounds(
            beam_angle,
            beam_size,
            cubesat_height
        )

        (bounced_upper, bounced_lower) = getBounds(
            beam_angle,
            beam_size,
            cubesat_height + 2*(ionosphere_height-cubesat_height)
        )

        print(normal_upper, normal_lower)
        print(bounced_upper, bounced_lower)
        print(cubesat_x)

        if normal_lower < cubesat_x < normal_upper:
            data_points.append([cubesat_x, freq])

        if bounced_lower < cubesat_x < bounced_upper:
            data_points.append([cubesat_x, freq])

        if cubesat_x > bounced_upper and cubesat_x > normal_upper:
            break
    print(data_points)
    plt.scatter(*zip(*data_points), )
    plt.show()


calculatebounds()

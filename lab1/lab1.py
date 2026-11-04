import math
import random
import matplotlib.pyplot as plt

NUMBER_OF_SIMULATIONS = 100000

def y_func(v_0y, t):
    return v_0y*t - 1/2 * 10 * t*t

def crosses_region(region, v_0x, v_0y):
    # Vertical regions
    if region[0] == region[2]:
        t = region[0] / v_0x
        y = y_func(v_0y, t)
        if  y > region[1] and y < region[3]:
            return True

    # Horizontal regions
    else: 
        y_target = region[1]
        delta = v_0y * v_0y - 2 * 10 * y_target
        if delta >= 0:
            t1 = (v_0y + math.sqrt(delta)) / 10
            t2 = (v_0y - math.sqrt(delta)) / 10
            x1 = v_0x * t1
            x2 = v_0x * t2
            if x1 > region[0] and x1 < region[2]:
                return True
            if x2 > region[0] and x2 < region[2]:
                return True
    return False
 

def calculate_trajectory(v_0x, v_0y, x_0, y_0):
    x_list = []
    y_list = []
    t = 0.0
    g = 10.0

    while True:
        x = v_0x * t + x_0
        x_list.append(x)

        y = v_0y * t - 0.5 * g * t * t + y_0
        y_list.append(y)

        if y < 0:
            break
        t += 0.01

    return x_list, y_list



def main():
    allowed_regions = [
        [2, 2, 2, 8],  # x_start, y_start, x_end, y_end
        [11, 3, 11, 7],  # x_start, y_start, x_end, y_end
    ]
    forbidden_regions = [
        [4, 5, 5, 5],  # x_start, y_start, x_end, y_end
        [7, 5, 10, 5],  # x_start, y_start, x_end, y_end
    ]
  

    x_0 = 0
    y_0 = 0
    v_0_points = []
    alpha_points = []

    for _ in range(NUMBER_OF_SIMULATIONS):
        v_0 = random.uniform(1.0, 30.0)   
        alpha_deg = random.uniform(1.0, 89.0)
        alpha_rad = math.radians(alpha_deg)
        v_0x = v_0 * math.cos(alpha_rad)
        v_0y = v_0 * math.sin(alpha_rad)

        isValid = False
        for region in allowed_regions:
            if crosses_region(region, v_0x, v_0y):
                isValid = True
            else:
                isValid = False
                break
        for region in forbidden_regions:
            if crosses_region(region, v_0x, v_0y):
                isValid = False
        if isValid:
            if len(v_0_points) < 5:
                x, y = calculate_trajectory(v_0x, v_0y, x_0, y_0)
                color = (random.random(), random.random() * 0.3, random.random())
                plt.plot(x, y, color=color, linewidth=0.25)
            v_0_points.append(v_0)
            alpha_points.append(alpha_deg)

    x = [forbidden_regions[0][0], forbidden_regions[0][2]]
    y = [forbidden_regions[0][1], forbidden_regions[0][3]]
    plt.plot(x, y, 'r', linewidth=2, label="R1")

    x = [forbidden_regions[1][0], forbidden_regions[1][2]]
    y = [forbidden_regions[1][1], forbidden_regions[1][3]]
    plt.plot(x, y, 'tomato', linewidth=2, label="R2")

    x = [allowed_regions[0][0], allowed_regions[0][2]]
    y = [allowed_regions[0][1], allowed_regions[0][3]]
    plt.plot(x, y, 'g', linewidth=2, label="R3")

    x = [allowed_regions[1][0], allowed_regions[1][2]]
    y = [allowed_regions[1][1], allowed_regions[1][3]]
    plt.plot(x, y, 'springgreen', linewidth=2, label="R4")

    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc="upper right")
    plt.title('Trajectory Simulation')
    plt.show()


    plt.plot(alpha_points, v_0_points,'o', markersize=1)
    plt.xlabel('alpha [deg]')
    plt.ylabel('v_0 [m/s]')
    plt.grid(True)
    plt.show()

    prob = len(v_0_points) / NUMBER_OF_SIMULATIONS
    print(prob)


if __name__ == '__main__':
    main()

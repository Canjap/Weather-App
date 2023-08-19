import matplotlib.pyplot as plt
import numpy as np 
from db_funcs import check_connect, get_values


def plot_weather():
    values = get_values("""
                SELECT tempCelsius FROM weather WHERE tempCelsius IS NOT NULL
               """,
               """
                SELECT humidity 
                FROM weather 
                WHERE humidity IS NOT NULL AND pressure IS NOT NULL
                """,
               """
                SELECT pressure FROM weather WHERE pressure IS NOT NULL
                """)
    plot_x = []
    plot_y = []
    for i in range(len(values)):
        for j in range(len(values[0])):
            x = values[i][j][0]
            y = i
            plot_x.append(x)
            plot_y.append(y)
            print(plot_x, plot_y, x, y)
            plt.plot(plot_x, plot_y)
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # giving a title to my graph
    plt.title('My first graph!')
    plt.show()
    return values
plot_weather()
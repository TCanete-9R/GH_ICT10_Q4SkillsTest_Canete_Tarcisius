from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def update_all(event):
    values = [
        document.getElementById("mon").value,
        document.getElementById("tue").value,
        document.getElementById("wed").value,
        document.getElementById("thu").value,
        document.getElementById("fri").value
    ]

    absences = [int(v) if v != "" else 0 for v in values]

    show_graph(absences)



def show_graph(absences):
    plt.clf() 

    x = np.array(days)
    y = np.array(absences)

    plt.plot(x, y)
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")

    display(plt, target='output')

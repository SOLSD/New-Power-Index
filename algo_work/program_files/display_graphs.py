import matplotlib.pyplot as plt

def plot_graph(results):
    xpoints = []
    ypoints = []
    for result in results:
        xpoints.append(result[0])
        ypoints.append(result[-1])

    plt.plot(xpoints, ypoints, 'o--g')

    plt.title("Relative Power of Parties")
    plt.xlabel("Parties")
    plt.ylabel("Relative Power")

    plt.grid(axis = 'x')

    plt.xticks(rotation = 90)

    plt.show()
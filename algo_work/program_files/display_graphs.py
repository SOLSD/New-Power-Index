import matplotlib.pyplot as plt


def plot_graph(results):
    """
    Takes final, normalised scores of algorithm and plots them as a line graph for ease of readability.
    """
    xpoints = []
    ypoints = []
    for result in results:
        xpoints.append(result[0])  # Adds names of all parties to x axis of graph
        ypoints.append(result[-1])  # Adds scores of each party to y axis of graph

    plt.plot(xpoints, ypoints, 'o--g')  # Plots appropriate points with dashed green line

    plt.title("Relative Power of Parties")
    plt.xlabel("Parties")
    plt.ylabel("Relative Power")

    plt.grid(axis='x')

    plt.xticks(rotation=90)

    plt.show()

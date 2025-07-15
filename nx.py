import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell
def _():
    import networkx as nx
    return (nx,)


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(nx):
    g = nx.DiGraph()
    return (g,)


@app.cell
def _(g):
    g.add_edges_from([(1,2), (2,3), (3,4), (5,6), (6,7), (6, 8), (8, 9)])
    print(g)
    return


@app.cell
def _(g, nx, plt):
    nx.draw_shell(g, with_labels=True)
    plt.show()
    return


@app.cell
def _(g, nx):
    independent_node_sets = list(nx.weakly_connected_components(g))
    return (independent_node_sets,)


@app.cell
def _(independent_node_sets):
    independent_node_sets
    return


@app.cell
def _(g, independent_node_sets):
    disconnected_subnetworks = [
        g.subgraph(node_set) for node_set in independent_node_sets
    ]
    return (disconnected_subnetworks,)


@app.cell
def _(disconnected_subnetworks):
    disconnected_subnetworks
    return


@app.cell
def _(disconnected_subnetworks):
    g1, g2 = disconnected_subnetworks
    return g1, g2


@app.cell
def _(g1, nx, plt):
    nx.draw_shell(g1, with_labels=True)
    plt.show()
    return


@app.cell
def _(g2, nx, plt):
    nx.draw_shell(g2, with_labels=True)
    plt.show()
    return


if __name__ == "__main__":
    app.run()

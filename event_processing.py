import marimo

__generated_with = "0.14.10"
app = marimo.App(width="full")

with app.setup:
    # Initialization code that runs before all other cells
    from dataclasses import astuple, dataclass
    import collections
    import operator

    import marimo as mo
    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np
    import pandas as pd


@app.cell(hide_code=True)
def _():
    mo.md(r"""# Wrangle the Data (Events and Projects)""")
    return


@app.cell
def _():
    df = pd.read_csv("scenarios/real_event_log.tsv", sep="\t")
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.to_records(index=False)[:5]
    return


@app.class_definition
@dataclass
class Event:
    date: str
    id: int
    parent_id: int|None
    who: str
    event: str

    def __post_init__(self):
        # Coerce date to str
        self.date = str(self.date)

        # Coerce id to int
        self.id = int(self.id)

        # Coerce parent_id to int or None
        if self.parent_id is None or pd.isna(self.parent_id):
            self.parent_id = None
        else:
            self.parent_id = int(self.parent_id)

    def __str__(self):
        """Make an easy str for this example"""
        return f"{self.id}-{self.date[-2:]}"


@app.cell
def _(df):
    events = [
        Event(*data)
        for data in df.to_records(index=False)
    ]
    events[:5]
    return (events,)


@app.cell
def _(events):
    e = events[0]
    return (e,)


@app.cell
def _(e):
    e
    return


@app.cell
def _():
    TERMINATING_EVENTS = set([
        "approve",
        "reject",
        "withdraw",
    ])
    return (TERMINATING_EVENTS,)


@app.cell
def _(events):
    event_sets = collections.defaultdict(list)
    for _e in events:
        event_sets[_e.id].append(_e)
    return (event_sets,)


@app.cell
def _(event_sets):
    sorted(event_sets)
    return


@app.cell
def _(event_sets):
    [repr(e) for e in event_sets[6]]
    return


@app.class_definition
@dataclass
class Chain:
    id: int
    start_date: str
    start_event: str
    parent_id: int | None = None
    end_date: str | None = None
    end_event: str | None = None

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.parent_id or " "}-{self.id}-{self.start_event}-{self.end_event}"


@app.cell
def _(TERMINATING_EVENTS, event_sets):
    chains: list[Chain] = []
    for events_1 in event_sets.values():
        event_list = sorted(events_1, key=operator.attrgetter('date'))
        potential_start_event: Event = event_list[0]
        potential_end_event: Event = event_list[-1]
        _c = Chain(id=potential_start_event.id, start_date=potential_start_event.date, start_event=potential_start_event.event, parent_id=potential_start_event.parent_id or None)
        chains.append(_c)
        if potential_end_event.event in TERMINATING_EVENTS:
            _c.end_date = potential_end_event.date
            _c.end_event = potential_end_event.event
    return (chains,)


@app.cell
def _(chains: list[Chain]):
    index_of_chains = {_p.id: _p for _p in chains}
    return (index_of_chains,)


@app.cell
def _(index_of_chains):
    index_of_chains
    return


@app.cell
def _(chains: list[Chain]):
    chains_by_name = {str(_c): _c for _c in chains}
    chains_by_name
    return (chains_by_name,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""# Graph Those Chains!""")
    return


@app.cell
def _(chains: list[Chain], index_of_chains):
    g = nx.DiGraph()
    for _p in chains:
        g.add_node(str(_p))
    for _p in chains:
        if _p.parent_id:
            g.add_edge(str(index_of_chains[_p.parent_id]), str(_p))
    return (g,)


@app.cell
def _(g):
    g.nodes
    return


@app.cell
def _(g):
    g.edges
    return


@app.cell
def _(g):
    nx.draw_planar(g, with_labels=True)
    plt.show()
    return


@app.cell
def _(g):
    all_nodes = set(g.nodes)
    all_nodes
    return (all_nodes,)


@app.cell
def _(g):
    all_linkages = nx.dfs_successors(g)
    all_linkages
    return (all_linkages,)


@app.cell
def _(all_linkages):
    parents = set(all_linkages)
    children = set()
    for child_list in all_linkages.values():
        for child in child_list:
            children.add(child)
    return children, parents


@app.cell
def _(parents):
    sorted(parents)
    return


@app.cell
def _(children):
    sorted(children)
    return


@app.cell
def _(all_nodes, children, parents):
    islands = all_nodes - parents - children
    roots = islands | parents - children
    leaves = children - parents
    return islands, leaves, roots


@app.cell
def _(roots):
    sorted(roots)
    return


@app.cell
def _(leaves):
    sorted(leaves)
    return


@app.cell
def _(islands):
    sorted(islands)
    return


@app.cell
def _(chains_by_name, g, islands, leaves, roots):
    def display(name: str) -> None:
        chain = chains_by_name[name]
        t = astuple(chain)
        print("{0} | {1:7} | {2:7} | {3!s:4} | {4!s:10} | {5}".format(*t))

    for start in sorted(islands | roots):
        start_has_path = False
        for leaf in leaves:
            if nx.has_path(g, start, leaf):
                start_has_path = True
                for path in nx.all_simple_paths(g, start, leaf):
                    print()
                    for n in path:
                        display(n)
        if not start_has_path:
            display(start)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""# Questions?""")
    return


if __name__ == "__main__":
    app.run()

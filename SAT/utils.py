import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import random


def display_nqueens(sol):
    board = [[0] * len(sol) for i in range(len(sol))]
    for x, y in sol:
        board[x][y] = 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            symbol = '♛' if board[i][j] == 1 else '.'
            print(symbol, end=' ')
        print()

def display_pigeons(sol, m):
    board = [0]*m
    for y in sol:
        board[y] = 1
    for i in range(len(board)):
        symbol = '[🕊]' if board[i] == 1 else '[.]'
        print(symbol, end=' ')
    print()

def display_color_graph(E, sol = None):
    G = nx.Graph()
    G.add_edges_from(E)
    colors = {}
    if sol:
        for v, c in sol:
            colors[c] = colors.get(c, random.random())
        assigned_colors = {v:colors[c] for v, c in sol}
        node_colors = [assigned_colors.get(node, 0.25) for node in G.nodes()]
    else:
        node_colors = [0] * len(list(set([v1 for v1, _ in E] + [v2 for _, v2 in E])))
    nx.draw(G, with_labels = True, node_color=node_colors, font_color='white') 

def display_nurses_shifts(sol, num_nurses, num_shifts, num_days):
    for d in range(num_days):
        print('Day %i' % d)
        for n in range(num_nurses):
            is_working = False
            for s in range(num_shifts):
                if (n, d, s) in sol:
                    is_working = True
                    print('  Nurse %i works shift %i' % (n, s))
            if not is_working:
                print('  Nurse {} does not work'.format(n))
    
def display_sudoku(sol):
    fig, ax = plt.subplots(figsize=(4, 4))
    for l in range(9):
        for c in range(9):
            v = sol[c][l]
            s = " "
            if v > 0:
                s = str(v)
            ax.text(l+0.5, 8.5-c, s, va='center', ha='center')
        ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.set_xticks(np.arange(9))
    ax.set_yticks(np.arange(9))
    ax.grid()
    plt.show()


def display_scheduling(sol):
    schedule = pd.DataFrame(sol)

    jobs = sorted(list(schedule['job'].unique()))
    machines = sorted(list(schedule['machine'].unique()))
    makespan = schedule['finish'].max()

    bar_style = {'alpha': 1.0, 'lw': 25, 'solid_capstyle': 'butt'}
    text_style = {'color': 'white', 'weight': 'bold', 'ha': 'center', 'va': 'center'}
    colors = mpl.cm.Dark2.colors

    fig, ax = plt.subplots(figsize=(8, len(machines) + 1))

    for _, row in schedule.iterrows():
        m = row['machine']
        j = row['job']
        xs = row['start']
        xf = row['finish']
        ax.plot([xs, xf], [m + 1] * 2, c=colors[j % 8], **bar_style)
        ax.text((xs + xf) / 2, m + 1, j, **text_style)

    ax.set_title('Machine Schedule')
    ax.set_ylabel('Machine')
    ax.set_xlabel('Time')

    for _, s in enumerate([jobs, machines]):
        ax.set_ylim(0.5, len(s) + 0.5)
        ax.set_yticks(range(1, 1 + len(s)))
        ax.set_yticklabels(s)

    ax.text(makespan, ax.get_ylim()[0] - 0.2, "{0:0.1f}".format(makespan), ha='center', va='top')
    ax.plot([makespan] * 2, ax.get_ylim(), 'r--')
    ax.grid(True)

    fig.tight_layout()
    plt.show()

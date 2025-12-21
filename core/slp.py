import pandas as pd
import math



def convert_adjacency_matrix(adj_matrix):
    values = {
        "A": 6,
        "E": 5,
        "I": 4,
        "O": 3,
        "U": 2,
        "X": 0
    }
    return adj_matrix.replace(values)




def generate_slp_layout(departments):
    layout = {}

    
    cols = math.ceil(math.sqrt(len(departments)))

    for i, dept in enumerate(departments):
        x = i % cols      
        y = i // cols
        layout[dept] = (x, y)

    return layout




def rectilinear_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])



def slp_total_distance(flow_matrix, layout):
    total = 0

    for i in flow_matrix.index:
        for j in flow_matrix.columns:
            if i != j:
                fij = flow_matrix.loc[i, j]
                dij = rectilinear_distance(layout[i], layout[j])
                total += fij * dij

    return total


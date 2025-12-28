import numpy as np
import pandas as pd


def compute_flux_matrices(machines, routings):
   

    n = len(machines)

    # Initialisation matrice numpy
    flow_np = np.zeros((n, n))

    # Dictionnaire machine → index
    machine_index = {m: i for i, m in enumerate(machines)}
    # Appel MST
      from core.mst import modified_mst
      sequence = modified_mst(flow_np, clearance_matrix, lengths)
    # Appel SLP
      from core.slp import generate_slp_layout, slp_total_distance
      layout = generate_slp_layout(flow_df.index)
      total_distance = slp_total_distance(flow_df, layout)

    # Calcul des flux
    for routing in routings:
        for k in range(len(routing) - 1):
            i = machine_index[routing[k]]
            j = machine_index[routing[k + 1]]

            flow_np[i, j] += 1
            flow_np[j, i] += 1  # symétrique

    # Conversion en DataFrame pour SLP
    flow_df = pd.DataFrame(flow_np, index=machines, columns=machines)
  
    return flow_np, flow_df

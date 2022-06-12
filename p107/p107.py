import numpy as np


def is_connected(adj_matrix: np.matrix):
    queue = [0]
    visited = set()

    while len(queue) > 0:
        cur_node = queue.pop(0)
        visited.add(cur_node)

        for i in range(adj_matrix.shape[1]):
            if adj_matrix[cur_node, i] > 0 and i not in visited and i not in queue:
                queue.append(i)
    return len(visited) == adj_matrix.shape[1]


def get_adj_matrix_input() -> np.matrix:
    adj_matrix = np.loadtxt("network.txt", delimiter=",", dtype=str)
    return np.vectorize(lambda x: 0 if x == '-' else int(x))(adj_matrix)


network_matrix = get_adj_matrix_input()
greedy_check_network = network_matrix.copy()

total_saving = 0
while np.sum(greedy_check_network) > 0:
    max_idx = np.unravel_index(np.argmax(greedy_check_network, axis=None), greedy_check_network.shape)
    max_idx_rev = tuple(reversed(max_idx))

    max_value = greedy_check_network[max_idx]

    greedy_check_network[max_idx] = 0
    greedy_check_network[max_idx_rev] = 0

    network_matrix[max_idx] = 0
    network_matrix[max_idx_rev] = 0
    if not is_connected(network_matrix):
        network_matrix[max_idx] = max_value
        network_matrix[max_idx_rev] = max_value
    else:
        total_saving += max_value

print(total_saving)

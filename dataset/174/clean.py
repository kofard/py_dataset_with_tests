"""
Algorithm for calculating the most cost-efficient sequence for converting one string
into another.
The only allowed operations are
--- Cost to copy a character is copy_cost
--- Cost to replace a character is replace_cost
--- Cost to delete a character is delete_cost
--- Cost to insert a character is insert_cost
"""

def compute_transform_tables(source_string: str, destination_string: str, copy_cost: int, replace_cost: int, delete_cost: int, insert_cost: int) -> tuple[list[list[int]], list[list[str]]]:
    """Finds the most cost efficient sequence
    for converting one string into another."""
    source_seq = list(source_string)
    destination_seq = list(destination_string)
    len_source_seq = len(source_seq)
    len_destination_seq = len(destination_seq)
    costs = [[0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)]
    ops = [['0' for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)]
    for i in range(1, len_source_seq + 1):
        costs[i][0] = i * delete_cost
        ops[i][0] = f'D{source_seq[i - 1]}'
    for i in range(1, len_destination_seq + 1):
        costs[0][i] = i * insert_cost
        ops[0][i] = f'I{destination_seq[i - 1]}'
    for i in range(1, len_source_seq + 1):
        for j in range(1, len_destination_seq + 1):
            if source_seq[i - 1] == destination_seq[j - 1]:
                costs[i][j] = costs[i - 1][j - 1] + copy_cost
                ops[i][j] = f'C{source_seq[i - 1]}'
            else:
                costs[i][j] = costs[i - 1][j - 1] + replace_cost
                ops[i][j] = f'R{source_seq[i - 1]}' + str(destination_seq[j - 1])
            if costs[i - 1][j] + delete_cost < costs[i][j]:
                costs[i][j] = costs[i - 1][j] + delete_cost
                ops[i][j] = f'D{source_seq[i - 1]}'
            if costs[i][j - 1] + insert_cost < costs[i][j]:
                costs[i][j] = costs[i][j - 1] + insert_cost
                ops[i][j] = f'I{destination_seq[j - 1]}'
    return (costs, ops)

def assemble_transformation(ops: list[list[str]], i: int, j: int) -> list[str]:
    """Assembles the transformations based on the ops table."""
    if i == 0 and j == 0:
        return []
    elif ops[i][j][0] in {'C', 'R'}:
        seq = assemble_transformation(ops, i - 1, j - 1)
        seq.append(ops[i][j])
        return seq
    elif ops[i][j][0] == 'D':
        seq = assemble_transformation(ops, i - 1, j)
        seq.append(ops[i][j])
        return seq
    else:
        seq = assemble_transformation(ops, i, j - 1)
        seq.append(ops[i][j])
        return seq
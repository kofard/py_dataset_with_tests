"""
A shopkeeper has bags of wheat that each have different weights and different profits.
eg.
profit 5 8 7 1 12 3 4
weight 2 7 1 6  4 2 5
max_weight 100

Constraints:
max_weight > 0
profit[i] >= 0
weight[i] >= 0
Calculate the maximum profit that the shopkeeper can make given maxmum weight that can
be carried.
"""

def calc_profit(profit: list, weight: list, max_weight: int) -> int:
    """Function description is as follows-
    :param profit: Take a list of profits
    :param weight: Take a list of weight if bags corresponding to the profits
    :param max_weight: Maximum weight that could be carried
    :return: Maximum expected gain"""
    if len(profit) != len(weight):
        raise ValueError('The length of profit and weight must be same.')
    if max_weight <= 0:
        raise ValueError('max_weight must greater than zero.')
    if any((p < 0 for p in profit)):
        raise ValueError('Profit can not be negative.')
    if any((w < 0 for w in weight)):
        raise ValueError('Weight can not be negative.')
    profit_by_weight = [p / w for p, w in zip(profit, weight)]
    sorted_profit_by_weight = sorted(profit_by_weight)
    length = len(sorted_profit_by_weight)
    limit = 0
    gain = 0
    i = 0
    while limit <= max_weight and i < length:
        biggest_profit_by_weight = sorted_profit_by_weight[length - i - 1]
        '\n        Calculate the index of the biggest_profit_by_weight in profit_by_weight list.\n        This will give the index of the first encountered element which is same as of\n        biggest_profit_by_weight.  There may be one or more values same as that of\n        biggest_profit_by_weight but index always encounter the very first element\n        only.  To curb this alter the values in profit_by_weight once they are used\n        here it is done to -1 because neither profit nor weight can be in negative.\n        '
        index = profit_by_weight.index(biggest_profit_by_weight)
        profit_by_weight[index] = -1
        if max_weight - limit >= weight[index]:
            limit += weight[index]
            gain += 1 * profit[index]
        else:
            gain += (max_weight - limit) / weight[index] * profit[index]
            break
        i += 1
    return gain
import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)

    return data[field]


def linear_search(sequence, number):
    dict = {"positions":[], "count":0}
    for pos in range(len(sequence)):
        if sequence[pos] == number:
            dict["positions"].append(pos)
            dict["count"] = dict["count"] + 1

    return dict


def pattern_search(sequence, pattern):
    positions = set()
    m = len(pattern)
    n = len(sequence)
    sequence_index = 0

    while sequence_index < n - m:
        pattern_index = 0
        while pattern_index < m:
            if sequence[sequence_index + pattern_index] != pattern[pattern_index]:
                break
            pattern_index = pattern_index + 1
        if pattern_index == m:
            positions.add(sequence_index + m // 2)
        sequence_index = sequence_index + 1

    return positions


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    test_number = 7
    test_sequence = [1, 4, 7]
    search_pattern = "ATA"
    find_number = linear_search(test_sequence, test_number)
    print(find_number)
    with open("sequential.json", mode="r") as file:
        data = json.load(file)
        dna_sequence = data["dna_sequence"]
    result_positions = pattern_search(dna_sequence, search_pattern)
    print(result_positions)

if __name__ == '__main__':
    main()
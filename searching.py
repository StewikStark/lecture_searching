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


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    test_number = 7
    test_sequence = [1, 4, 7]
    find_number = linear_search(test_sequence, test_number)


if __name__ == '__main__':
    main()
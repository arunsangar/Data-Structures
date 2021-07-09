def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            for x in line.split():
                data.append(int(x))
    return data


def print_list(list):
    for i in range(0, len(list)):
        if(i < len(list) - 1):
            print(list[i], end='->')
        else:
            print(list[i])

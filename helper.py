def get_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            for x in line.split():
                data.append(int(x))
    return data

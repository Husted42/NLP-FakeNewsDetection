def read_data(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file:
            values = line.strip().split()
            data.append([float(val) for val in values])
    return data

print(read_data("data.txt")[0]) 

list_of_rows = read_data('data.txt')
# print(list_of_rows[0])

def calc_averages(data):
    n = len(data)
    col1_sum = 0
    col2_sum = 0
    for row in data:
        col1_sum += row[0]
        col2_sum += row[1]
    avg1 = col1_sum / n
    avg2 = col2_sum / n
    return avg1, avg2

col1_avg, col2_avg = calc_averages(list_of_rows)
# print(col1_avg, col2_avg)   

def transpose_data(data):
    transposed = [[] for i in range(len(data[0]))]
    for row in data:
        for i, value in enumerate(row):
            transposed[i].append(value)
    return transposed


list_of_columns = transpose_data(list_of_rows)
# print(list_of_columns[0])
import numpy as np
###### -- Using standart python -- #####
#Read datafile
def read_data(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file:
            values = line.strip().split()
            data.append([float(val) for val in values])
    return data

#Calculate average
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


def transpose_data(data):
    transposed = [[] for i in range(len(data[0]))]
    for row in data:
        for i, value in enumerate(row):
            transposed[i].append(value)
    return transposed

###### -- Using numpy -- #####
#Read datfile into array
def getData(filename):
    data = np.genfromtxt(filename)
    return data

#Calculates the average of each column
def calcAverages(input):
    avg = np.average(input, axis=0)
    return round(avg[0], 4), round(avg[1], 4)

#Changes array of rows into list of columns
def transpose(input):
    array = np.array(input).T
    return array





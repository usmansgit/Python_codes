'''Import math and sqrt from math'''
import math
from math import sqrt


def mean(input_data):
    '''Tis function calculates the mean '''
    n = len(input_data)
    mean = sum(input_data) / n
    return mean


def variance(input_data):
    '''This function calculates variance'''
    n = len(input_data)
    mean = sum(input_data) / n
    dev = [(x - mean) ** 2 for x in input_data]
    variance = sum(dev) / (n - 1)
    return variance


def std(input_data):
    '''This function calculares standerd deviation'''
    var = variance(input_data)
    std = math.sqrt(var)
    return std


def hist(std, mean, input_data):
    '''This function plots the histogram'''
    hist_list = []
    for x in input_data:
        hist_val = float(abs(x - mean))
        hist_list.append(hist_val)

    for category_number in range(0, 6):
        lower_bound = category_number * 0.5 * std
        upper_bound = (category_number + 1) * 0.5 * std
        count = 0
        if lower_bound == 0 and upper_bound == 0:
            print("Deviation is zero.")
            break

        else:
            for i in hist_list:
                if lower_bound <= i < upper_bound:
                    count += 1

            print(f"Values between std. dev. {lower_bound:.2f}-{upper_bound:.2f}: {'*' * count}")


def main():
    print("Enter the data, one value per line.\nEnd by entering empty line.")

    data_list = []
    while True:
        try:
            data = float(input())
        except ValueError:
            break
        data_list.append(data)
    if len(data_list) < 2:
        print("Error: needs two or more values. ")
    else:
        print(f"The mean of given data was: {mean(data_list):.2f}")
        print(f"The standard deviation of given data was: {std(data_list):.2f}")
        hist(std(data_list), mean(data_list), data_list)


if __name__ == "__main__":
    main()
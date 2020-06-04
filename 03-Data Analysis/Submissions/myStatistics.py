# This module defines statistical functions
# Student Name: Ali Al-Musawi
# Student ID: AALMUSAW

def myMax(numberlist):
    greatest = numberlist[0]
    for number in numberlist:
        if number > greatest:
            greatest = number
    return greatest

def myMin(numberlist):
    smallest = numberlist[0]
    for number in numberlist:
        if number < smallest:
            smallest = number
    return smallest

def myAverage(numberlist):
    return sum(numberlist)/len(numberlist)

def myMedian(numberlist):
    m = ((len(numberlist)+1)/2) - 1     #  m is the position of the median data entry
    if abs(m-int(m)) < 0.00000001:      # Check if m is an integer
        m = int(m)
        my_med = sorted(numberlist)[m]
    else:                               # If m is not an integer, then the median is an average
        m = int(m)
        my_med = (sorted(numberlist)[m] + sorted(numberlist)[m+1])/2
    return my_med

def myStandardDeviation(numberlist):
    from math import sqrt
    n = len(numberlist)
    x_bar = myAverage(numberlist)
    x_bar_list = [x_bar]*n
    sq_deviation_list = [0]*n          # This list will contain the squared deviations of each data entry
    for i in range(n):
         sq_deviation_list[i] = (numberlist[i]-x_bar_list[i])**2
    variance = (sum(sq_deviation_list))/(n-1)
    sd = sqrt(variance)
    return sd

def myCountBins(numberlist, binsize):
    n = len(numberlist)
    bincount_list_size = int(myMax(numberlist)/binsize) + 1   # Find the size of the list containing the counts
    bincount_list = [0]*bincount_list_size                    # Create a list to contain the counts
    counter = 0
    for k in range(1, bincount_list_size+1):            # Loop for each entry of the counts list
        for i in range(n):                              # For each data entry, test whether they belong to the kth bin
            if (k-1)*binsize <= sorted(numberlist)[i] < k*binsize:
                counter += 1                            # Count the successes for the kth bin
                bincount_list[k-1] = counter
            else:
                continue                                # numberlist is sorted; there is no point of further testing
        counter = 0                                     # Reset the counter for each kth bin
    return bincount_list

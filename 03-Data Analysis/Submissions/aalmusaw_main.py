# A program for parsing CSV files.
# Student Name: Ali Al-Musawi
# Student ID: AALMUSAW

from myStatistics import *
trial1 = []; trial2 = []; trial3 = []; trial4 = [] # Creating a whole bunch of empty lists to store data
try:
    file = input('Please enter the file name to analyze: ')
    infile = open(file, 'r')
    for line in infile:     # Cleaning the file and extracting the appropriate data into respective lists.
        if line.startswith('trial1'):
            line = line.replace("trial1 ", "")
            trial1.append(float(line))
        elif line.startswith('trial2'):
            line = line.replace("trial2 ", "")
            trial2.append(float(line))
        elif line.startswith('trial3'):
            line = line.replace("trial3 ", "")
            trial3.append(float(line))
        elif line.startswith('trial4'):
            line = line.replace("trial4 ", "")
            trial4.append(float(line))
        else:
            pass
    infile.close()
except NameError:   # In case the user messes up by opening a non-existent file
    print('Sorry. The file ', file, ' is not available.')

trials = [trial1, trial2, trial3, trial4]   # Creating more lists to take advantage of loops to automate the work.
outfiles = [open('trial1-data-analysis.txt', 'w'), open('trial2-data-analysis.txt', 'w'),\
            open('trial3-data-analysis.txt', 'w'), open('trial4-data-analysis.txt', 'w')]
for file in range(4):
    outfiles[file].writelines('minimum  : %5.5f\n' %myMin(trials[file]))
    outfiles[file].writelines('maximum  : %5.5f\n' %myMax(trials[file]))
    outfiles[file].writelines('average  : %5.5f\n' %myAverage(trials[file]))
    outfiles[file].writelines('median   : %5.5f\n' %myMedian(trials[file]))
    outfiles[file].writelines('std_dev  : %5.5f\n' %myStandardDeviation(trials[file]))
    outfiles[file].writelines('bin_count: {}\n'.format(myCountBins(trials[file], 25)))
    outfiles[file].close() #I CLOSED THE FILES IN THE LOOP :-)


#!/usr/bin/env python

#########################################
# Mattia Corradi - Dalla Chiara Michele #
#########################################

import subprocess
import os
import sys

print(sys.argv)

file_result = 'result.log'

matching_file = sys.argv[2]
input_file = sys.argv[1]

try:
     os.remove(file_result)
except OSError:
     pass

subprocess.call(['./runTestOnSis.sh', input_file])

watt = [0, 0, 0, 2000, 300, 1200, 1000, 2000, 1800, 240, 400, 200, 400]


try:
    infile = open(file_result, 'r')
except:
    print("File {} non trovato (File generato usando il file di test fornito dal prof)".format(file_result))

try:
    matchingFile = open(matching_file, 'r')
except:
    print("File {} non trovato (File di verifica fornito dal prof)".format(matching_file))

try:
    inputFile = open(input_file, 'r')
except:
    print("File {} non trovato (File di verifica fornito dal prof)".format(input_file))


results = []
for line in infile:
    app = line.strip().split()

    if len(app) > 0:

        if app[0] == "Outputs:":
            del app[0]
            results.append(app)

matching = []

for line in matchingFile:
    app = line.strip().split()
    matching.append(app)

inputArray = []
for line in inputFile:
    app = line.strip().split()
    del app[0]
    inputArray.append(app)

del inputArray[0]

bad = 0
ok = 0
tot = len(results)
totWatt = 0

for i in range(0, tot):

    if matching[i] == results[i]:
        print('{}) ok'.format(i+1))
        print('input  {}'.format(inputArray[i]))
        print('ris    {}'.format(results[i]))
        ok += 1
    else:
        for j in range(0, len(inputArray[i])):
            if inputArray[i][j] == '1':
                totWatt += watt[j]
        bad += 1

        print('{}) bad'.format(i + 1))
        print('watt tot = {}'.format(totWatt))
        print('input  {}'.format(inputArray[i]))
        print('tuo    {}'.format(results[i]))
        print('prof   {}'.format(matching[i]))

        totWatt = 0



print('\nOK {}/{}'.format(ok, tot))
print('BAD {}/{}'.format(bad, tot))
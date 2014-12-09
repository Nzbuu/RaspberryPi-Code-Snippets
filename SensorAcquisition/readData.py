import csv
import json

# Read Text File
time = []
data = []
with open('Thermistor.txt', 'r') as f:
    # next(f) # skip headings
    reader=csv.reader(f, delimiter='\t')

    for timeStamp, datum in reader:
        time.append(timeStamp)
        data.append(datum)

time = [float(t) for t in time]
timeStart = time[0]
time = [(t - timeStart)/3600 for t in time]
data = [float(d) for d in data]

sample = {'time': time, 'temperature': data}

arrayOfObjects = [{'time': t, 'temperature': d} for t, d in zip(time,data)]


print(len(data))
print(len(time))
f.close()


with open('data.js', 'w') as fp:
    fp.write('var lineData = \n')
    json.dump(arrayOfObjects, fp, sort_keys=True, indent=4, separators=(',', ': '))
    fp.close()
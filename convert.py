import numpy as np
import mne,sys
from os import listdir
from os.path import isfile, join


files = [f for f in listdir('tmp/') if isfile(join('tmp/', f))]
files.sort()

print(files)

tot = []
channels = [[],[],[],[],[],[],[],[]]
channel_names = []

for file in files:
    segment = int(file.split('.')[0])
    channel = int(file.split('.')[1].split(' ')[0])
    name = file.split(' ')[2]

    print(str(segment) + ' ' + str(channel) + ' '+ name)
    if channel <= 8:
        if len(channels[channel-1]) == 0:
            channel_names.append(name)

        data = np.loadtxt('tmp/'+file, delimiter=',')
        data = np.transpose(data)
        channels[channel-1].extend(data)
        
        
for channel in channels:
    print(len(channel))
    


# Read the CSV file as a NumPy array

# Some information about the channels
#ch_names = ['CH 1', 'CH 2', 'CH 3', 'CH 4', 'CH 5', 'CH 6','CH 7', 'CH 8', 'CH 9']  # TODO: finish this list

# Sampling rate of the Nautilus machine
sfreq = 500  # Hz

# Create the info structure needed by MNE
info = mne.create_info(channel_names, sfreq)

# Finally, create the Raw object
raw = mne.io.RawArray(channels, info)

# Plot it!
fname = sys.argv[1]
mne.export.export_raw(fname, raw)
raw.plot()
input("wait")
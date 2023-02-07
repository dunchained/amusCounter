from glob import glob
from collections import Counter
import pandas

file_list = glob('input/*.txt')
song_list = []
for item in file_list:
    with open(item, 'rb') as f:
        data = f.readlines()
        for line in data:
            strip_line = line.decode("cp1255")[8:]
            strip_line2 = strip_line[:-2]
            song_list.append(strip_line2)
           
counter = dict(Counter(song_list))
zapis = pandas.DataFrame(data=counter, index=[0])
zapis = zapis.T
zapis.to_excel('prebrojano.xlsx', index=[0])
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
            song_list.append(strip_line)
           
print(song_list) 
#counter = dict(Counter(song_list))
#print(counter)

# zapis = pandas.DataFrame(data=counter)
# zapis = zapis.T
# zapis.to_excel('prebrojano.xlsx', index=[0])
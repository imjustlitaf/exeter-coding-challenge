import tracemalloc          #for checking the amount of memory used
import pandas               #for processing csv files
import time                 #for calculating the total time taken by the program to finish its execution

start = time.time()

tracemalloc.start()

word_li = list()            #store the words to be found

for i in open("C:\\Users\\sivad\\Downloads\\TranslateWordsChallenge\\find_words.txt"):
  word_li.append(i.strip().split('\n'))             #strip the extra spaces that precede and succede, and store the data by splitting it at the new line



french_dict = pandas.read_csv("C:\\Users\\sivad\\Downloads\\TranslateWordsChallenge\\french_dictionary.csv", header=None) #load the dictionary file

main_dict = dict(zip(french_dict[0].to_list(), french_dict[1].to_list())) #convert the csv file to a dict type 

with open("C:\\Users\\sivad\\Downloads\\TranslateWordsChallenge\\t8.shakespeare.txt", "r") as f:
  txt_file = f.read()                   #read the text file to be processed

replaced_words = []                     #store the words that are replaced
frequency_words = []                    #store the frequency of the words that are replaced


for i in word_li:
  frequency_words.append(txt_file.count(i[0]))              #append the frequency of each word to be replaced
  replaced_words.append(i[0])                               #append the word to be replaced
  txt_file = txt_file.replace(i[0], main_dict[i[0]])        #replace the word inside the text file

#find the total number of words replaced
c = 0
l = len(frequency_words)
for i in range(l):
  if frequency_words[i] > 0:
    c += 1
print("number of words replaced: ", c)

#store the translated text file
text_file = open("C:\\Users\\sivad\\Downloads\\TranslateWordsChallenge\\t8.shakespeare.translated.txt", "w")
text_file.write(" %s " % txt_file)
text_file.close()

#create a list with the english word, its french equivalent and its frequency
Dict=[{'English word':e, 'French word':f, 'Frequency':freq} for e,f,freq in zip(french_dict[0].to_list(), french_dict[1].to_list(),frequency_words)]
#create a dataFrame with the three prescribed columns
df = pandas.DataFrame (Dict, columns = ['English word','French word','Frequency'])
#store the dataframe as csv
df.to_csv("C:\\Users\\sivad\\Downloads\\TranslateWordsChallenge\\frequency.csv", index=None)

l = len(df)
#find the unique number of words replaced
unique_li = []
for i in range(l):
    if df['Frequency'][i] > 0:
        unique_li.append(df['English word'][i])
print(unique_li)

end = time.time()

total_time = round(end-start)

current, peak = tracemalloc.get_traced_memory()

current = round(current/1024)

print("total time: ", total_time)

print("memory used: ", current/1024, "kB")

s1 = "Time to process: " + str(total_time) + " seconds\n"

s2 = "Memory used: " + str(current) + " kB"

with open("C:\\Users\\sivad\\Downloads\\TranslateWordsChallenge\\performance.txt", "w") as f:
    f.write(s1)
    f.write(s2)
import csv


# read file as separate line without newline and add "key" to keystroke_lines
addme = "key"
with open("logs/keyfreq_1536361200.txt") as f:
    keystroke_lines = [''.join([x.strip(), addme])for x in f.read().splitlines()]

with open("logs/window_1536361200.txt") as f:
    window_lines = f.read().splitlines()

# merge both files
keystroke_lines.extend(window_lines)

# sort according to timestamp
keystroke_lines.sort()

# find next k
k_index = []
w_index = []
i = 0
for line in keystroke_lines:
    if(line[len(line)-3:len(line)]=="key"):
        k_index.append(i)
    else:
        w_index.append(i)
    i+=1

# curr_k_index = k_index.index(w_index[0]+1)
# first_k = keystroke_lines[first_k_index]
# print(first_k_index)
# print(first_k)


with open('training.csv','w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Timestamp", "Category", "Keystrokes"])
    curr_k_index = 0
    for i in range (0,len(w_index)-1):
        # get activity from w line
        curr_w_line = keystroke_lines[w_index[i]]
        try:
            activity = curr_w_line[11:curr_w_line.index(":")-1]
            #print(activity)
        except ValueError:
            activity = curr_w_line[11:len(curr_w_line)-1]
            #print(activity)

        # seperate activity according to category

        if(w_index[i+1] == (w_index[i]+1)):
            print(i)
            # active window change without keystroke logging in between
            # as long as either window is work , we will take that
            # otherwise take the first one's category
        else:
            try:
                while (k_index[curr_k_index] > w_index[i] and k_index[curr_k_index] < w_index[i+1]):
                    #take
                    curr_k_line = keystroke_lines[k_index[curr_k_index]]
                    timestamp = curr_k_line[0:9]
                    keystrokes = curr_k_line[len(curr_k_line)-6:len(curr_k_line)-3].lstrip()
                    print(timestamp)
                    filewriter.writerow([timestamp, activity, keystrokes])
                    # increase curr_k_index
                    curr_k_index +=1
            except IndexError:
                print("index out of bounds")
                # add keystroke_lines[w_index[i]] activity




#print(w_index)

# break for each

 # with open('training.csv','wb') as csvfile:
 #    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
 #    filewriter.writerow(["Timestamp", "Category", "Keystrokes"])
 #    current=0
 #    for line in lines:
 #        timestamp = line[0:9]
 #
 #        keystrokes = line[len(line)-3:len(line)].lstrip()
 #
 #        filewriter.writerow(["Timestamp", "Category", "Keystrokes"])

from data_set import Reading

################### use this for training #####################
data = []
###############################################################

################### use this for testing ######################
test = []
###############################################################


####################### constants #############################
length = 0
width = 1
size = 2
conc = 3
conc1 = 4
asym = 5
m3long = 6
m3trans = 7
alpha = 8
dist = 9
classification = 10
##############################################################


def read_data():
    f = open("train.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        split = line.split(",")
        reader = Reading(split[0], split[1], split[2], split[3], split[4], split[5], split[6], split[7], split[8],
                         split[9], split[10].replace("\n", ""))
        data.append(reader)
    f.close()

    f = open("test.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        split = line.split(",")
        reader = Reading(split[0], split[1], split[2], split[3], split[4], split[5], split[6], split[7], split[8],
                         split[9], split[10].replace("\n", ""))
        test.append(reader)
    f.close()

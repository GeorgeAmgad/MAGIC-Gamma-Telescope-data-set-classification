from data_set import Reading

################### use this for training #####################
data = []
###############################################################

################### use this for testing ######################
test = []
###############################################################


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

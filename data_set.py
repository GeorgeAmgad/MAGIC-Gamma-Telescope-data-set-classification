import random

################### use this for random training #####################
training_data = []  # pure training data
######################################################################

################### use this for random testing ######################
testing_data = []  # testing data
######################################################################


class Reading:
    def __init__(self, length, width, size, conc, conc1, asym, m3long, m3trans, alpha, dist, classi):
        self.length = length
        self.width = width
        self.size = size
        self.conc = conc
        self.conc1 = conc1
        self.asym = asym
        self.m3long = m3long
        self.m3trans = m3trans
        self.alpha = alpha
        self.dist = dist
        self.classi = classi


f = open("magic04.data", "r")
raw_data = []
counter = 0
while True:
    line = f.readline()
    if not line:
        break
    split = line.split(",")
    reader = Reading(split[0], split[1], split[2], split[3], split[4], split[5], split[6], split[7], split[8], split[9],
                     split[10].replace("\n", ""))
    raw_data.append(reader)
    counter += 1

print("total number of data =", counter)

num_of_g = 0
num_of_h = 0

list_of_g = []  # split the Gs to randomly trim from them
list_of_h = []

for reading in raw_data:
    if reading.classi == "g":
        list_of_g.append(reading)
        num_of_g += 1
    else:
        list_of_h.append(reading)
        num_of_h += 1


print("number of Gs =", num_of_g)
print("number of Hs =", num_of_h)

random.shuffle(list_of_g)  # shuffle the list to trim randomly

all_data = []  # all of the -ready to use- data

for i in range(num_of_h):  # iterate in list of Gs till the number of Hs is reached ( balancing )
    all_data.append(list_of_g[i])

for reading in list_of_h:
    all_data.append(reading)

random.shuffle(all_data)  # shuffle the data to extract testing data randomly

print("total number of filtered data =", len(all_data))


for i in range((70 * len(all_data)) // 100):
    reading = all_data.pop()
    training_data.append(reading)

testing_data = all_data.copy()  # save the rest for testing

f.close()

########################### uncomment this code to edit/create different testing data #################################

# f = open("train.txt", "w+")
# for reading in training_data:
#     f.write(
#         reading.length + ',' + reading.width + ',' + reading.size + ',' + reading.conc + ',' + reading.conc1 + ',' +
#         reading.asym + ',' + reading.m3long + ',' + reading.m3trans + ',' + reading.alpha + ',' + reading.dist + ',' +
#         reading.classi + '\n')
#
# f.close()
#
# f = open("test.txt", "w+")
# for reading in testing_data:
#     f.write(
#         reading.length + ',' + reading.width + ',' + reading.size + ',' + reading.conc + ',' + reading.conc1 + ',' +
#         reading.asym + ',' + reading.m3long + ',' + reading.m3trans + ',' + reading.alpha + ',' + reading.dist + ',' +
#         reading.classi + '\n')
#
# f.close()


######################################################################################################################

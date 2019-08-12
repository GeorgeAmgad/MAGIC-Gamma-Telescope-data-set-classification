import random

################### use this for random training #####################
training_data = []
######################################################################

################### use this for random testing ######################
testing_data = []
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

random.shuffle(list_of_g)  # shuffle the list to trim randomly

all_data = []  # all of the -ready to use- data

for i in range(num_of_h):  # iterate in list of Gs till the number of Hs is reached ( balancing )
    all_data.append(list_of_g[i])

for reading in list_of_h:
    all_data.append(reading)

random.shuffle(all_data)  # shuffle the data to extract testing data randomly

for i in range((70 * len(all_data)) // 100):
    reading = all_data.pop()
    training_data.append(reading)

testing_data = all_data.copy()  # save the rest for testing

f.close()


########################### uncomment this code to edit/create different testing data #################################

# f = open("all_data.txt", "w+")
# for reading in all_data:
#     f.write(
#         reading.length + ',' + reading.width + ',' + reading.size + ',' + reading.conc + ',' + reading.conc1 + ',' +
#         reading.asym + ',' + reading.m3long + ',' + reading.m3trans + ',' + reading.alpha + ',' + reading.dist + ',' +
#         reading.classi + '\n')
#
# f.close()

# f = open("test.txt", "w+")
# for reading in testing_data:
#     f.write(
#         reading.length + ',' + reading.width + ',' + reading.size + ',' + reading.conc + ',' + reading.conc1 + ',' +
#         reading.asym + ',' + reading.m3long + ',' + reading.m3trans + ',' + reading.alpha + ',' + reading.dist + ',' +
#         reading.classi + '\n')
#
# f.close()


######################################################################################################################

def convert_to_array(readings):
    array = []
    for x in range(len(readings)):
        a_line = [readings[x].length, readings[x].width, readings[x].size, readings[x].conc, readings[x].conc1,
                  readings[x].asym, readings[x].m3long, readings[x].m3trans, readings[x].alpha, readings[x].dist,
                  readings[x].classi]
        array.append(a_line)

    return array


def array_of_element_n(data, n):
    array = []
    for values in data:
        array.append(values[n])
    return array


def encode_target(df, target_column):
    """Add column to df with integers for the target.

    Args
    ----
    df -- pandas DataFrame.
    target_column -- column to map to int, producing
                     new Target column.

    Returns
    -------
    df_mod -- modified DataFrame.
    targets -- list of target names.
    """
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return df_mod, targets

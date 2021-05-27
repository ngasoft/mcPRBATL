import itertools
from itertools import permutations
numberOfAgents = int(input("Enter the numebr of agents: "))
numberOfResources = 2  # int (input("Enter the numebr of resources: "))
# Probability assigned
# p = 1/(3*numberOfAgents)
p = 0.99 / (numberOfAgents * numberOfAgents)
q = 0.88 / (numberOfAgents * numberOfAgents)
r = 0.77 / (numberOfAgents * numberOfAgents)
# print(p)

numberOfStates = int(7 + numberOfAgents)
loopIndex = int(numberOfStates + 1)
action = list(itertools.product([1, 2], repeat=numberOfAgents))

f = open(str(numberOfAgents) + "-agents-example.model", "w")


def initial_structure(numberOfAgents):
    f.write("Structure Example" + str(numberOfAgents) + " = {")
    f.write("\n")
    # f.write(str(numberOfAgents))
    f.write(str(numberOfAgents) + ", # number of agents")
    f.write("\n")
    f.write(str(numberOfResources) + ", # number of resources")
    f.write("\n")

def system_states(loopIndex):
    for x in range(loopIndex - 1):
        if x == 0:
            f.write("{q" + str(x) + ",")
        elif x == loopIndex - 2:
            f.write("q" + str(x) + "}, # states")
        else:
            f.write("q" + str(x) + ",")
    # print("q%d" % (x),  end = ',')

def labelling_function(numberOfAgents):
    f.write("\n")
    f.write("{lowburnt,mediumburnt,highburnt,completelyburnt}, #propositions")
    f.write("\n")
    f.write("{ #Labelling function")
    f.write("\n")
    f.write("lowburnt -> {q" + str(numberOfAgents + 1) + "},")
    f.write("\n")
    f.write("mediumburnt -> {q" + str(numberOfAgents + 3) + "},")
    f.write("\n")
    f.write("highburnt -> {q" + str(numberOfAgents + 5) + "},")
    f.write("\n")
    f.write("completelyburnt -> {q" + str(numberOfAgents + 6) + "}")
    f.write("\n")
    f.write("},")
    f.write("\n")


def available_function(loopIndex, numberOfAgents):
    f.write("{ #Available function")
    f.write("\n")
    for x in range(loopIndex - 1):
        if x <= numberOfAgents:
            for y in range(numberOfAgents):
                f.write("(q" + str(x) + "," + str(y + 1) + ") -> 2,")
                f.write("\n")

        elif (x == numberOfAgents + 2) or (x == numberOfAgents + 4):
            for y in range(numberOfAgents):
                f.write("(q" + str(x) + "," + str(y + 1) + ") -> 2,")
                f.write("\n")

        else:
            for y in range(numberOfAgents):
                if (x == loopIndex - 2) and (y == numberOfAgents - 1):
                    f.write("(q" + str(x) + "," + str(y + 1) + ") -> 1")
                    f.write("\n")
                else:
                    f.write("(q" + str(x) + "," + str(y + 1) + ") -> 1,")
                    f.write("\n")

    f.write("},")
    f.write("\n")


def costing_function(loopIndex, numberOfAgents):
    f.write("{ #Costing function")
    f.write("\n")

    for x in range(loopIndex - 1):
        if x == 0:
            for y in range(numberOfAgents):
                f.write("(q" + str(x) + "," + str(y + 1) + "," + str(2) + ") -> (0,1),")
                f.write("\n")

        elif (x <= numberOfAgents) or (x == numberOfAgents + 2):
            for y in range(numberOfAgents):
                f.write("(q" + str(x) + "," + str(y + 1) + "," + str(2) + ") -> (1,1),")
                f.write("\n")

        elif (x == numberOfAgents + 4):
            for y in range(numberOfAgents):
                if (y == numberOfAgents - 1):
                    f.write("(q" + str(x) + "," + str(y + 1) + "," + str(2) + ") -> (1,1)")
                    f.write("\n")
                else:
                    f.write("(q" + str(x) + "," + str(y + 1) + "," + str(2) + ") -> (1,1),")
                    f.write("\n")

    f.write("},")
    f.write("\n")



def transitions_from_the_initial_state(numberOfAgents, numberOfStates):
    f.write("{ #Transition function")
    f.write("\n")
    f.write("#transitions from the initial state")
    f.write("\n")
    for y in range(numberOfAgents + 1):
        for x in action:
            if (x.count(2) == y) and (y == 0):
                f.write("(q0," + str(x) + ") -> {q" + str(numberOfStates - 1) + ":1.0},")
                f.write("\n")
            elif x.count(2) == y:
                f.write("(q0," + str(x) + ") -> {q" + str(y) + ":1.0},")
                f.write("\n")


def transitions_from_the_sensed_low_fire_states(numberOfAgents, p):
    f.write("#transitions from the low fire detected states")
    f.write("\n")
    for y in range(numberOfAgents):
        #f.write("i am here\n")
        # if y!=0:
        # q = q + 0.2475
        # else:
        # q = p
        #f.write("PRINTING q :" + str(q))
        for z in range(numberOfAgents + 1):
            #f.write("\n i am then here\n")
            # if p < 1:
            #    p = p + 0.07
            for x in action:
                if (x.count(2) == z) and (z == 0):
                    f.write("(q" + str(y + 1) + "," + str(x) + ") -> {q" + str(numberOfAgents + 2) + ":1.0},")
                    f.write("\n")
                elif x.count(2) == z:
                    f.write("(q" + str(y + 1) + "," + str(x) + ") -> {q" + str(numberOfAgents + 1) + ":" + str(
                        round(p, 2)) + ", q" + str(numberOfAgents + 2) + ":" + str(round(1 - p, 2)) + "},")
                    f.write("\n")
                    #f.write("i am at the end\n")
                    # q = q + 0.2475
            if (z != 0):
                p = p + 0.99 / (numberOfAgents * numberOfAgents)
            #f.write("\n Then PRINTING q :" + str(q))
            f.write("\n")


def transitions_for_the_rest_of_the_states(numberOfStates, q, r):
    f.write("#transitions for the rest of the states")
    f.write("\n")
    #for y in range(numberOfStates - 1, 0, -1):
    for y in range(numberOfStates):
        if (y == numberOfAgents + 2):

            for z in range(numberOfAgents + 1):
                # r = q + z * 0.1
                for x in action:
                    if (x.count(2) == z) and (z == 0):
                        f.write("(q" + str(y) + "," + str(x) + ") -> {q" + str(y + 2) + ":1.0},")
                        f.write("\n")
                    elif x.count(2) == z:
                        f.write(
                            "(q" + str(y) + "," + str(x) + ") -> {q" + str(y + 1) + ":" + str(
                                round(q, 2)) + ", q" + str(
                                y + 2) + ":" + str(round(1 - q, 2)) + "},")
                        f.write("\n")
                if z != 0:
                    q = q + + 0.88 / (numberOfAgents * numberOfAgents)

        elif (y == numberOfAgents + 4):

            for z in range(numberOfAgents + 1):
                # r = q + z * 0.1
                for x in action:
                    if (x.count(2) == z) and (z == 0):
                        f.write("(q" + str(y) + "," + str(x) + ") -> {q" + str(y + 2) + ":1.0},")
                        f.write("\n")
                    elif x.count(2) == z:
                        f.write(
                            "(q" + str(y) + "," + str(x) + ") -> {q" + str(y + 1) + ":" + str(
                                round(r, 2)) + ", q" + str(
                                y + 2) + ":" + str(round(1 - r, 2)) + "},")
                        f.write("\n")
                if z != 0:
                    r = r + + 0.77 / (numberOfAgents * numberOfAgents)


        elif y > numberOfAgents:
            for x in action:
                if (x.count(2) == 0) and (y == numberOfStates - 1):
                    f.write("(q" + str(y) + "," + str(x) + ") -> {q" + str(y) + ":1.0}")
                    f.write("\n")
                elif (x.count(2) == 0):
                    f.write("(q" + str(y) + "," + str(x) + ") -> {q" + str(y) + ":1.0},")
                    f.write("\n")

    f.write("}")
    f.write("\n")
    f.write("}")


initial_structure(numberOfAgents)
system_states(loopIndex)
labelling_function(numberOfAgents)
available_function(loopIndex, numberOfAgents)
costing_function(loopIndex, numberOfAgents)
transitions_from_the_initial_state(numberOfAgents, numberOfStates)
transitions_from_the_sensed_low_fire_states(numberOfAgents, p)
transitions_for_the_rest_of_the_states(numberOfStates,q,r)

f.close()

# open and read the file after the appending:
f = open(str(numberOfAgents) + "-agents-example.model", "r")
print(f.read())

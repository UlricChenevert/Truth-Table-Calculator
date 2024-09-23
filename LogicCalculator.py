'''
Logic Calculator

'''

def determineTestValue(iteration, bit_position):
    # value changes every changeRate position
    changeRate = 2**bit_position
    completeIterationSize = changeRate*2

    return iteration % completeIterationSize >= changeRate


def printLogic(result, variables):
    print("| ", end="")

    for variable in variables:
        print(f"{int(variable)} | ", end="")
    
    print(f"{int(result)} |")

def printHeader(numberOfVariables):
    print("| ", end="")

    for variable_index in range(numberOfVariables):
        print(f"{chr(variable_index + 65)} | ", end="")

    print("F | ")
    print("-"*((numberOfVariables + 1)*4 + 2))


def testLogic(numberOfVariables, func):
    truthTableSize = numberOfVariables**2
    logicalVariables = [0] * numberOfVariables # Array of size numberOfVariables

    printHeader(numberOfVariables)

    for row_iteration in range(truthTableSize):
        
        # Determine variable values
        for variable_index in range(len(logicalVariables)):
            logicalVariables[variable_index] = determineTestValue(row_iteration, numberOfVariables - variable_index - 1)
            

        printLogic(func(logicalVariables), logicalVariables)


logicalFunction = lambda variables : (( variables[2] ) | ( not(variables[0]) and not(variables[1]) ) | ( not(not(variables[1]) or variables[2]) ))

logicalFunction = lambda variables : variables[0] or variables[1]
testLogic(2, logicalFunction)
print()

logicalFunction = lambda variables : not(not variables[0] and not variables[1])
testLogic(2, logicalFunction)
print()

logicalFunction = lambda variables : not variables[0] and not variables[1]
testLogic(2, logicalFunction)
print()
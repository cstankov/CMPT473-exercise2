import os
import io
import filecmp
 

inputPath = 'TestData/TestFiles/'
expectedOutputPath = 'TestData/ExpectedOutput/'
expectedMessagePath = 'TestData/ExpectedMessages/'
outputPath = 'TestOutput/Files/'
outputMessagePath = 'TestOutput/Messages/'

testName1 = "Numeric and boolean values included with -d option and file is tab separated for a non empty file."
testName2 = "Numeric and boolean values included with -s option and file is comma separated for a non empty file."
testName3 = "Both -d and -s options and file is separated with tabs for a non empty file."
testName4 = "No options and file is spearated with commas for a non empty file. However invalid input and output path"
testName5 = "Numeric and boolean values not included with option -d and file is separated with comas for a non empty file."
testName6 = "Empty file."
testName7 = "Invalid input path"
testName8 = "Invalid output path"

def createInputPath(testNum):
    inputFile = "testCase" + str(testNum) + ".csv"
    return (inputPath + inputFile)

def createExpectedOutputPath(testNum):
    expectedOutputFile = "expectedOutput" + str(testNum) + ".json"
    return expectedOutputPath + expectedOutputFile

def createExpectedMessagePath(testNum):
    expectedMessageFile = "expectedMessage" + str(testNum) + ".txt"
    return expectedMessagePath + expectedMessageFile

def createOutputPath(testNum):
    outputFile = "testCase" + str(testNum) + "Output.json"
    return outputPath + outputFile

def createMessageOutputPath(testNum):
    messageOutputFile = "messageOut-" + str(testNum) + ".txt" 
    return outputMessagePath + messageOutputFile 

def createCommandLineArgForTest(inputFilePath, outputFilePath, d_flag, s_flag):
    commandLineArg = 'csv2json ' + inputFilePath + ' ' + outputFilePath
    if(d_flag == True):
        commandLineArg = 'csv2json -d ' + inputFilePath + ' ' + outputFilePath   
    elif (s_flag ==True):
        commandLineArg = 'csv2json -s "\t"' + inputFilePath + ' ' + outputFilePath
    print(commandLineArg + '\n')
    return commandLineArg
 
def runCommandLineIfValid(commandLineArg, inputFilePath, outputFilePath, messageOutputFilePath, expectedMessagePath):
    validPath = False
    if os.path.exists(inputFilePath) == False:
        message = 'Error: Invalid input file path'
        print("Message - " + message)
        with open(messageOutputFilePath, 'w') as file:
            file.write((message + '\n\n'))
    elif os.path.exists(outputFilePath) == False:
        message = 'Error: Invalid output file path'
        print("Message - " + message)
        with open(messageOutputFilePath, 'w') as file:
            file.write((message + '\n\n'))
    else:
        os.system(commandLine)
        validPath = True

    return validPath
 
def compareFiles(outputFilePath, expectedOutputFilePath, messageOutputFilePath):
    outMsg = pathOutputMessage + testFileName('message.txt')
 
    commandLine = 'diff ' + outputFilePath + ' ' + expectedOutputFilePath
    print(commandLine + '\n')
    os.system(commandLine)
 
    msg = ""
    if filecmp.cmp(outputFilePath, expectedOutputFilePath):
        msg = 'Output and Expected Files Match'
    else:
        msg = 'Output and Expected Files DO NOT Match'
 
    print('message: ' + msg)
    with open(messageOutputFilePath, 'w') as file:
            file.write((commandLine + '\n\n')) 
            file.write((msg + '\n\n'))  
 
    print('\nMessage saved to ' + messageOutputFilePath)
    return
 
def compareMessages(testNum, messageOutputFilePath, expectedMessagePath):
    commandLineArg = '\ndiff ' + messageOutputFilePath + ' ' + expectedMessagePath
    os.system(commandLineArg)
 
    if filecmp.cmp(messageOutputFilePath, expectedMessagePath):
        msg = 'Test ' + str(testNum) + ' Passed: Output message matched the expected out message.'
    else:
        msg = 'Test ' + str(testNum) + ' Failed: Output message did not match the expected out message.'
 
    print(msg)
    return

def runTest(testNum, testName, inputFile, outputFile, d_flag = False, s_flag = False):
    print('Running Test: ' + str(testNum) + ' - ' + testName + "\n")
    inputFilePath = createInputPath(testNum)
    expectedOutputFilePath = createExpectedOutputPath(testNum)
    expectedMessagePath = createExpectedMessagePath(testNum)
    outputFilePath = createOutputPath(testNum)
    messageOutputFilePath = createMessageOutputPath(testNum)

    commandLineArg = createCommandLineArgForTest(inputFilePath, outputFilePath, d_flag, s_flag)

    with open(messageOutputFilePath, 'w') as file:
        file.write((commandLineArg + '\n\n'))

    validPath = runCommandLineIfValid(commandLineArg, inputFilePath, outputFilePath, messageOutputFilePath, expectedMessagePath)
    
    if validPath:
        compareFiles(outputFilePath, expectedOutputFilePath, messageOutputFilePath)
    compareMessages(testNum, messageOutputFilePath, expectedMessagePath)
 
 
def runAllTests():
    print("ACTS TESTING OF CSV2JSON PROGRAM")   
    print("=================================\n")
    #test case 1
    runTest(1, testName1, "testCase1.csv", "testCase1Output.json", d_flag=True)
    #test case 2
    runTest(2, testName2, "testCase2.csv", "testCase2Output.json", s_flag=True)
    #test case 3
    runTest(3, testName3, "testCase3.csv", "testCase3Output.json", d_flag=True, s_flag=True)
    #test case 4
    runTest(4, testName4, "testCase4.csv", "testCase4Output.json")
    #test case 5
    runTest(5, testName5, "testCase5.csv", "testCase5Output.json", d_flag=True)
    #test case 6
    runTest(6, testName6, "testCase6.csv", "testCase6Output.json")
    #test case 7
    runTest(7, testName7, "testCase7.csv", "testCase7Output.json")
    #test case 8
    runTest(8, testName8, "testCase8.csv", "testCase8Output.json")

if __name__ == "__main__":
    runAllTests()

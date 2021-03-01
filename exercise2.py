import os
import io
import filecmp


inputPath = 'TestData/TestFiles/'
expectedOutputPath = 'TestData/ExpectedOutput/'
expectedMessagePath = 'TestData/ExpectedMessages/'
outputPath = 'TestOutput/Files/'
outputMessagePath = 'TestOutput/Messages/'

testName1 = "Numeric and boolean values and file is comma separated for a non empty record."
testName2 = "Both -d and -s options and file is separated with commas for a non empty record."
testName3 = "Numeric and boolean values with and both -d and -t options and file is separated with tabs for a non empty record."
testName4 = "option -s and file is separated with tabs for a non empty record."
testName5 = "Empty file."
testName6 = "Numeric and boolean values with option -s file is separated with commas for a non empty record."
testName7 = "Invalid input path"
testName8 = "Invalid output path"
testName9 = "Option -t and file is separated with commas for a non empty record."

def createInputPath(testNum, inputFile):
    return (inputPath + inputFile)

def createExpectedOutputPath(testNum):
    expectedOutputFile = "expectedOutput" + str(testNum) + ".json"
    return expectedOutputPath + expectedOutputFile

def createExpectedMessagePath(testNum):
    expectedMessageFile = "expectedMessage" + str(testNum) + ".txt"
    return expectedMessagePath + expectedMessageFile

def createOutputPath(testNum, outputFile):
    return outputPath + outputFile

def createMessageOutputPath(testNum):
    messageOutputFile = "messageOut-" + str(testNum) + ".txt" 
    return outputMessagePath + messageOutputFile 

def createCommandLineArgForTest(inputFilePath, outputFilePath, d_flag, s_flag, t_flag):
    commandLineArg = 'csv2json ' + inputFilePath + ' ' + outputFilePath
    options = ""
    if(d_flag == True):
        options += " -d "
    if (s_flag ==True):
        options += " -s ' ' "
    if (t_flag == True):
        options += " -t "
    commandLineArg = 'csv2json'+ options + inputFilePath + ' ' + outputFilePath
    return commandLineArg
 
def runCommandLineIfValid(commandLineArg, inputFilePath, outputFilePath, messageOutputFilePath, expectedMessagePath):
    validPath = False
    if os.path.exists(inputFilePath) == False:
        message = 'Error: Invalid input file path'
        with open(messageOutputFilePath, 'a') as file:
            file.write((message + '\n\n'))
    elif os.path.exists(outputFilePath) == False:
        message = 'Error: Invalid output file path'
        with open(messageOutputFilePath, 'a') as file:
            file.write((message + '\n\n'))
    else:
        os.system(commandLineArg)
        validPath = True

    return validPath
 
def compareFiles(outputFilePath, expectedOutputFilePath, messageOutputFilePath):
    commandLine = 'diff ' + outputFilePath + ' ' + expectedOutputFilePath
    os.system(commandLine)
 
    msg = ""
    if filecmp.cmp(outputFilePath, expectedOutputFilePath):
        msg = 'Output and Expected Files Match'
    else:
        msg = 'Output and Expected Files DO NOT Match'
 
    with open(messageOutputFilePath, 'a') as file:
            file.write((commandLine + '\n\n')) 
            file.write((msg + '\n\n'))  
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

def runTest(testNum, testName, inputFile, outputFile, d_flag = False, s_flag = False, t_flag=False):
    print('Running Test: ' + str(testNum) + ' - ' + testName + "\n")
    inputFilePath = createInputPath(testNum, inputFile)
    expectedOutputFilePath = createExpectedOutputPath(testNum)
    expectedMessagePath = createExpectedMessagePath(testNum)
    outputFilePath = createOutputPath(testNum, outputFile)
    messageOutputFilePath = createMessageOutputPath(testNum)

    commandLineArg = createCommandLineArgForTest(inputFilePath, outputFilePath, d_flag, s_flag, t_flag)

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
    runTest(1, testName1, "testCase1.csv", "testCase1Output.json")
    #test case 2
    runTest(2, testName2, "testCase2.csv", "testCase2Output.json", d_flag=True, s_flag=True)
    #test case 3
    runTest(3, testName3, "testCase3.csv", "testCase3Output.json", d_flag=True, t_flag=True)
    #test case 4
    runTest(4, testName4, "testCase4.csv", "testCase4Output.json", s_flag=True)
    #test case 5
    runTest(5, testName5, "testCase5.csv", "testCase5Output.json")
    #test case 6
    runTest(6, testName6, "testCase6.csv", "testCase6Output.json", s_flag=True)
    #test case 7
    runTest(7, testName7, "testCase77.csv", "testCase7Output.json")
    #test case 8
    runTest(8, testName8, "testCase8.csv", "random/testCase8Output.json")
    #test case 9
    runTest(9, testName9, "testCase9.csv", "testCase9Output.json", t_flag=True)


if __name__ == "__main__":
    runAllTests()

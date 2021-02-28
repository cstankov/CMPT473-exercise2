import os
import io
import filecmp
 

pathFileInput = 'TestData/TestFiles/TestInput/'
pathFileOutput = 'TestData/TestFiles/TestOutput/'
pathOutputMessage = 'TestData/TestFiles/TestOutput/Messages/'
pathExpectedOutput= 'TestData/ExpectedOutput/'
pathExpectedMessage= 'TestData/ExpectedMessages/'
num = 1
 
def testFileName(name):
    global num
    return ('testCase' + str(num) + '.csv')
 
def newMessageOut(commandLine):
    global num
    with io.FileIO(pathOutputMessage + testFileName('message.txt'), 'w') as file:
        file.write(commandLine)
 
def appendMessageOut(msg):
    global num
    with io.FileIO(pathOutputMessage + testFileName('message.txt'), 'a') as file:
        file.write(msg)
 
 
def runProg(inputFile, outputFile, d_flag = False, s_flag = False):
    msgFileOut = pathOutputMessage + testFileName('message.txt')
    out = pathFileOutput + testFileName(outputFile)
    inp = pathFileInput + testFileName(inputFile)
    msgFileExp = pathExpectedMessage + testFileName('ExpectedMessage.txt')
 
    commandLine = 'csv2json ' + inp + ' ' + out
    if(d_flag == True):
        commandLine = 'csv2json -d ' + inp + ' ' + out   
    elif (s_flag ==True):
        commandLine = 'csv2json -s "\t"' + inp + ' ' + out
 
    print(commandLine + '\n')
    newMessageOut(commandLine + '\n\n')
    
    if os.path.exists(inp) == False:
        message = 'Input path is INVALID'
        print("Message: " + message)
        appendMessageOut(message)
    elif os.path.exists(out) == False:
        message = 'Output path is INVALID'
        print("Message: " + message)
        appendMessageOut(message)
    else:
        os.system(commandLine)
        compareFiles(outputFile)
    
    compareMessages(msgFileOut, msgFileExp)
    return
 
 
def compareMessages(actualMsg, expMsg):
    commandLine = '\ndiff ' + actualMsg + ' ' + expMsg
    print(commandLine + '\n')
    os.system(commandLine)
 
    msg = ""
    if filecmp.cmp(actualMsg, expMsg):
        msg = 'Test Passed!! Both Message Files Match'
    else:
        msg = 'Test Failed! Both Message Files Do Not Match'
 
    print(msg)
    return
 
def compareFiles(outputFile):
    out = pathFileOutput + testFileName(outputFile)
    outExp = pathExpectedOutput + testFileName('ExpectedOutput.json')
 
    outMsg = pathOutputMessage + testFileName('message.txt')
 
    commandLine = 'diff ' + out + ' ' + outExp
    print(commandLine + '\n')
    os.system(commandLine)
    appendMessageOut(commandLine + '\n\n')
 
    msg = ""
    if filecmp.cmp(out, outExp):
        msg = 'Output and Expected Files Match'
    else:
        msg = 'Output and Expected Files DO NOT Match'
 
    print('message: ' + msg)
    appendMessageOut(msg)     
 
    print('\nMessage saved to ' + outMsg)
    return
 
 
def testFrame(testName, inputFile, outputFile, d_flag = False, s_flag = False):
    global num
    print('\n\nTest: ' + str(num) + ' - ' + testName)
    print("\n")
    runProg(inputFile, outputFile, d_flag, s_flag)
    num += 1
 
 
print("ACTS TESTING OF CSV2JSON PROGRAM ")   
print("=================================")
print("=================================\n\n")

#test case 1
testFrame("testing num and bool with tabs.", "testCase1.csv", "testCase1Output.json", True)
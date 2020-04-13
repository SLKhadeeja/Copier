import re, os, shutil

pdfRegex = re.compile(r'[\w+\s\-\.|\w+]+.pdf')
txtRegex = re.compile(r'[\w+\s\-\.|\w+]+.txt')

def copy(String):
    for j in range(len(String)):
            print('COPYING FILE INSIDE ' + folderName + ':' + String[j])
            shutil.copy((folderName + '\\' + String[j]), copyPath)

def copying():
    for folderName, subFolders, fileNames in os.walk(workPath):
        print('CHECKING ' + folderName)
        for fileName in fileNames:
            workStr = ''
            for i in range(len(fileNames)):
                workStr = workStr + ':' + fileNames[i]
            
            matchpdf = pdfRegex.findall(workStr)
            copy(matchpdf)
            matchtxt = txtRegex.findall(workStr)
            copy(matchtxt)
            
        for subFolder in subFolders:
            print('SUBFOLDER OF ' + folderName + ':' + subFolder)
        
         
def start(source, destination):
    workpath = source
    copyPath = destination

    copying()
            

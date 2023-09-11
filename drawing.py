import matplotlib.pyplot as plt
import numpy as np
import os

def getDirPath(dirAll):
    dirList = []
    for dir in os.scandir(dirAll):
        if dir.is_dir():
            dirList.append(dir.path)
    return dirList

def solveEachinstitute(path):
    year = '2013'
    x = []
    y = []
    for everydayFile in os.scandir(path):
        with open(everydayFile,'r') as f:
            info = f.read().strip().split('\n')
            featureTemperature = info[1].split(',')[2]
            featureTemperature = float(featureTemperature)
            institute = everydayFile.name[0:5]
            tepYear = everydayFile.name[6:10]
            tepDay = everydayFile.name[10:14]
            if tepYear == year:
                x.append(tepDay)
                y.append(featureTemperature)
            else:
                plt.xlabel('Full Year ' + year + ' Date')
                plt.ylabel('temperature (°C)')
                plt.title(institute+'_institute')
                plt.xticks([])
                plt.plot(x,y)
                plt.show()
                x = []
                y = []
                year = str(int(year) + 1)
if __name__ == '__main__':
    #print('hello,world')
    dirList = getDirPath("./data/原始数据/20230228/tk/")
    # print(dirList)
    # solveEachinstitute(dirList[0])
    for dir in dirList:
         solveEachinstitute(dir)
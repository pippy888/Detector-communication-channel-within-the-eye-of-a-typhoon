import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

def getDirPath(dirAll):
    dirList = []
    dirName = []
    for dir in os.scandir(dirAll):
        if dir.is_dir():
            dirList.append(dir.path)
            dirName.append(dir.name)
    return dirList,dirName
def solveEachinstitute(path,name):
    year = '2013'
    x = []
    y = []
    institute = name
    newDir = '.\\' + name + '_pictures'
    if os.path.exists(newDir):
        shutil.rmtree(newDir)
    os.mkdir(newDir)
    for everydayFile in os.scandir(path):
        with open(everydayFile, 'r') as f:
            info = f.read().strip().split('\n')
            featureTemperature = info[1].split(',')[2]
            featureTemperature = float(featureTemperature)
            tepYear = everydayFile.name[6:10]
            tepDay = everydayFile.name[10:14]
            if tepYear == year:
                x.append(tepDay)
                y.append(featureTemperature)
            else: #一年结束
                # plt.xlabel('Full Year ' + year + ' Date')
                # plt.ylabel('temperature (°C)')
                # plt.title(institute + '_institute')
                # plt.xticks([])
                # plt.plot(x, y)
                # plt.show()
                dataAggregation(year,name,x,y)
                year = str(int(year) + 1)
    dataAggregation(year,name,x,y)
def dataAggregation(year,name,x,y):
    with open('.\\' + name + '_pictures' + '\\' + year + '.txt', 'w') as newFile:
        for i in range(0, len(x)):
            newFile.write(str(x[i]) + ' ' + str(y[i]) + '\n')
        x = []
        y = []
if __name__ == '__main__':
    #print('hello,world')
    dirList,dirName = getDirPath("./data/原始数据/20230228/tk/")
    # print(dirList)
    # solveEachinstitute(dirList[0], dirName[0])
    for i in range(0,len(dirList)):
        solveEachinstitute(dirList[i],dirName[i])
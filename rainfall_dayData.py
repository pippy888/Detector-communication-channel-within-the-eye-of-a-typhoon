import numpy as np
import os
import shutil

mouthDate = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 平年
mouthDate_1 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 闰年

def getDataOfFile(path):
    with open(path) as f:
        buffer = f.read().strip()
        return buffer
if __name__ == '__main__':

    buffer = getDataOfFile('.\\data\\原始数据\\20230228\\Rain.txt')
    tmp = buffer.split('\n')
    institute = tmp[0].strip().split()
    mouth = tmp[1:]
    if os.path.exists('.\\rainfall_dayData'):
        shutil.rmtree('.\\rainfall_dayData')
    os.mkdir('.\\rainfall_dayData')
    for i in range(1,len(institute)):
        tmpPath = '.\\rainfall_dayData\\'+str(institute[i])
        if os.path.exists(tmpPath):
            shutil.rmtree(tmpPath)
        os.mkdir(tmpPath)
        # for year in (2013,2023):
        #     file = open(tmpPath+'\\' + str(year), 'w')
        #     file.close()

    year = '2013'
    year_rainfall_data = []  # 准备留作整年待写入的数据
    for i in range(1,len(institute)):
        for j in range(0,len(mouth)):
            detail = mouth[j].split() #一整行数据 空格隔开
            year_now = detail[0][0:4]
            mouth_now = detail[0][4:6]
            mouth_average_rainfall_data = float(detail[i])
            if year != year_now:
                tmpPath = '.\\rainfall_dayData\\' + str(institute[i]) + '\\'
                with open(tmpPath + year + '.txt','w') as f:
                    for item in year_rainfall_data:
                        f.write(item)
                year = str(int(year) + 1)
                year_rainfall_data = []
            if mouth_average_rainfall_data < 10000: #999999是没有测到的值
                sum_of_day = mouthDate[int(mouth_now)] if int(year) % 4 != 0 else mouthDate_1[int(mouth_now)] #那个月份的天数
                n = np.random.normal(mouth_average_rainfall_data,0.1*mouth_average_rainfall_data,sum_of_day) #生成符合高斯分布的随机数
                n = np.around(n,decimals=2)
                for item in n:
                    year_rainfall_data.append(str(item))
                    year_rainfall_data.append(' ')
                year_rainfall_data.append('\n')
            else:
                sum_of_day = mouthDate[int(mouth_now)] if int(year) % 4 != 0 else mouthDate_1[int(mouth_now)]  # 那个月份的天数
                n = np.zeros(sum_of_day)
                for item in n:
                    year_rainfall_data.append(str(item))
                year_rainfall_data.append('\n')
        tmpPath = '.\\rainfall_dayData\\' + str(institute[i]) + '\\'
        with open(tmpPath + year + '.txt', 'w') as f:
            for item in year_rainfall_data:
                f.write(item)
        year = '2013'
        year_rainfall_data = []



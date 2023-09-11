import numpy as np
import os
import shutil

mainDataPath = '.\\height_interval_data'
def process_every_institute(dirPath,dirName):
    instituteDir = os.path.join(mainDataPath,dirName)
    if os.path.exists(instituteDir):
        shutil.rmtree(instituteDir)
    os.mkdir(instituteDir) # 每个气象台的文件夹
    mouth = 1
    year = 2013
    heigth_interval = [0,150,1000,3000,5000,7500,10000,12000,14000,16000,18000,20000,22000]
    # for i in range(0,len(heigth_interval)):
    #     num[i] = 0
    num_pressure = np.zeros_like(heigth_interval)    # 压力和
    num_temperature = np.zeros_like(heigth_interval) # 温度和
    num_dewpoint = np.zeros_like(heigth_interval)     # 露点和
    num_sum = np.zeros_like(heigth_interval)         # 个数
    num_pressure_all = np.zeros((13,len(heigth_interval)))
    num_temperature_all = np.zeros((13,len(heigth_interval)))
    num_dewpoint_all = np.zeros((13,len(heigth_interval)))

    for file in os.scandir(dirPath):
        year_now = file.name[6:10]
        mouth_now = file.name[10:12]

        if mouth != int(mouth_now):
            for i in range(0,len(num_sum)): # num_sum可能出现sum是0的项，把是0的项的sum设为1即可，因为对应的分子也一定是0
                if num_sum[i] == 0:
                    num_sum[i] = 1
            # 但还需要注意一个问题，就是露点温度在12km左右以上就测不到了，这时候代码会将此值设为-1（设为0会更好其实）所以露点温度如果是-1，则说明测不到了
            num_pressure_all[int(mouth)] = num_pressure / num_sum
            num_temperature_all[int(mouth)] = num_temperature / num_sum
            num_dewpoint_all[int(mouth)] = num_dewpoint / num_sum
            mouth = mouth_now # 更新mouth
            # 更新每月数组
            num_pressure = np.zeros_like(heigth_interval)  # 压力和
            num_temperature = np.zeros_like(heigth_interval)  # 温度和
            num_dewpoint = np.zeros_like(heigth_interval)  # 露点和
            num_sum = np.zeros_like(heigth_interval)  # 个数
        if year != int(year_now):
            with open(os.path.join(instituteDir,str(year)+'.txt'),'w') as f:
                f.write('pressure:\n')
                for i in range(1,13):
                    f.write(str(num_pressure_all[i]))
                    f.write('\n')
                f.write('temperature:\n')
                for i in range(1, 13):
                    f.write(str(num_temperature_all[i]))
                    f.write('\n')
                f.write('dewpoint:\n')
                for i in range(1, 13):
                    f.write(str(num_dewpoint_all[i]))
                    f.write('\n')
            num_pressure_all = np.zeros((13, len(heigth_interval)))
            num_temperature_all = np.zeros((13, len(heigth_interval)))
            num_dewpoint_all = np.zeros((13, len(heigth_interval)))
            # print(year)
            # print(year_now)
            # print(file)
            year = int(year_now)

        # 遍历文件数据
        with open(file,'r') as readFile:
            buffer = readFile.read()
            statement = buffer.strip().split('\n')
            for i in range(1,len(statement)):
                detail = statement[i].split(',')

                if detail[1] == '':  # height数据缺失，跳过
                    continue
                pressure = 0 if detail[0] == '' else float(detail[0])
                height = float(detail[1])
                temperature = 0 if detail[2] == '' else float(detail[2])
                dewpoint = 0 if detail[3] == '' else float(detail[3])
                index = judgeHeight(height)
                num_pressure[index] += pressure
                num_temperature[index] += temperature
                num_dewpoint[index] += dewpoint
                num_sum[index] += 1
    # 每个文件夹的最后一个2020年的文件结束后还未处理全年数据
    with open(os.path.join(instituteDir, str(year) + '.txt'), 'w') as f:
        f.write('pressure:\n')
        for i in range(1, 13):
            f.write(str(num_pressure_all[i]))
            f.write('\n')
        f.write('temperature:\n')
        for i in range(1, 13):
            f.write(str(num_temperature_all[i]))
            f.write('\n')
        f.write('dewpoint:\n')
        for i in range(1, 13):
            f.write(str(num_dewpoint_all[i]))
            f.write('\n')

def judgeHeight(height):
    heigth_interval = [0, 150, 1000, 3000, 5000, 7500, 10000, 12000, 14000, 16000, 18000, 20000, 22000]
    for i in range(0,len(heigth_interval)-1):
        if height >= heigth_interval[i] and height <= heigth_interval[i+1]:
            return i
    return len(heigth_interval) - 1
if __name__ == '__main__':
    if os.path.exists(mainDataPath):
        shutil.rmtree(mainDataPath)
    os.mkdir(mainDataPath)
    dataPath = '.\\data\\原始数据\\20230228\\tk\\'
    for dir in os.scandir(dataPath):
        if dir.is_dir():
            process_every_institute(dir.path,dir.name)
            # break # test


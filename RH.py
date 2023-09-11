import os
# with open("./data/原始数据/20230228/tk/50953/50953_2013010100.csv","r") as file:
#     buffer = file.read()
#     list = buffer.split()
#     for v in list:
#         print(v)

def getFilePath(dirAll):
    dirList = []
    for dir in os.scandir(dirAll):
        if dir.is_dir():
            for file in os.scandir(dir):
                dirList.append(file.path)
    return dirList

def oprationFile(filePathList):
    for file in filePathList:
        f = open(file,'r+')
        print(file)
        buffer = f.read()
        statement = buffer.split('\n')
        statement[0] += ',相对湿度(RH)'
        for i in range(1,len(statement)-1):
            # print(statement[i])
            date = statement[i].split(',')
            # print(date)
            pressure, height, temperature, dewpoint = date[0], date[1], date[2], date[3]
            # print(pressure,height,temperature,dewpoint)
            if temperature == '' or dewpoint == '':
                break
            temperature = float(temperature)
            dewpoint = float(dewpoint)
            es = Approximate_formula_for_saturated_water_vapor_pressure(temperature)
            e = Approximate_formula_for_saturated_water_vapor_pressure(dewpoint)
            RH = (e / es) * 100
            statement[i] += ',' + '{:.2f}'.format(RH)
            # print(RH)
        f.seek(0)
        for i in range(0, len(statement)):
            f.write(statement[i] + '\n')
        f.close()




def Approximate_formula_for_saturated_water_vapor_pressure(temperature):
    return 6.11 * 10.0 ** ((7.5 * temperature) / (237.7 + temperature))
"""
要将气压、温度和露点转化为湿度，你可以使用饱和水蒸气压的概念。下面是一种常用的方法：
使用给定的温度值来计算饱和水蒸气压（es）。
如果温度单位为摄氏度（℃），可以使用饱和水蒸气压的近似公式来计算：
es = 6.11 * 10^[(7.5 * 温度) / (237.7 + 温度)]
如果温度单位为华氏度（℉），首先将其转化为摄氏度，然后使用上述公式计算。
使用给定的露点值来计算露点水蒸气压（e）。
露点水蒸气压等于饱和水蒸气压在给定的露点温度下的值。
使用给定的气压值来计算相对湿度（RH）。
RH = (e / es) * 100
这样，你就可以通过将气压、温度和露点转化为相对湿度。请注意，这个方法假设大气中只有水蒸气，而没有其他气体的影响。在实际应用中，还可能有其他因素需要考虑。
"""
if __name__ == '__main__':
    dirList = getFilePath("./data/原始数据/20230228/tk/")
    # print(dirList)
    oprationFile(dirList)
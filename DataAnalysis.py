'''
Author: your name
Date: 2021-07-28 16:24:27
LastEditTime: 2021-07-28 16:24:27
LastEditors: your name
Description: In User Settings Edit
FilePath: /数据分析代码/study.py
'''

'''
Author: your name
Date: 2021-07-27 17:18:42
LastEditTime: 2021-07-27 17:18:42
LastEditors: your name
Description: In User Settings Edit
FilePath: /数据分析代码/study.py
'''
     
import os
import sys
import xlwt
import csv

import matplotlib.pyplot as plt 
from scipy import interpolate
import numpy as np

import matplotlib.font_manager as mpt


# #去掉txt里面的空白行，并保存到新的文件中
# with open('./out.txt','r',encoding = 'utf-8') as fr,open('./output.txt','w',encoding= 'utf-8') as fd:
# 	for text in fr.readlines():
# 		if text.split():
# 			fd.write(text)
# 	print('success')

# 提取关键字行
fr = open('./ReceivedTofile-COM10-2021_7_28_13-25-30.DAT','r')
fw = open('./DataAbstract.txt','w')
fwtest = open('./DataAbstracttest.txt','w') 

lines = fr.readlines()
for line in lines:
    if 't_RCAR_Sys_time_stmp_tick.i64RCARTimestmp' in line:
        fw.write(line)    
    if 't_RCAR_Sys_time_stmp_tick.i64valtest' in line:
        fwtest.write(line)
        
with open('./DataAbstract.txt','r',encoding='utf-8') as file1,open('./DataAbstracttest.txt','r',encoding='utf-8') as file2,open('./testval.txt','w',encoding='utf-8') as file3:
    xlines = file1.readlines()
    ylines = file2.readlines()    
    for line1,line2 in zip(xlines,ylines):
        file3.write("{},{}\n".format(line1.rstrip(), line2.rstrip()))
        
#  #创建一个workbook对象，相当于创建一个Excel文件
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
# '''
# Workbook类初始化时有encoding和style_compression参数
# encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。默认是ascii。
# style_compression:表示是否压缩，不常用。
# '''

# # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
sheet = book.add_sheet('Output', cell_overwrite_ok=True)
# 其中的Output是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False


#数据切片并存储txt文件 

n=1
with open('./testval.txt','r',encoding='utf-8') as fr,open('./output.txt','w',encoding='utf-8') as fw:
    for text in fr.readlines():
        x = text.split(',')[1]  #数据第一次切片
        # print(x)
        y = text.split(',')[3]
        # print(y)
        a = x.split('=')[1]     #数据第二次切片
        b = y.split('=')[1]
        fw.write(a + ' ' +b)    #数据写入txt文件       
        sheet.write(n,0,a)      #数据写入sheet 0行 0列
        sheet.write(n,1,b)      #数据写入sheet 0行 1列        
        n =  n+1                #循环写入
book.save('Output.xls')         #保存工作表

# 写入CSV文件
csvFile = open("./data.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("./output.txt",'r',encoding='utf-8')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()


# 等差数列
# print(np.linspace(0.1, 1, 10, endpoint=True))

"""总结：
  arange 侧重点在于增量，不管产生多少个数
  linspace 侧重于num, 即要产生多少个元素，不在乎增量
"""
# 等比数列
# np.logspace(1, 4, 4, endpoint=True, base=2) # 2**1---2**4

file =  open('./data.csv')  #打开csv文件
filereader = csv.reader(file)  #读取csv文件
Data = list(filereader) #转换为list列表
len1 = len(Data)    #读取到数据行数
# print(len1)


x = np.arange(1,len1, 1)
print(x)

y = list()  
z = list()

for i in range(1,len1): 
    # print(y.append(Data[i][0]))
    y.append(Data[i][0])
    z.append(Data[i][1])

plt.plot(x,y)
plt.plot(x,z)
plt.show()










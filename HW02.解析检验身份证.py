#coding:utf-8
import re

dict_temp = {}

# 打开文本文件
file = open('GB.txt','r')

# 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
for line in file.readlines():
    line = line.strip()
    k = line.split('\t')[0]
    v = line.split('\t')[1]
    dict_temp[k] = v



def checkIdcard(idcard):
    Errors = ['验证通过!', '身份证号码位数不对!',
              '身份证号码出生日期超出范围或含有非法字符!', '身份证号码校验错误!', '身份证地区非法!']

    idcard = str(idcard)
    idcard_list = list(idcard)
    # 地区校验
    if (not dict_temp[(idcard)[0:6]]):
        print(Errors[4])

    if (len(idcard) == 18):
        # 出生日期的合法性检查
        if (int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10]) % 4 == 0)):
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
        else:
            ereg = re.compile(
                '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
        if (re.match(ereg, idcard)):
            # //计算校验位
            S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + (int(idcard_list[1]) + int(idcard_list[11])) * 9 + (
                int(idcard_list[2]) + int(idcard_list[12])) * 10 + (
                int(idcard_list[3]) + int(idcard_list[13])) * 5 + (
                int(idcard_list[4]) + int(idcard_list[14])) * 8 + (
                int(idcard_list[5]) + int(idcard_list[15])) * 4 + (
                int(idcard_list[6]) + int(idcard_list[16])) * 2 + int(idcard_list[7]) * 1 + int(
                idcard_list[8]) * 6 + int(idcard_list[9]) * 3
            Y = S % 11
            M = "F"
            JYM = "10X98765432"
            M = JYM[Y]  # 判断校验位
            if (M == idcard_list[17]):  # 检测ID的校验位
                return(Errors[0])
            else:
                return(Errors[3])
        else:
            return(Errors[2])
    else:
        return(Errors[1])

def get_birthday(cdcard):
    birth_year = int(cdcard[6:10])
    birth_month = int(cdcard[10:12])
    birth_day = int(cdcard[12:14])
    birthday = f"{birth_year}年{birth_month}月{birth_day}日"
    return birthday

def get_sex(cdcard):
    num = int(cdcard[16:17])
    if num % 2 == 0:
        return "女"
    else:
        return "男"

if __name__ == "__main__":
    while True:
        cdcard = input("请输入您的身份证号：")
        if cdcard == "exit":
            print("程序已结束！")
            break
        else:
            print(checkIdcard(cdcard))
            if checkIdcard(cdcard) == '验证通过!':
                print("性别：", end='')
                sex = get_sex(cdcard)
                print(sex)
                print("出生日期：", end='')
                birthday = get_birthday(cdcard)
                print(birthday)
                print("出生地域：", end='')
                print(dict_temp[(cdcard)[0:6]])
                print('')

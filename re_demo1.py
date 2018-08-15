import re

#####################匹配单个字符###############################
# 1.匹配某个字符串
# match()匹配以某个字符串开头的
# text = "hello"
# ret = re.match('he',text)
# print(ret.group())

# 2.点，匹配任意的 单个 字符,换行符\n不能匹配
# text = "hello"
# ret = re.match('.',text)
# print(ret)

# 3.\d，匹配 1个 任意的数字0~9，\D匹配单个的非数字字符
# text = "hello"
# ret = re.match("\D",text)
# print(ret)

# 4. \s 匹配任意的空白字符，包括空格、制表符、换页符等.、\S正好相反
# text = "\r"
# ret = re.match("\s",text)
# print(ret.group())

# 5. \w,匹配的是a-z,A-Z,数字和下划线,\W正好相反
# text = "_12Aq"
# ret = re.match('\w',text)
# print(ret.group())

# # 6. [...]匹配括号中的任意一个
# text = "1"
# ret = re.match('[a1]',text)
# print(ret.group())

# 7.组合方式
# text = "0731-88888qwe"
# ret = re.match('[\d\-]+',text)
# print(ret.group())

# 8.中括号代替\D \W
# text = "_"
# ret = re.match('[^a-zA-Z0-9]',text)
# print(ret.group())


######################匹配多个字符#################################
# × 匹配0个或者任意多个
# + 匹配1个或者任意多个
# ？ 匹配0个或者1个
# {m} 匹配m个
# {m,n} 匹配m到n次

#########案例1##############
# 手机号
text = "18578900987"
ret = re.match('1[34578]\d{9}',text)
print(ret.group())

##############案例2##########
# 邮箱
text = "abc@163.com"
ret = re.match('\w+@[a-z0-9]+\.[a-z0-9]+',text)
print(ret.group())

#############案例3############
# url
text = "https://www.google.com/search?q=python&oq=python&aqs=chrome..69i57j69i60j69i58j69i61l2.4081j0j4&sourceid=chrome&ie=UTF-8"
ret = re.match('(http|https|ftp)://[\S]+',text)
print(ret.group())

#########案例4################
#身份证号
text = "513902199311178192"
ret = re.match('\d{17}[\dxX]',text)
print(ret.group())
import re

# 分组函数group()
text = "apple's price $99,orange's price is $10"
ret =re.search('.*(\$\d+).*(\$\d+)',text)
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))
print(ret.group(0,1,2))
print(ret.groups())

# find函数  返回的是一个列表
text = "apple's price $99,orange's price is $10"
ret =re.findall('\$\d+',text)
print(ret)

# sub函数  替换
text = "apple's price $99,orange's price is $10"
ret =re.sub('\$\d+',"￥998",text)
print(ret)

# split函数 分割
text = "life is short ,i use python"
ret = re.split(' ',text)
print(ret)

# cpmplile
text = "the number is 20.50"
# r =re.compile('\d+\.?\d+')
r = re.compile(r"""
    \d+ # 小数点前面的数字
    \.? # 小数点本身
    \d+ # 小数点后面的数字
""",re.VERBOSE)
ret = re.search(r,text)
print(ret.group())
import json

books = [
    {
        'title': '钢铁是怎样练成的',
        'price': 9.8
    },
    {
        'title': '红楼梦',
        'price': 9.9
    }
]
#将字典或列表直接转换为JSON
json_str = json.dumps(books,ensure_ascii=False)
print(type(books))
print(type(json_str))
print(json_str)
print(type([{"price": 9.8, "title": "钢铁是怎样练成的"}, {"price": 9.9, "title": "红楼梦"}]))
#dump到json文件中
with open('books.json','w') as fp:
    json.dump(books,fp,ensure_ascii=False)

print("=================================json转化为python==============================")

json_str = '[{"title": "钢铁是怎样练成的", "price": 9.8}, {"title": "红楼梦", "price": 9.9}]'
print(type(json_str))
books = json.loads(json_str,encoding='utf-8')
print(type(books))
print(books)

with open('books.json','r') as fp:
    json_str  = json.load(fp)
    print(json_str)
    print(type(json_str))
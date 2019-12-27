### 如何把一个字典转换成一个字典，但是只是留下少量属性。但是加了几个新的键值对：
keyword:
total:1

result是一个字典。它有各种属性

def isbn_convert(q, result):
    result  = {}
    result1 = cut_dict(result0)
    result['keyword'] = q
    result['total'] = 1
    result['books'] = result1

# 如何剪切一个字典，保留少部分的属性呢？
def cut_dict(result1):
    result = {}
    # ？笔记：我的写法不够简单，去看原版
    result['author'] = result1['author']
    result['image'] = result1['author']
    result['author'] = result1['author']
    return result

'''
这个bookcollection类要完成什么功能呢？
1:它要做为一个对象，对象里有属性：keyword,total,还有就是所有查询到的书的一个列表，列表里是字典
2


'''
class Book():
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    # 定义函数，函数能把上一步yushubook查询到的对象传进来，把关键字q传进来，然后赋值给Book属性。
    def convert(self, data, q):
        self.total = data.total
        self.keyword = q
        self.books = data.books


books = Book()
books.convert(yushubook,q)

return books




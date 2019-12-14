# 需求：如果是13位的数字，或者是10位的数字，数字中有"-"，那么就判断为isbn,否则就是key,这里有两个编程方面的思想要注意：一个可以把这个判断做为一个函数封装起来，这是为了1容易阅读，一看你的函数名就知道这个函数是做什么的，如果一个表达式出现两次，也可以把它封装成一个变量。第二个就是怎么把If elsea语句写得简短，代码少，执行快。你就要让计算机减少判断。把容易出现的情况写在前面。
# 需要封装一个函数，第一，放在试图函数里，代码在多，不易阅读，第二，有可能其它地方也要用到这个判断，第三,占用太多视图函数代码行

# 如果x是13位，而且是数字，那么就判断x为isbn,或者x是10位，且是数字，中间可能有"-"。那么也判断是数字，其它情况就是关键字。
# 版本一
def is_isbn_or_key(x):
    if len(x) == 13 and x.isdigit():
        isbn_or_key = 'isbn'
    if  '-' in x and len(x.replace('-', '')) == 10 and x.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    else:
        isbn_or_key = 'key'

# 版本二：提取出y = x.replace('-', '')
def is_isbn_or_key(x):
    if len(x) == 13 and x.isdigit():
        isbn_or_key = 'isbn'

    y = x.replace('-', '')

    if  '-' in x and len(y) == 10 and y.isdigit():
        isbn_or_key = 'isbn'
    else:
        isbn_or_key = 'key'

# 版本三：优化if else，第一个原则，把很有可能出现假的放在前面，这样后面就不用运行就过了，第二个原则是：有一些条件判断是要查询数据库的，这样一些也应该放在后面。

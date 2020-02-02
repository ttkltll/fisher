from app.models.user import User


class WishViewModel():
    def __init__(self,trade):
        user = User.query.filter(User.id == trade.uid)

        self.user_name = user.nickname #如何转换
        self.id = trade.id

class Wishesinfo():
    def __init__(self,trades2):
        self.total = 0
        self.trades = []
        self.__convert(trades2)
    def __convert(self,trades2):
        # def total(self,trades2):
        self.total = len(trades2)

        # def fill(self,trades2):
            # 如何把这本书的所有wish对象，转换成所有符合模板属性的列表？
        self.trades = [WishViewModel(trade) for trade in trades2]




#题目2: 
# 实现一个hash table，input数据是最长1024的ascii码，需要UT。

#class hashtable
class Hashtable:
    __size=0
    __data=[]
    def __init__(self,size):
        self.__size=size
        self.__data=[(None,None) for i in range(self.__size)]
    def hash(self,key):
        if type(key)==type('A'):
            pos=len(key)%self.__size
        else:
            pos=len(str(key))%self.__size
        return pos
    def insert_hash(self,key,data):
        if type(data)!=type('a') :
            print('Input ERROR!')
            return -1
        if len(data)>1024:
            print('Input ERROR!')
            return -1
        pos=self.hash(key)
        while self.__data[pos]!=(None,None):
            pos=(pos+1)%self.__size
        self.__data[pos]=(key,data)
    def search_hash(self,key):
        start=self.hash(key)
        pos=start
        while self.__data[pos][0]!=key:
            pos=(pos+1)%self.__size
            if pos ==start:
                print('Can\'t find data.')
                return -1
        return self.__data[pos][1]
            


#UT:
if __name__=='__main__':
    print('#题目2: 实现一个hash table，input数据是最长1024的ascii码，需要UT。')
    print('测试：建立哈希表并输入ASCII码和测试数据')
    print('测试数据：key：111,222,thekey,test1,test2；data：aaaa,bbbb,ccc,ddd,eeeee')
    h=Hashtable(7)
    h.insert_hash(111,'aaaa')
    h.insert_hash(222,'bbbb')
    h.insert_hash('thekey','ccc')
    h.insert_hash('test1','ddd')
    h.insert_hash('test2','33333')
    print('通过key 111 查找数据：',h.search_hash(111))
    print('通过key 222 查找数据：',h.search_hash(222))
    print('通过key thekey 查找数据：',h.search_hash('thekey'))
    print('通过key test1 查找数据：',h.search_hash('test1'))
    print('通过key test2 查找数据：',h.search_hash('test2'))
    print('当key没有对应的data时，显示找不到数据：')
    h.search_hash('Z')
    print('输入数据不为最长1024的ascii码时，报错')
    h.insert_hash('test3',111)

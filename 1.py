
#题目1:
#用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT。

#class stack with r_pop r_push 
class Stack_r:
    __list=[]
    def __init__(self):
        self.__list=[]
    def r_pop(self):
        if len(self.__list)>0:
            pop_data=self.__list.pop()
            return pop_data
        else:
            print('ERROR! The Stack is empty')
            return -1
    def r_push(self,data):
        if type(data) != type(1):
            print('ERROR! Data type is not Integer')
        else:
            self.__list.append(data)
    def printAll(self):
            print(self.__list)



#class stack with  l_pop l_push
class Stack_l:
    __list=[]
    def __init__(self):
        self.__list=[]
    def l_pop(self):
        if len(self.__list)>0:
            pop_data=self.__list[0]
            self.__list=self.__list[1:]
            return pop_data
        else:
            print('ERROR! The Stack is empty')
            return -1
    def l_push(self,data):
        if type(data) != type(1):
            print('ERROR! Data type is not Integer')
        else:
            self.__list.insert(0,data)
    def printAll(self):
        print(self.__list)


#UT:
if __name__=='__main__':
    print('题目1:用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT')
    print('测试1：左进左出栈')
    print('创建一个空栈并打印')
    sl=Stack_l()
    sl.printAll()
    print('对空栈尝试pop方法，报错')
    sl.l_pop()
    print('压入非整形数据，报错')
    sl.l_push('a')
    print('压入数据1,2,3,4,5，并打印')
    sl.l_push(1)
    sl.l_push(2)
    sl.l_push(3)
    sl.l_push(4)
    sl.l_push(5)
    sl.printAll()
    print('移出一个数据项，打印移除的数据项，并打印栈')
    print('移出数据项为：',sl.l_pop())
    sl.printAll()
    print('测试2：右进右出栈')
    print('创建一个空栈并打印')
    sr=Stack_r()
    sr.printAll()
    print('对空栈尝试pop方法，报错')
    sr.r_pop()
    print('压入非整形数据，报错')
    sr.r_push('a')
    print('压入数据1,2,3,4,5，并打印')
    sr.r_push(1)
    sr.r_push(2)
    sr.r_push(3)
    sr.r_push(4)
    sr.r_push(5)
    sr.printAll()
    print('移出一个数据项，打印移除的数据项，并打印栈')
    print('移出数据项为：',sr.r_pop())
    sr.printAll()













    
    

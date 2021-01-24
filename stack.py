class Stack:
    def __init__(self):
        self.__list= []
        
    # empty list
    def isEmpty(self):
        return self.__list == []
    
    # get size of list
    def size(self):
        return len(self.__list)
    
    # clear items of list
    def clear(self):
        self.__list.clear() 
    
    # push item into back of list
    def push(self, item):
        self.__list.append(item)
        
    # extract last item of list
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
        
    # get items of list
    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    
    # returns output in neat format
    def __str__(self):
        output = '<'
        for i in range( len(self.__list) ):
            item = self.__list[i]
            if i < len(self.__list)-1:
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output
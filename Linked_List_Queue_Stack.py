from typing import Any



class Node:

    value: Any
    next: 'Node'
    
    def __init__(self, value = Any,next = None):
        self.value = value
        self.nextval = next

class LinkedList:

    head : Node
    tail : Node
    
    def __init__(self):
      self.head = None
      self.tail = None

    #############################
    
    def append(self,value:Any)->None:
        NewNode = Node(str(value))
        if self.head == None:
            self.head=NewNode
            self.tail = self.head
            return
        self.tail.nextval = NewNode
        self.tail=self.tail.nextval

    ###################################

    def push(self,value:Any)->None:
        NewNode = Node(str(value))
        if self.head is None:
            self.head = NewNode
            self.tail=self.head
            return
        
        NewNode.nextval=self.head
        self.head=NewNode

    ################################
        
    def node(self,at:int)->Node:
    
        printval = self.head
        count=0
        while count != at:
            printval = printval.nextval
            count=count+1
        return printval
    
     ################################

    def __len__(self):
        if not self.head:
            return 0
        count = 0
        while self.head is not None:
            count += 1
            self.head  = self.head.nextval
        return count

    #######################################
    
    def __str__(self)->str:
        printval = self.head
        c=self.tail
        x='->'
        y=''
        while printval.nextval is not None:
            print(printval.value,"head",c.value,"tail")
            y=y+ printval.value +'->'
            printval = printval.nextval
        y=y+str(printval.value)
        return y

    ####################################

    def remove(self,after:Node)->Any:      
        temp = self.head
        if after == 0:
            self.head = temp.nextval
            temp = None
            return

        # Find the key to be deleted
        for i in range(after -2):
            temp = temp.nextval
            #print(temp.value,i)
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.nextval is None:
            return

        next = temp.nextval.nextval
        
        temp.nextval = None
        temp.nextval = next

    ###########################################
    
    def insert(self, value: Any, after: Node) -> None :
        
        NewNode=Node(str(value))
        
        NewNode.nextval = after.nextval
        after.nextval = NewNode
        
    ####################################
    
    def pop(self) -> Any :
        temp = self.head
        c=temp
        self.head=temp.nextval
        temp=None
        return c

    ##############################
        
    def remove_last(self) ->Node:
        
        temp = self.head

        if temp.nextval.nextval is  None:
                    temp.nextval = None
                    return
        
        while True:
            temp = temp.nextval
            if temp.nextval.nextval is  None:
                temp.nextval = None
                return
          
        
    
list_ = LinkedList()

#print("------------------")
list_.push(1)
list_.push(9)
list_.push(11)
list_.push(12)
list_.push(13)
list_.append(1)
list_.append(9)
list_.append(15)
a=list_.pop()
print(a.value)

#print(list_.node(5))


##print("------------------")
print(list_)
#list_.remove(4)
#list_.pop()
#list_.pop()
#list_.remove_last()
#list_.remove_last()

#x =list_.node(at=0)
#list_.insert(25,x)


#print(list_)
#print("------------------")


class Stack:
    
    _storage: LinkedList

    def __init__(self):
        
        self.stacks = LinkedList()

    def push(self,value):
        self.stacks.append(value)

    def pop(self):
        self.stacks.remove_last()
        
    def __len__(self):
        if not self.stacks.head:
            return 0
        count = 0
        while self.stacks.head is not None:
            count += 1
            self.stacks.head  = self.stacks.head.nextval
        return count

    def __str__(self):
        
        printval = self.stacks.head
        x='->'
        y=''
        while printval.nextval is not None:
            print(printval.value,"head",c.value,"tail")
            y=y+ printval.value +'->'
            printval = printval.nextval
        y=y+str(printval.value)
        return y


stack = Stack()
#stack.push(0)
#stack.push(1)
#stack.pop()
#stack.push(3)
#print(stack,"stack")
#print(len(stack))

#print("---1-----1-----1----1-----1-----1------")
class Queue:

    _storage: LinkedList

    def __init__(self):
        self._storage=LinkedList()

    def peek(self)->Any:
        return self._storage.head

    def enqueue(self, element:Any)->None:
        self._storage.append(element)

    def dequeue(self)->Any:
        return self._storage.pop()

    def __str__(self):
        printval = self._storage.head
        x='->'
        y=''
        while printval.nextval is not None:
            #print(printval.value,"head",c.value,"tail")
            y=y+ printval.value +'->'
            printval = printval.nextval
        y=y+str(printval.value)
        return y

    def __len__(self):
        if not self._storage.head:
            return 0
        count = 0
        while self._storage.head is not None:
            count += 1
            self._storage.head  = self._storage.head.nextval
        return count


queue = Queue()
#queue.enqueue(5)
#queue.enqueue(4)
#queue.enqueue(3)
#queue.dequeue()
#print(queue)
#print(len(queue))

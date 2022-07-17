from typing import Any, List, Callable, Union
#from Projekt1_Python import Node,LinkedList,Stack,Queue
#from typing import Any



class Node:
    def __init__(self, data: Any, post: 'Node'):
        self.value = data
        self.next = post

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
   
        NewNode = Node(data,None)
        if self.head == None:
            self.head=NewNode
            self.tail = self.head
            return
        self.tail.next = NewNode
        self.tail=self.tail.next


    def __str__(self):
        if self.head is None:
            print("Lista nie posiada elementów")
            return
        pom = self.head
        lista = str(pom.value)
        while pom.next is not None:
            pom = pom.next
            lista += ' -> ' + str(pom.value)
        return lista


    

    def pop(self) -> Any:
        temp = self.head
        c=temp
        self.head=temp.next
        temp=None
        return c.value



    def __len__(self):
        if not self.head:
            return 0
        count = 0
        while self.head is not None:
            count += 1
            self.head  = self.head.nextval
        return count


class Queue:

    _storage: LinkedList

    def __init__(self):
        self._storage=LinkedList()

    def peek(self)->Any:
        return self._storage.head

    def enqueue(self, element:Any):
        self._storage.append(element)

    def dequeue(self)->Any:
        return self._storage.pop()

    def __str__(self):
        if self._storage.head is None:
            print('Kolejka pusta')
            return
        helper = self._storage.head
        mqueue = str(helper.value)
        while helper.next is not None:
            helper = helper.next
            mqueue += ', ' + str(helper.value)
        return mqueue
        

    def __len__(self):
        if not self._storage.head:
            return 0
        count = 0
        
        x = self._storage.head
        #print(x.value,"x")
        while x is not None:
            x  = x.next
            count += 1
           
        return count


queue = Queue()



class TreeNode:
    
    value: Any
    children: List['TreeNode']

    def __init__(self,value,children=None):
        self.value: Any = value
        self.children: List['TreeNode'] = []
       

    def is_leaf(self):
        if self.children:
            return False
        return True
          
    def add(self,child:'TreeNode')->None:
        
        self.children.append(TreeNode(child))

    def for_each_deep_first(self, visit:Callable[['TreeNode'], None])-> None:
        visit(self.value)
        for i in self.children:
                i.for_each_deep_first(visit)
         
    def for_each_level_order(self,visit:Callable[['TreeNode'], None])-> None:
        visit(self)
        q = Queue()
        for i in self.children:
            q.enqueue(i)
            visit(i)
        c=q
        while len(c) != 0:
            a = c.dequeue()
            for z in a.children:
                q.enqueue(z)
                visit(z)

        
      

    def __str__(self):
       return self.value
                                   
    
node = TreeNode("F")
node.add("B")
node.add("C")
node.add("D")
node.add("E")
node.children[0].add("Q")
node.children[1].add("Z")
node.children[1].add("G")
node.children[2].add("H")
node.children[3].add("P")



print("--------------")
node.for_each_deep_first(print)
print()
node.for_each_level_order(print)



class Tree:
    root : TreeNode

    def __init__(self,root):
        self.root= TreeNode(root)
        

    def add(value:Any, parent_name:Any) -> None:
        parent_name=TreeNode(parent_name)
        value=TreeNode(value)
        parent_name.children.append(value)

    def for_each_level_order(visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(print)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(print)

    def show(self):
        print(self.root.value,"\n")
        if len(self.children) == 1:
            print("|\n")
            print(self.children.value)
            return
        if self.children:
            for i in self.children:
                print("x")
            
        

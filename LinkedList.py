class MyLinkedList:

    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        current = self.head
        counter = 0
        while current:
            if counter == index:
                return current.val
            current = current.next
            counter += 1
        return -1

    def addAtHead(self, val: int) -> None:
        headNode = MyLinkedList()
        headNode.val = val
        if self.head:
            self.head.prev = headNode
            headNode.next = self.head
        self.head = headNode
        if not self.tail:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        tailNode = MyLinkedList()
        tailNode.val = val
        if self.tail:
            self.tail.next = tailNode
            tailNode.prev = self.tail
        self.tail = tailNode
        if not self.head:
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = MyLinkedList()
        newNode.val = val
        current = self.head
        counter = 0
        if index == 0:
            self.addAtHead(val)
            return
        while current:
            if counter == index - 1:
                newNode.next = current.next
                newNode.prev = current
                current.next = newNode
                if newNode.next:
                    newNode.next.prev = newNode
                else:
                    self.tail = newNode
                break
            current = current.next
            counter += 1

    def deleteAtIndex(self, index: int) -> None:
        counter = 0
        current = self.head
        if index == 0 and current:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        while current:
            if counter == index - 1:
                if not current.next:
                    break
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                else:
                    self.tail = current
                break
            current = current.next
            counter += 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

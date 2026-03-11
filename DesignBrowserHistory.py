class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = DLLStack()
        self.stack.AddHomePage(homepage)

    def visit(self, url: str) -> None:
        self.stack.AddAfterPositionAndFlush(url)

    def back(self, steps: int) -> str:
        return self.stack.goBack(steps)


    def forward(self, steps: int) -> str:
        return self.stack.moveForward(steps)

class DLLStack:
    def __init__ (self):
        self.position = None
        self.val = None
        self.next = None
        self.prev = None
    
    def AddHomePage(self, string:str):
        newNode = DLLStack()
        newNode.val = string
        self.position = newNode

    def AddAfterPositionAndFlush(self, string:str):
        newNode = DLLStack()
        newNode.val = string
        self.position.next = newNode
        newNode.prev = self.position
        self.position = newNode
    
    def goBack(self, steps:int) -> int:
        x = 0
        while self.position.prev and steps > x:
            print(self.position.val)
            self.position = self.position.prev
            x += 1
        print(self.position.val)
        print("-------")
        return self.position.val

    def moveForward(self, steps: int) -> int:
        x = 0
        while self.position.next and steps > x:
            self.position = self.position.next
            x += 1
        return self.position.val
        



            


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

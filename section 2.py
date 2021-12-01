#question 1
class Account:
    count = 0

    def incr(self):
        self.count += 1
        return self.count
    
    def __init__(self, name, balance):
        self.id = self.incr()
        self.name = name
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"
        
   
   
#("John", 1000)
#temp = test.deposit(1000000)
#print(f"{test}")

#question 2     
class DevAccount(Account):
  def __init__(self, name, balance):
    super().__init__(name, balance)

  def getBalance(self):
    print(self.name, "'s balance is", self.balance)
    
  def setBalance(self, amount):
    self.balance = amount 

  def transfer(self, amount):
    self.balance -= amount 
    
x = DevAccount("Mike", 1000)
x.setBalance(100)
x.transfer(10)
x.getBalance()




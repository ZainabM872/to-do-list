#make a class for a task
from types import new_class


class Task:

  def __init__(self, description
               ):  #constructor: used to initialize the attributes of an object
    #initialize object attributes
    self.description = description  #holds info about task
    self.next_task = None  #no new nodes initally: refers to next_task node


#create a To-do list class to manage list of tasks
class ToDoList:
  #initializes an empty list to start with
  def __init__(self):
    self.head = None  #no nodes

  #adds new task to list
  def add_task(self, description):
    new_task = Task(description)  #create a new object. This is a new node
    if self.head is None:  #if list is empty
      self.head = new_task  #set the new node as the head
    else:  #if the list isnt empty

      #create a pointer that will go thru the list and add the node the the beginning
      current = self.head
      #points to head node (first node in list)
      #use next pointer in each node to go thru list: current = the current node.next

      while current.next_task:  #while theres another node: runs until theres no more nodes
        current = current.next_task  #current points to next node
      current.next_task = new_task  #the new task is added to the end of the list

  def remove_task(self, description):
    #if list is empty, nothing happens
    if self.head is None:
      print("The list is empty!")
      return

    #remove first node from list if description matches the description value
    if self.head.description == description:  #if the description of task on first node matches the description of object
      self.head = self.head.next_task  #updates the head to be the next node (skips the first node)
      print("Task removed successfully")
      return

  #use a pointer to go thru list
    current = self.head  #the pointer is at the beginnign of the list
    while current.next_task:  #while theres a new node: stops when current.next_task = None
      #check if the ponters description matches with the current node
      if current.next_task.description == description:
        #skip over the current node (aka delte it) and move on to the next
        current.next_task = current.next_task.next_task
        
        print("Task removed successfully")
        return
      #if no match is found, pointer continues to move thru list:
      current = current.next_task
    print("There is no task with that name in the list") #when the while loop ends

  def task_at_front(self, description):
    #create a new task
    new_task = Task(description)
    if self.head is None:  #if list is empty
      self.head = new_task  #set the new node as the head
      return
    else: 
      new_task.next_task = self.head # Set the new node's 'next' pointer to the current head
      self.head = new_task #set the head = to the new task
      return
      
  def print_list(self):
    current = self.head  #the pointer points to the first node
    #check if list is empty:
    if current is None:
      print("The list is empty!")
    #if list is not empty
    else:
      print("Your current list: ")
      #create pointer that goes thru list and prints it
      pointer = self.head  #pointer points to first node in list
      while pointer:
        print(pointer.description)
        pointer = pointer.next_task  #move to next pointer
      #when there r no more elements left to print
      print("We've reached the end of the list")

  def search(self, description):
    #value = input("What task do you want to search for? ")
    current = self.head #make a pointer at the beginning that will go thru the list
    while current.next_task: #while there r more nodes
      #current = current.next_task #move the pointer to the next node

      #PROBLEM: THIS IS COMMENTED OUT
      if current.next_task.description == description or current.description == description:
        print(description, "was found!") 
        break 
      current = current.next_task
    if current.next_task == "null":
      print("There isnt a task with that name in the list")

#menu

my_list = ToDoList()  #create a to do list object
userInput = 3
while userInput != 6:
  print("\nWelcome to the to-do list application!")
  print("1: Enter a task anywhere in the list")
  print("2: Delete a task")  
  print("3: Enter a high priority task at the top of the list")
  print("4: Print the current list")
  print("5: Check if a task is already in the list")
  print("6: Exit program")
  
  userInput = int(input("\nPlease select an option from above: "))
  #check if input is invalid
  while userInput > 6 or userInput < 1:
    userInput = int(input("please enter a number between 1 and 6: "))

#implement algorithims for user responses
  if userInput == 1:
    print("Add a task: ")
    my_list.add_task(input())
  elif userInput == 2:
    print("which task would you like to remove? ")
    my_list.remove_task(input())  
  elif userInput == 3:
    print("Enter an important task: ")
    my_list.task_at_front(input())
  elif userInput == 4:
    my_list.print_list()
  elif userInput == 5:
    my_list.search(input())

print("Thank you for using the program!") #if the user enters 4

#future advancements: data from to do list can be written to a file
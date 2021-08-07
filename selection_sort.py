class DLNode:
    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sorted_to = None
        self.the_claw = None

    def print_forward(self):
        if self.head == None:
            print("No list to print")
        else:
            print("Printing List Forward:")
            runner = self.head
            print_counter=0
            while(runner != None):
                print(runner.value)
                # print("\t", runner.previous)
                # print("\t",runner)
                # print("\t", runner.next)
                runner = runner.next
                print_counter +=1
                if print_counter > 15:
                    return
        return self

    def print_backward(self):
        if self.tail == None:
            print("No list to print")
        else:
            print("Printing List Backward:")
            runner = self.tail
            while(runner != None):
                print(runner.value)
                runner = runner.previous
        return self

    def add_to_front(self, val):
        if self.head == None:
            # print("Empty list detected.  Adding new head, which is also the tail!")
            self.head = DLNode(value = val, previous = None, next = None)
            self.tail = self.head
        else:
            self.head = DLNode(value = val, previous = None, next = self.head)
            self.head.next.previous = self.head
        return self

    def add_to_back(self, val):
        if self.tail == None:
            # print("Empty list detected.  Adding new tail, which is also the head.  Using add_to_front()")
            self.add_to_front(val)
        else:
            self.tail = DLNode(value = val, previous = self.tail, next = None)
            self.tail.previous.next = self.tail
        return self

    def insert_new_node_at(self, val, position):
        if self.head == None:
            print("There is no list to insert into.  Calling add_to_front")
            self.add_to_front(value=val)
        else:
            runner = self.head
            for counter in range(1,position):
                runner = runner.next
            node_to_insert=DLNode(value=val, previous=runner.previous, next=runner)
            if(runner.previous != None):
                runner.previous.next = node_to_insert
            node_to_insert.next.previous = node_to_insert
        return self



    def find_lowest_value(self):
        if self.head == None:
            print("There is no list to sort")
        else:
            runner = self.head
            self.the_claw = self.head
            while(runner != None):
                print("runner.value:", runner.value, "the_claw.value:",self.the_claw.value)
                if runner.value < self.the_claw.value:
                    print("runner.value:",runner.value,"is less than what the_claw is holding:",self.the_claw.value)
                    self.the_claw = runner
                runner = runner.next
            print("Minimum value found:",self.the_claw.value)

    def selection_sort(self):
        print("**** BEGINNING OF SELECTION SORT ****")
        if self.head == None:
            print("There is no list to sort")
        else:
            self.sorted_to = self.head
            insertion_runner = self.head
            while(insertion_runner.next != None):
                scan_runner = self.sorted_to
                self.the_claw = self.sorted_to
                # Scan the whole list and have the_claw grab the DLNode with the smallest value
                while(scan_runner != None):
                    if scan_runner.value < self.the_claw.value:
                        self.the_claw = scan_runner
                    scan_runner = scan_runner.next
                ## CODE TO "BREAK" MINIMUM NODE OUT OF THE CHAIN
                if self.sorted_to == self.the_claw: # If the_claw == self.sorted to, than nothing needs to move and none of the rest of the loop needs to execute...
                    self.sorted_to = self.the_claw.next # ...just need to move the_claw forward one and start over
                if self.sorted_to == self.head: # Self.sorted_to will only be the self.head at the very beginning.  During the first run, whatever item the claw grabs will be the smallest item in the list.
                    self.head = self.the_claw   # ... so set that item equal to the new head.  This situation won't occur again for the rest of the sort because self.sorted_to will increment past the head of the list.
                if self.the_claw.previous != None:  # If there is a node before the node to be removed...
                    self.the_claw.previous.next = self.the_claw.next    # ...link it to the node after the node to be removed  ## THIS IS THE LINE THAT SETS LAST NODE's .next TO NONE
                if self.the_claw.next != None:  # If there is a node after the node to be removed...
                    self.the_claw.next.previous = self.the_claw.previous    # ...link it to the node before the node to be removed
                ## INSERTION
                insertion_runner = self.sorted_to   # Start looking to insert at the point where the list is known to be sorted
                while(self.the_claw.value > insertion_runner.value):    # Scan the list until a value bigger than the node to be inserted
                    insertion_runner = insertion_runner.next
                # CODE TO INSERT NODE HELD BY the_claw
                if insertion_runner.previous == None:   # ...If the point of insertion has NO previous node...
                    self.the_claw.previous = None   # ...set the node to be interted's previous to none
                if insertion_runner.previous != None:   # ...If the point of insertion has a node before it...
                    insertion_runner.previous.next = self.the_claw  # ...set the previous node's next to the node to be inserted...
                    self.the_claw.previous = insertion_runner.previous # ...set the node to be inserted's previous to the previous node
                if insertion_runner != None:    # If the point of insertion is not the end of the list
                    self.the_claw.next = insertion_runner   # ...set the node to be inserted's next to the point of insertion
                    insertion_runner.previous = self.the_claw   #...set the point of insertion's previous to the node to be inserted
                self.sorted_to=self.the_claw.next   # update the starting point of the insertion scanner to the point at where the list is now sorted
            self.tail = insertion_runner    # set the last node as the list's tail




        

list = DLList()
# list.add_to_front(5).add_to_front(4).add_to_front(3).add_to_front(2).add_to_front(1).add_to_front(0).print_forward().print_backward()
# list.add_to_back(0).add_to_back(1).add_to_back(2).add_to_back(3).add_to_back(4).add_to_back(5).print_forward().print_backward()
# list.add_to_back(0).add_to_back(1).add_to_back(2).add_to_back(3).add_to_back(4).add_to_back(5)
# list.insert_new_node_at(6,2).print_forward()

list.add_to_back(33).add_to_back(22).add_to_back(99).add_to_back(88).add_to_back(55).add_to_back(11).add_to_back(66).add_to_back(44).add_to_back(0).add_to_back(77)
list.print_forward()
list.selection_sort()
list.print_forward()
list.print_backward()
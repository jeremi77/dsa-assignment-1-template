"""Assignment 2: Linked Lists - University Helpdesk Ticket Queue."""
class Ticket:
    def __init__(self, ticket_id, student_name, issue):
        self.ticket_id = ticket_id
        self.student_name = student_name
        self.issue = issue
        self.next = None

class TicketQueue:
    def __init__(self):
        self.head = None

    # 1. Enqueue Ticket: Add a new ticket to the end of the queue
    def enqueue(self, ticket_id, student_name, issue):
        new_ticket = Ticket(ticket_id, student_name, issue)
        
        # If the queue is empty, the new ticket becomes the head
        if not self.head:
            self.head = new_ticket
            return
            
        # Otherwise, traverse to the very last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_ticket

    # 2. Priority Insert: Insert a new ticket immediately after a specified ticket ID
    def priority_insert(self, target_id, ticket_id, student_name, issue):
        current = self.head
        
        # Search for the target ticket ID
        while current:
            if current.ticket_id == target_id:
                new_ticket = Ticket(ticket_id, student_name, issue)
                # Link the new ticket to the rest of the chain first
                new_ticket.next = current.next
                # Link the target ticket to the new ticket
                current.next = new_ticket
                return True
            current = current.next
            
        print(f"Error: Ticket ID {target_id} not found. Priority insertion failed.")
        return False

    # 3. Resolve Ticket: Delete a resolved ticket given its ID
    def resolve_ticket(self, ticket_id):
        current = self.head
        prev = None
        
        while current:
            if current.ticket_id == ticket_id:
                # Case 1: The ticket to delete is the head of the queue
                if prev is None:
                    self.head = current.next
                # Case 2: The ticket is in the middle or end
                else:
                    prev.next = current.next
                return True
                
            prev = current
            current = current.next
            
        print(f"Error: Ticket ID {ticket_id} not found. Cannot resolve.")
        return False

    # 4. Find Middle Ticket: Single pass execution using Fast/Slow pointers
    def find_middle_ticket(self):
        if not self.head:
            return None
            
        slow = self.head
        fast = self.head
        
        # Fast moves 2 steps, slow moves 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # When fast reaches the end, slow points exactly to the middle
        return slow

    # 5. Reverse Queue: In-place reversal manipulating only pointers
    def reverse_queue(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # Temporarily save the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev one step forward
            current = next_node       # Move current one step forward
            
        self.head = prev              # Update head to point to the new front

    # 6. Display Queue: Traversal method to print all tickets
    def display_queue(self):
        current = self.head
        if not current:
            print("The ticket queue is currently empty.")
            return
            
        print("\n--- Current IT Helpdesk Queue ---")
        while current:
            print(f"[ID: {current.ticket_id}] Student: {current.student_name} | Issue: {current.issue}")
            current = current.next
        print("---------------------------------")


# --- Demonstration of Functionality ---
if __name__ == "__main__":
    queue = TicketQueue()
    
    # Test Enqueue
    queue.enqueue(101, "Kwame", "WiFi login issues in Library")
    queue.enqueue(102, "Ama", "Moodle password reset")
    queue.enqueue(103, "Kofi", "Lab computer won't boot")
    queue.display_queue()
    
    # Test Priority Insert
    queue.priority_insert(102, 999, "Abena", "CRITICAL: Exam portal crashed")
    queue.display_queue()
    
    # Test Find Middle
    mid = queue.find_middle_ticket()
    if mid:
        print(f"Middle Ticket is ID: {mid.ticket_id} ({mid.student_name})")
        
    # Test Resolve (Delete)
    queue.resolve_ticket(102)
    queue.display_queue()
    
    # Test Reverse
    print("\nReversing the queue for priority override...")
    queue.reverse_queue()
    queue.display_queue()


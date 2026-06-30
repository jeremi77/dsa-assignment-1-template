"""Assignment 1: Arrays - University Course Registration Analytics."""
registrations = [1023, 1050, 1023, 1102, 1050, 1023, 1201, 1102, 1300, 1023]

# 1. Most Frequent Registrant
def most_frequent_registrant(regs):
    """Finds the student ID that appears most frequently."""
    if not regs:
        return None
    
    counts = {}
    for student_id in regs:
        counts[student_id] = counts.get(student_id, 0) + 1
        
    # Return the key associated with the maximum value in the dictionary
    return max(counts, key=counts.get)


# 2. Ordered Deduplication
def ordered_deduplication(regs):
    """Removes duplicates while preserving the first appearance order."""
    seen = set()
    result = []
    
    for student_id in regs:
        if student_id not in seen:
            seen.add(student_id)
            result.append(student_id)
            
    return result


# 3. First Unique Student
def first_unique_student(regs):
    """Finds the first student ID that appears exactly once."""
    counts = {}
    
    # First pass: Count all frequencies
    for student_id in regs:
        counts[student_id] = counts.get(student_id, 0) + 1
        
    # Second pass: Find the first ID with a count of 1
    for student_id in regs:
        if counts[student_id] == 1:
            return student_id
            
    return None


# 4. Contiguous Subarray Sum
def has_contiguous_subarray_sum(regs, target):
    """Checks if any contiguous subarray sums to the target value T."""
    # We use a set to store prefix sums. Initialize with 0 to handle 
    # cases where a subarray starting from the 0th index equals the target.
    prefix_sums = {0}
    current_sum = 0
    
    for student_id in regs:
        current_sum += student_id
        
        # If (current_sum - target) exists in our seen prefix sums, 
        # the subarray between that previous point and here sums to target.
        if (current_sum - target) in prefix_sums:
            return True
            
        prefix_sums.add(current_sum)
        
    return False

# --- Testing the functions ---
if __name__ == "__main__":
    print(f"1. Most Frequent: {most_frequent_registrant(registrations)}")
    print(f"2. Ordered Deduplication: {ordered_deduplication(registrations)}")
    print(f"3. First Unique: {first_unique_student(registrations)}")
    
    target_sum = 1050 + 1023 + 1201  # Example target: 3274
    print(f"4. Contiguous Sum to {target_sum}: {has_contiguous_subarray_sum(registrations, target_sum)}")


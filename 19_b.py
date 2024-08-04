 # Initialize an empty list to represent the queue
queue = []

# Simulate enqueue operations (adding elements to the end of the queue)
queue.append(1)
print("Enqueued 1:", queue)
queue.append(2)
print("Enqueued 2:", queue)
queue.append(3)
print("Enqueued 3:", queue)

# Simulate dequeue operations (removing elements from the front of the queue)
if queue:
    removed_element = queue.pop(0)
    print("Dequeued:", removed_element, "New Queue:", queue)
else:
    print("Queue is empty, cannot dequeue.")

if queue:
    removed_element = queue.pop(0)
    print("Dequeued:", removed_element, "New Queue:", queue)
else:
    print("Queue is empty, cannot dequeue.")

if queue:
    removed_element = queue.pop(0)
    print("Dequeued:", removed_element, "New Queue:", queue)
else:
    print("Queue is empty, cannot dequeue.")

# Attempt to dequeue from an empty queue
if queue:
    removed_element = queue.pop(0)
    print("Dequeued:", removed_element, "New Queue:", queue)
else:
    print("Queue is empty, cannot dequeue.")

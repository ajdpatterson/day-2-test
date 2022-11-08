# 1. Create an empty list called `task_list`

# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'

# 3. Print out `task_list`

# 4. Remove the last task

# 5. Print out `task_list`

# 6. Print out the number of elements in `task_list`
task_list = []
task_list = ["make dinner", "brush teeth", "cook dinner", "wash dishes"]
print(f"Todo: {task_list}")
done_task = task_list.pop()
print(f"Completed: {done_task}")
print(f"Todo: {task_list}")
print(f"Number of tasks remaining: {len(task_list)}")
def solution(target, position, speed):
  cars = [[p, s] for p, s in zip(position, speed)]
  stack = []

  for p, s in sorted(cars)[::-1]:
    time = (target - p) / s
    stack.append([time])
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
      stack.pop()
  return len(stack)

# T: O(log(n) * n) -> sorting then 1 for loop through
# S: O(n) -> extra space for stack and cars

print(solution(12, [10,8,0,5,3], [2,4,1,1,3]))

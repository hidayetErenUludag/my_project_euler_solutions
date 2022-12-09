def clac():
  count = 1  # Initialize the running total of the sum to 1 for the center point
  current_num = 1
  square = 1
  while square <= 2:
    # Compute the corner points of the square using simple arithmetic
    a = current_num + square * 2
    b = a + square * 2
    c = b + square * 2
    d = c + square * 2

    # Add the corner points to the running total of the sum
    count += a + b + c + d

    # Move to the next square and update the current number
    current_num = d
    square += 2

  # Print the result
  print(count)

# Test the function
clac()
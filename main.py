def calculate_calibration_value(line):
  # Find the first and last digits in the line
  first_digit = next((int(char) for char in line if char.isdigit()), 0)
  last_digit = next((int(char) for char in reversed(line) if char.isdigit()), 0)

  # Combine to form a two-digit number
  calibration_value = first_digit * 10 + last_digit

  return calibration_value
  
# Read lines from a file
file_path = "test.txt"  # Update with your file path
with open(file_path, "r") as file:
    lines = file.readlines()
  
# Calculate calibration values for each line
calibration_values = [calculate_calibration_value(line.strip()) for line in lines]

# Sum of all calibration values
total_calibration_sum = sum(calibration_values)

# Print results
for i, line in enumerate(lines):
    print(f"Line {i + 1}: {line}, Calibration Value: {calibration_values[i]}")

print(f"\nSum of Calibration Values: {total_calibration_sum}")
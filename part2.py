import re

def calculate_calibration_value(line):
  spelled_out_to_numeric = {
      'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
  }
  spelled_out_digits = re.findall(r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d+)', line, re.IGNORECASE)
  numeric_digits = [spelled_out_to_numeric[digit.lower()] if digit.lower() in spelled_out_to_numeric else int(digit) for digit in spelled_out_digits]
  numeric_digits = [digit for digit in numeric_digits if 0 <= digit <= 9]  # Filter out non-digit elements

  if len(numeric_digits) < 2:
      return 0  # Return 0 for lines with less than 2 digits

  first_digit = numeric_digits[0]
  last_digit = numeric_digits[-1]
  calibration_value = first_digit * 10 + last_digit

  return calibration_value


# Example lines
lines = [
  "two1nine",
  "eightwothree",
  "abcone2threexyz",
  "xtwone3four",
  "4nineeightseven2",
  "zoneight234",
  "7pqrstsixteen"
]
# Calculate calibration values for each line
calibration_values = [calculate_calibration_value(line) for line in lines]
# Sum of all calibration values
total_calibration_sum = sum(calibration_values)

# Print results
for i, line in enumerate(lines):
    print(f"Line {i + 1}: {line}, Calibration Value: {calibration_values[i]}")
print(f"\nSum of Calibration Values: {total_calibration_sum}")
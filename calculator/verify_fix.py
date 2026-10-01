from pkg.calculator import Calculator

calc = Calculator()

# Test the bug case: 3 + 7 * 2 should be 17, not 20
result = calc.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")
assert result == 17, f"Expected 17, got {result}"

# Additional tests
print(f"10 - 3 * 2 = {calc.evaluate('10 - 3 * 2')}")  # should be 4
print(f"5 * 2 + 3 = {calc.evaluate('5 * 2 + 3')}")    # should be 13
print(f"8 / 2 + 1 = {calc.evaluate('8 / 2 + 1')}")    # should be 5

print("All tests passed!")
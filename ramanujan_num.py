# Program to find Ramanujan number (smallest number that can be expressed as sum of two cubes in two different ways)

limit = 2000  # Set a limit to search for such numbers
ramanujan_numbers = []

# Check for all pairs (a, b) such that a^3 + b^3 = c^3 + d^3
for a in range(1, int(limit**(1/3)) + 1):
    for b in range(a, int(limit**(1/3)) + 1):  # Start b from a to avoid duplicate pairs
        sum_of_cubes = a**3 + b**3
        for c in range(a+1, int(limit**(1/3)) + 1):
            for d in range(c, int(limit**(1/3)) + 1):
                if sum_of_cubes == c**3 + d**3:
                    ramanujan_numbers.append((sum_of_cubes, (a, b), (c, d)))

# Display the smallest Ramanujan number
for number, pair1, pair2 in ramanujan_numbers:
    if number == 1729:
        print(f"Ramanujan number: {number}")
        print(f"Two ways: {pair1[0]}^3 + {pair1[1]}^3 = {pair2[0]}^3 + {pair2[1]}^3")
        break

        
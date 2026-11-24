# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline:
    # 1. Create an empty stack.
    # 2. Loop through each token.
    # 3. If the token is a number, add it to the stack.
    # 4. If it is an operator, remove the last two numbers.
    # 5. Perform the operation and add the result to the stack.
    # 6. Return the final result.

    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                result = int(a / b)

            stack.append(result)

    return stack.pop()


def decode_string(s):
    # Outline:
    # 1. Create an empty stack.
    # 2. Read each character in the string.
    # 3. If it is a number, save the repeat count.
    # 4. If it is an opening bracket, save the current string and number.
    # 5. If it is a closing bracket, repeat the current string.
    # 6. Return the decoded string.

    stack = []
    current = ""
    number = 0

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)

        elif char == "[":
            stack.append((current, number))
            current = ""
            number = 0

        elif char == "]":
            previous, count = stack.pop()
            current = previous + current * count

        else:
            current += char

    return current


def daily_temperatures(temps):
    # Outline:
    # 1. Create a results list filled with zeros.
    # 2. Create an empty stack.
    # 3. Loop through each day's temperature.
    # 4. Check if today's temperature is warmer than previous days.
    # 5. Calculate how many days those temperatures waited.
    # 6. Add the current day to the stack.
    # 7. Return the results.

    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous = stack.pop()
            result[previous] = i - previous

        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    # 1. Check if the grid is empty.
    # 2. Go through every position in the grid.
    # 3. If unvisited land is found, increase the island count.
    # 4. Use a stack to explore connected land.
    # 5. Mark visited land so it is not counted again.
    # 6. Return the number of islands.

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                stack = [(r, c)]

                while stack:
                    row, col = stack.pop()

                    if (row, col) in visited:
                        continue

                    visited.add((row, col))

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr = row + dr
                        nc = col + dc

                        if (0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] == "1" and
                            (nr, nc) not in visited):
                            stack.append((nr, nc))

    return islands


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()

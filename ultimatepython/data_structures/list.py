def main():
    # This is a list of one-letter strings where
    # 'a' is a string at index 0 and
    # 'e' is a string at index 4
    letters = ["a", "b", "c", "d", "e"]

    # This is a list of integers where
    # 1 is an integer at index 0
    # 5 is an integer at index 4
    numbers = [1, 2, 3, 4, 5]

    # Print letters and numbers side-by-side using the `zip`
    # function. Notice that we pair the letter at index 0
    # with the number at index 0, and do the same for the
    # remaining indices
    for letter, number in zip(letters, numbers):
        print("letter_and_number", letter, number)

    # The for loop above worked well because the lengths
    # of `letters` and `numbers` are equal
    assert len(letters) == len(numbers)

    # If you want to the see the indices and values of a
    # list side-by-side, you can use `enumerate`
    for index, number in enumerate(numbers):
        print("number", index, number)

    # Lists can be nested at arbitrary levels
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("matrix", matrix)

    # Something to know about lists is that they are mutable
    mutable = []
    for _ in range(5):  # [0, ..., 0]
        mutable.append(0)
    mutable.pop()  # pop out the fifth zero
    mutable[0] = 100  # first item
    mutable[1] = 4  # second item
    mutable[-1] = 30  # last item
    mutable[-2] = 50  # second to last item
    print("mutable", mutable)


if __name__ == "__main__":
    main()
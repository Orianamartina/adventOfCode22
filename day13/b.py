from itertools import zip_longest

FILENAME = "day13/13input.txt"


def compare(left, right):
    z = zip_longest(left, right, fillvalue=None)

    for p in z:
        l, r = p
        res = None

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            elif l > r:
                return False

        elif isinstance(l, list) and isinstance(r, list):
            res = compare(l, r)

        elif isinstance(l, int) and isinstance(r, list):
            res = compare([l], r)
        elif isinstance(l, list) and isinstance(r, int):
            res = compare(l, [r])

        # check if one side has run out of items
        elif l == None:
            return True
        elif r == None:
            return False

        # return result from any recursive checks
        if res != None:
            return res


def part_one():
    part_one = 0

    s_pairs = [pair.split("\n")
               for pair in open(FILENAME).read().split("\n\n")]
    pairs = list(map(lambda p: [eval(i) for i in p], s_pairs))

    for i, pair in enumerate(pairs, start=1):
        part_one += i if compare(pair[0], pair[1]) > 0 else 0
        print(i)if compare(pair[0], pair[1]) > 0 else 0
    return part_one


def part_two():
    """
        the index of an item in a sorted list will equal the sum of items in 
        the list against which it passes the sorting test. so instead of 
        sorting the whole list including the extra values, we can just test 
        the extra values against each other value and sum how many times it 
        passes.
    """
    pairs = [eval(l.strip()) for l in open(FILENAME).readlines() if l != "\n"]
    sum_two = 1     # add one for 1-indexing
    sum_six = 2     # add one for 1-indexing, another 1 to account for [[2]]
    for p in pairs:
        sum_two += 1 if compare(p, [[2]]) else 0
        sum_six += 1 if compare(p, [[6]]) else 0

    return sum_two * sum_six


def main():
    print("Part one: ", part_one())
    print("Part two: ", part_two())


if __name__ == "__main__":
    main()

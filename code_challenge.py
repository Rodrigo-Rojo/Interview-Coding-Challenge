def solution(A):
    list_length = len(A)

    def sort_list(my_list):
        TAILS = 1
        HEADS = 0
        for index in range(list_length - 1):
            if my_list[index] % 2 == 0:
                my_list.append(TAILS)
            else:
                my_list.append(HEADS)
        return my_list

    def counter(my_list):
        count = 0
        for index in range(list_length):
            if A[index] != my_list[index]:
                count += 1
        return count

    list_a = sort_list([0])
    list_b = sort_list([1])
    if counter(list_a) < counter(list_b):
        return counter(list_a)
    else:
        return counter(list_b)


def solution(S):
    option1 = ["XXX", "XX", "X.X", ".X.", "X"]
    option2 = ["X.X", "XXX", "XX", ".X.", "X"]
    option3 = ["XX", "XXX", "X.X", ".X.", "X"]


    def calculate(options):
        str_strip = f".{S}."
        count = 0
        for option in options:
            while str_strip.find(option):
                if option in str_strip:
                    str_strip = str_strip.replace(option, "...", 1)
                    count += 1
                if not option in str_strip:
                    break
        return count
    return min([calculate(option1), calculate(option2), calculate(option3)])

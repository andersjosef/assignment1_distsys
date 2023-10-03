import glob


def sorted_word_count():
    string = ""
    for file in glob.glob("input/file*.txt"):
        with open(file, "r") as f:
            string += f.read() + " "

    count = dict()
    words = string.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_count)

if __name__ == "__main__":
    # print("freq = ", sorted_word_count())
    my_dict = sorted_word_count()
    # print(my_dict)
    my_list = list()
    for k in my_dict:
        my_list.append(f"{k}: {my_dict[k]}")
    print(my_list)

    # test_dic = dict()
    # for i in my_list:
    #     i = i.split(": ")
    #     print(i)
    # print(test_dic)
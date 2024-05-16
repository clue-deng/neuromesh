# Task 1
# Given two strings source and target, return the minimum number of subsequences of source
# such that their concatenation equals target. If the task is impossible, return -1.
def number_of_subsequence(source, target):
    # 首先检查target里有没有source里的要素，没有就-1
    for char in target:
        if char not in source:
            return -1

    # 有要素，必定可以组成，数需要多少分部
    formation_counts = 0

    # 利用pointer巡视整个target（可以跳跃），一个一个要素看，align到source的要素上
    # 两个while loop的worst case performance会到O（len（source)*len（target)),不过可以处理当source有重复
    # 要素的情况，返回出最小值的sequence number
    target_ptr = 0
    while target_ptr < len(target):
        formation_counts += 1
        source_ind = 0
        # 在source中拼凑最长分支部分,两个pointer(index)小于source/target长度
        while source_ind < len(source) and target_ptr < len(target):
            # 看看是否找到匹配的元素，若找到，target的pointer移前。
            if target[target_ptr] == source[source_ind]:
                target_ptr += 1
            # 不论找到与否，都要source的pointer前进一个位置，总会找到一个匹配的，直到source pointer超出
            # source的长度
            source_ind += 1

    return formation_counts



if __name__ == '__main__':
    print(number_of_subsequence("abc", "abcbc"))
    print(number_of_subsequence("abc", "acdbc"))
    print(number_of_subsequence("xyz", "xzyxz"))


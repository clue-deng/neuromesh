# Task 2
# 本体运用fist in last out的stack原理可以帮助消减正确的括号匹配，可以使用两个list来完成

def parentheses_inspection(lines):
    # 用来记录每条线的括号情况
    output_list = []
    # 巡视每条线
    for line in lines:
        # 添加每一条原先的line
        output_list.append(line)
        # 只添加左括号的index位置到list里，然后根据匹配的右括号次数消除
        # 剩下的index会是没有被匹配到的左括号
        left = []
        # 只添加右括号的list
        right = []
        # 在每一条line生成的结果，最后会放到output里
        result_line = list(line)

        # 在每条线中巡视每个字符，查看是否有匹配括号
        for i in range((len(line))):
            if line[i] == '(':
                left.append(i)  # 左括号的index
            elif line[i] == ')':
                if left:  # 左括号list不为空
                    left.pop()  # 匹配到一个左括号，弹出
                else:  # 为空，表示右括号多余的空号
                    right.append(i)  # 记录多余的右括号位置

        # 建造
        for elem in left:
            result_line[elem] = 'x'
        for elem in right:
            result_line[elem] = '?'
        for i in range(len(result_line)):
            # 把不是？或x的变成空格
            if result_line[i] != '?' and result_line[i] != 'x':
                result_line[i] = ' '

        # 添加建造后的结果
        output_list.append(''.join(result_line))
    return output_list

test_inputs = [
    "bge))))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

results = parentheses_inspection(test_inputs)
for result in results:
    print(result)
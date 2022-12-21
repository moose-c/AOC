lst = open('2e_input.txt').read().splitlines()
lst = ['(' + sum + ')' for sum in lst]

def calculate_sum(sum):
    res = sum[1]
    for i, char in enumerate(sum):
        if char == '(':
            sub_sum = sum[i:]
            calculate_sum(sub_sum)
        elif char in '*+':
            pass
            



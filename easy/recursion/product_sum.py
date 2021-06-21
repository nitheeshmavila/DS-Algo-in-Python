
def product_sum(array, depth=1):
    sum = 0
    for item in array:
        if type(item) is list:
            sum = product_sum(item, depth+1)
        sum += item
    
    return sum * depth
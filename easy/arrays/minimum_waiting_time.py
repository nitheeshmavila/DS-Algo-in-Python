
# O(N^2 logN) Time where N is the no of elements in this array
#O(1) SPACE
def minimumWaitingTime(queries):
    queries.sort()
    total_waiting_time = 0
    for i in rangelen(queries)):
        waiting_time = waiting_time_at_index[i-1] + queries[i-1] 
        idx = i - 1
        while idx >= 0:
            waiting_time += queries[idx]
            idx -= 1
        total_waiting_time += waiting_time
    return total_waiting_time


# O(N lonN) Time where N is the no of elements in this array
# O(N) space
def minimumWaitingTime(queries):
    queries.sort()
    total_waiting_time = 0
    waiting_time_at_index = {0:0}
    for i in range(1, len(queries)):
        waiting_time = waiting_time_at_index[i-1] + queries[i-1]
        waiting_time_at_index[i] = waiting_time 
        total_waiting_time += waiting_time
    return total_waiting_time


# O(N lonN) Time where N is the no of elements in this array
def minimumWaitingTime(queries):
    queries.sort()
    total_waiting_time = 0
    for i, query in enumerate(queries):
        total_waiting_time += (query * (len(queries) - i+1))
    return total_waiting_time
print(minimumWaitingTime([3,2,1,2,6]))
        
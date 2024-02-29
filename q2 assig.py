# Take input for the number of test cases
T = int(input())

# Initialize an empty list to store the output counts for each test case
a = []

# Iterate through each test case
for _ in range(T):
    # Input the values for the number of players and their height
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))

    # Initialize count for players to be shot
    count = 0
    
    # Iterate through the heights and count the players taller than Gi-Hun and Ali
    for h in heights:
        if h > K:
            count += 1
    
    # Append the count to the list of output counts
    a.append(count)
# Print the output counts for all test cases
for ans in a:
    print(ans)

#Time complexity is O(T*N) because we iterate over the list of length N for T times.
#Space complexity is O(1) since we are using a integer variable count to store the result.
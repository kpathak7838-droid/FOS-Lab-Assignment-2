# Banker's Algorithm Implementation

def bankers_algorithm():
    n = int(input("Enter number of processes: "))
    r = int(input("Enter number of resources: "))

    print("\nEnter Allocation Matrix:")
    allocation = []
    for i in range(n):
        row = list(map(int, input(f"P{i}: ").split()))
        allocation.append(row)

    print("\nEnter Maximum Matrix:")
    maximum = []
    for i in range(n):
        row = list(map(int, input(f"P{i}: ").split()))
        maximum.append(row)

    print("\nEnter Available Resources:")
    available = list(map(int, input().split()))

    # Task 2: Need Matrix
    need = []
    for i in range(n):
        row = []
        for j in range(r):
            row.append(maximum[i][j] - allocation[i][j])
        need.append(row)

    print("\nNeed Matrix:")
    for i in range(n):
        print(f"P{i}: {need[i]}")

    # Task 3 & 4: Safety Algorithm
    finish = [False] * n
    safe_sequence = []
    work = available.copy()

    while len(safe_sequence) < n:
        allocated = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(r)):
                    # Allocate
                    for j in range(r):
                        work[j] += allocation[i][j]

                    safe_sequence.append(f"P{i}")
                    finish[i] = True
                    allocated = True

        if not allocated:
            break

    # Result
    print("\n--- Result ---")
    if len(safe_sequence) == n:
        print("System is in SAFE state")
        print("Safe Sequence:", " -> ".join(safe_sequence))
    else:
        print("System is in UNSAFE state (Deadlock may occur)")


# Run program
bankers_algorithm()

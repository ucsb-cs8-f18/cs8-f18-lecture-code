def fac_loop(N):
    result  = 1
    for i in range(1, N+1):
        result = result *i

    return result


def fac(N):
    # Step 1: Solve for input where the answer is trivial
    # Stopping condition , base case
    print("Inside fac, N = ", N)
    if N <=1:
        return 1

    rest = fac(N-1)
    return rest * N


def facWrong(N):
    return N* facWrong(N-1)

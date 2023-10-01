import rebecca.plot as plt

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(nums)

plt.plot({"nums": nums, "n": n}, title="inital state").savefig(filename="initial state")

for i in range(n):
    plt.plot({"nums": nums, "n": n}, title=f"{i}th iteration").savefig(filename="initial state")


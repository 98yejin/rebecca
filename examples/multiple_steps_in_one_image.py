import rebecca.plot as plt

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(nums)

plt.subplot({"nums": nums, "n": n}, title="inital state")
for i in range(n):
    plt.subplot({"nums": nums, "n": n}, title=f"{i}th iteration")
plt.savefig(filename="filename.png", title="increasing list")

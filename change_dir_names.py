import os

res = os.listdir("../")

# os.mkdir("../testDir")


# print(res)
# print("testDir1" in res)


for i in range(1, len(res) + 1):
    new_name = f"{i:03}_{res[i -1]}"
    print("\033[93m\033[1m >> \033[0m", new_name)
    os.rename(f"../{res[i -1]}", f"../{new_name}")

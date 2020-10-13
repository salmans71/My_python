d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Actual dictionary", d)
ascen = sorted(d.items(), key=lambda kv:kv[1])
print(f"Ascending order of dictionary:{ascen}")
descen = sorted(d.items(), key=lambda kv:kv[1] , reverse=True)
print(f"Ascending order of dictionary:{descen}")
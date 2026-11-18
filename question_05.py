students = {"Sam": [95, 90, 92], "Ali": [80, 85, 90], "Sara": [98, 95, 94]}

for name, scores in students.items():
    average = sum(scores) / len(scores)

    if average > 90:
        print(f"{name}: Average {average:.1f} - Honor Roll")
    else:
        print(f"{name}: Average {average:.1f}")

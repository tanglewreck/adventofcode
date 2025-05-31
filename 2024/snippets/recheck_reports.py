# coding: utf-8
reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]]
for report in reports:
    a2 = report.copy()
    print(f"report: {a2}: ", end="")
    #print()
    if not check_row_safety(a2):
        for i, x in enumerate(a2):
            a2copy = a2.copy()
            removed_item = a2copy.pop(i)
            # print(f"Item {i} popped from a2: {a2copy}")
            now_safe = False
            if check_row_safety(a2copy, i):
                print(f"safe with item {i} removed: {removed_item}: ")
                # print(f"original row: {a2}")
                # print(f"popped row: {a2copy}")
                # print()
                now_safe = True
                break
        if not now_safe:
            print(f"not safe, no matter what")
    else:
        print(f"already safe")

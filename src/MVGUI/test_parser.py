
filename = "ALLTEST_OK_TestReport_2025-03-27_07_45_03.txt"


with open(filename, "r") as file:
    for line in file:
        line.strip()
        if "test" in line:
            print(line)
        elif "ok" in line:
            print(line)

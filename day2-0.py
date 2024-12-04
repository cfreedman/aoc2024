import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day2")

def main():
    reports = []
    with open(file_path) as f:
        for line in f:
            reports.append([int(num) for num in line.split()])

    total_safe = 0
    for report in reports:
        increasing, safe = None, True
        for i in range(1, len(report)):
            if abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
                safe = False
                break
            elif (report[i] > report[i - 1] and increasing == -1) or (report[i] < report[i - 1] and increasing == 1):
                safe = False
                break

            if not increasing:
                increasing = 1 if report[i] > report[i - 1] else -1
        
        total_safe += 1 if safe else 0
    
    print(total_safe)
    return total_safe

if __name__ == "__main__":
    main()
import bisect

def determine_grades(scores, breakpoints=[30, 40, 50, 60, 70], grades='FDCBA'):
    i = bisect.bisect(breakpoints, scores)
    return grades[i]

score = int(input("What was your score?"))
determine_grades(score)
print()

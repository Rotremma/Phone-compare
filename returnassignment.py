# 70 -100 = A 
# 60 - 69 = B
# 50 - 59 = C 
# 45 - 49 = D 
# 40 - 44 = E 
# 0 - 39 = F

def grade_student(score,total):
    your_score = (score/total)*100
    if your_score <= 39:
        return f"you scored {score} out of {total} which is F"
    elif your_score <= 44:
        return f"you scored {score} out of {total} which is E"
    elif your_score <= 49:
        return f"you scored {score} out of {total} which is D"
    elif your_score <= 59:
        return f"you scored {score} out of 1{total} which is C"
    elif your_score <= 69:
        return f"you scored {score} out of {total} which is B"
    elif your_score <= 100:
        return f"you scored {score} out of {total} which is A"
    else:
        return "you are done"


print(grade_student(35,100))
print(grade_student(43,900))
print(grade_student(49,100))
print(grade_student(34,100))
print(grade_student(70,120))
print(grade_student(58,100))
print(grade_student(55,150))
print(grade_student(95,100))








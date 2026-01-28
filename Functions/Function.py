# Example for Function in Python
def check_result(sname, mark):
    if mark >= 40:
        return f"{sname} has passed the exam."
    else:
        return f"{sname} has failed the exam."
print(check_result("Alice", 40))


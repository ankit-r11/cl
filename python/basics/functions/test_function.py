

def display_message():
    print("this is python")

#display_message()

def return_message():
    return "This is returned message"

#print(return_message())


work_hours=[('a',100),('b',400),('c',800)]

def employee_check(work_hours):
    max_hour=0
    emp_name=''
    for name,hour in work_hours:
        if hour>max_hour:
            max_hour=hour
            emp_name=name
        else:
            #continue
            pass
    return (emp_name,max_hour)

#name,hour=employee_check(work_hours)
result=employee_check(work_hours)

print(result[1])


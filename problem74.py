def get_final_salary(current_salary , years_of_services):

    if years_of_services>5:
        bouns=current_salary*0.10

    elif years_of_services<5:
        bouns=current_salary*0.05

    total_salary=current_salary + bouns

    return total_salary

# result1=get_final_salary(10000,6)
# print(result1)

result2=get_final_salary(10000,4)
print(result2)





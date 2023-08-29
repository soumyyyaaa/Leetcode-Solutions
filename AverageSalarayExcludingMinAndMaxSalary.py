def average(salary):
    index_max_sal = max(salary)
    index_min_sal = min(salary)
    total_sal = 0
    for money in salary:
        if money != index_max_sal and money != index_min_sal:
            total_sal += money
    
    return (total_sal / (len(salary) - 2))

salary = [1000, 2000, 3000, 4000]
print(average(salary))

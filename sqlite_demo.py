import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_pay(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 75000)
emp_2 = Employee('Sarah', 'Pascoe', 85000)
#
# c.execute("INSERT INTO employees VALUES ('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay))
#
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_2.first, emp_2.last, emp_2.pay))
#
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

# conn.commit()
# c.execute("INSERT INTO employees VALUES ('Barbara', 'Mitchell', 80000)")

# c.execute("DELETE from employees VALUES ('Jack', 'Test', 90000)")
#
# conn.commit()
# employees.remove()
# c.execute("SELECT * FROM employees WHERE last=?", ('Mitchell',))

# print(c.fetchone())

# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Pascoe'})
#
# print(c.fetchall())
#
# conn.commit()

insert_emp(emp_1)
insert_emp(emp_2)

update_pay(emp_2, 95000)
remove_pay(emp_1)

emps = get_emps_by_name('Pascoe')
print(emps)

conn.close()
# dictionary
details={'emp_name':'asd','emp_age':24,'emp_salary':35000,'gender':'male','emp_id':123456}
print(details)
print(details.values())# used in the vaues identify
print(details.keys())# used in the key pair in the identify
print(details.items())#used in the key pair and value in the identify
for i in details:
    print(i)
    #print(details[i])
for k in details.items():
        print(k)
x=details['emp_age']#accessing the vaue
print(x)
details.update({'company':'fraction'})
print(details)
details['emp_salary']=37000
print(details)
emp_detail={"details1":{'emp_name':'asd','emp_age':24,'emp_salary':35000,'gender':'male','emp_id':123456},
"details2":{'emp_name':'gfh','emp_age':24,'emp_salary':39000,'gender':'male','emp_id':1234}}# nested dictionary
print(emp_detail)

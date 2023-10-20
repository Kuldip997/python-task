key = input("enter keys seperated by space: ").split()
num_list=int(input("Enter the number value of the list: "))

result_dict={}

for i in range(num_list):
    values=input(f"Enter values seperated by space for {key[i]}: ").split()
    result_dict[key[i]]= values
print("/nCreatyed Dictionary:")
print(result_dict)
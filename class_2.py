#counting array time complexity o(N+M)

input_list=[2,5,3,0,2,3,0,3]
count_list=[0]*(max(input_list)+1)
# print(count_list)

for i in input_list:
    count_list[i]=count_list[i]+1

print(count_list)

#commulative sum

for i in range (1,len(count_list)):
    count_list[i]=count_list[i]+count_list[i-1]
print(count_list)



output_list=[0]*len(input_list)
print(output_list)


for i in input_list:
    a=count_list[i]
    output_list[a-1]=i
    count_list[i]=count_list[i]-1


print(output_list)
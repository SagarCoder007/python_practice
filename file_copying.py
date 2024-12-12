
def copy_list(orignal_list):
    copied_list=orignal_list.copy()
    return copied_list
orignal_list=[1,3,4,5,6,7]
copied_list=copy_list(orignal_list)
print("orignal_list",orignal_list)
print("copied_list",copied_list)



list1=[12,3,4,5,3,1,4]
list2 = list1
print(f"{list2}")
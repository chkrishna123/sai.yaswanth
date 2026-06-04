# l=[2,31, 40, 44, 62, 11, 13]
# m=list(map(lambda x: x*2, l))
# print(m)
# f=list(map(lambda x: x*5, l))
# print(f)
# s=list(map(lambda x: x*3, l))
# print(s)

# comp_budget=50000
# def company_budget():
#     total_projects = 100
#     def update_project():
#         nonlocal total_projects
#         global comp_budget
#         total_projects+=20
#         comp_budget+=10000
#     update_project()
#     print("total_projects=", total_projects)
#     print("comap_budget", comp_budget)
# company_budget()
# company_budget()



funcs=[lambda x:x*2,lambda x:x*3,lambda x:x*4 ]
def apply_all(func,values):
    for value in values:
        func(value)
        return value
print(apply_all(funcs,2))

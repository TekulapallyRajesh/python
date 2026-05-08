from tabulate import tabulate
title=["Name","age","department"]
data=[["raj",21,"csm"],
      ["vishal",21,"ai"],
      ["harsh",21,"cse"],
      ["sid",21,"cso"],]

res=tabulate(data,headers=title,tablefmt="fancy_grid")
print(res)
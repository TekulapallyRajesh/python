from scipy import stats
a=[10,30,40,59,47]
res=stats.percentileofscore(a,100)
print(res)
import matplotlib.pyplot as plt
import numpy as np
overs=np.arange(1,11)
scores=[9,4,8,9,2,10,20,5,7,13]
plt.bar(overs,scores,color="green")
plt.title("INDIA SCORE OVER WISE")
plt.xlabel("OVERS FROM 1 TO 10")
plt.ylabel("RUNS BASED ON OVERS")
plt.xticks(overs)
plt.grid(axis='y',linestyle="--")
plt.show()
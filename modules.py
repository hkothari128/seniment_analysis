import math

def distance(n,p1,p2):
    sum=0
    print(p1,p2)
    for i in range(n):
        sum+=math.pow(float(p1[i])-float(p2[i]),2)
    return math.sqrt(sum)
def centroid(cluster,data):
    import operator
    
    sum=(0,0,0)
    for i in range(len(cluster)):
        sum=tuple(map(operator.add, sum, data[cluster[i]-1]))
    sum=list(sum)
    for i in range(len(sum)):
        sum[i]/=len(cluster)
    
    return tuple(sum)



    
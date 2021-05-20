def findMeans(clusters):
        temp = [0]*len(clusters)
        for i in range(len(clusters)):
                sum = 0
                for j in clusters[i]:
                        sum+=j
                if(len(clusters[i])==0):
                        temp[i]=0
                else:
                        temp[i] = round(sum/len(clusters[i]),2)
        return temp

def getNewClusters(data,clusters,means):
        temp = []
        pos = 0
        newClusters = []
        for i in range(len(clusters)):
                newClusters.append([])
        for i in range(len(data)):
                for j in means:
                        temp.append(abs(j-data[i]))
                pos = temp.index(min(temp))
                newClusters[pos].append(data[i])
                temp = []
        return newClusters

x = input("Enter Data: ")
data = []
for i in x.split(" "):
        data.append(int(i))
k = int(input("Enter Number of Clusters (K): "))
clusters = []
for i in range(k):
        clusters.append([])
for i in range(len(data)):
        clusters[i%k].append(data[i])
means = findMeans(clusters)
newClusters = getNewClusters(data,clusters,means)
print("Clusters: ",clusters)
print("Means: ",means)
while newClusters!=clusters:
        clusters = newClusters
        print("Clusters: ",clusters)
        means = findMeans(clusters)
        print("Means: ",means)
        newClusters = getNewClusters(data,clusters,means)
print("Final Clusters: ",newClusters) 

#input
#Enter Data: 2 3 6 8 9 12 15 18 22
#Enter Number of Clusters (K): 3
def car_clusters(cars):
    if cars:    
        result =1
    else: 
        return 0
    for idx in range(len(cars)-1):
        current= cars[idx]
        nex= cars[idx+1] 
        if nex > current :
            result +=1
    return result

print(car_clusters([]))
print(car_clusters([2,5,8]))
print(car_clusters([1,5,5,5, 2,9]))
print(car_clusters([1,5,2,9,19,10]))
print(car_clusters([6,4,2]))
print(car_clusters([3,2,5,1]))
print('-------')
def car_clusters2(cars):
    if cars:
        return sum(leftcar < rightcar for (leftcar,rightcar) in zip(cars, cars[1:]) )+1
    return 0
print(car_clusters2([]))
print(car_clusters2([2,5,8]))
print(car_clusters2([1,5,5,5, 2,9]))
print(car_clusters2([1,5,2,9,19,10]))
print(car_clusters2([6,4,2]))
print(car_clusters2([3,2,5,1]))
from collision import collision as cl

print("isCorrectRect([(-3.4, 1), (9.2, 10)]):", cl.isCorrectRect([(-3.4, 1), (9.2, 10)])) 
print()
print("isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]):", cl.isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))
print()
print("intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]):", cl.intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))
print()
print("intersectionAreaMultiRect([(-3, 1), (9, 10)], [(3, 17), (13, 1)]):",cl.intersectionAreaMultiRect([[(-3, 1), (9, 10)], [(3, 17), (13, 1)]]))
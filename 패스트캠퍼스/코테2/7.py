import numpy as np

def angle_between(p1, p2):  #두점 사이의 각도:(getAngle3P 계산용) 시계 방향으로 계산한다. P1-(0,0)-P2의 각도를 시계방향으로
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        res = np.rad2deg((ang1 - ang2) % (2 * np.pi))
        return res
def getAngle3P(p1, p2, p3, direction="CW"): #세점 사이의 각도 1->2->3
        pt1 = (p1[0] - p2[0], p1[1] - p2[1])
        pt2 = (p3[0] - p2[0], p3[1] - p2[1])
        res = angle_between(pt1, pt2)
        res = (res + 360) % 360
        if direction == "CCW":    #반시계방향
            res = (360 - res) % 360
        return res

def solution(points):
    res = getAngle3P(tuple(points[0]),tuple(points[1]), tuple(points[2]), "CCW")
    if res < 180:
        return "CW"
    elif res == 180:
        return "LINE"
    elif res > 180:
        return "CCW"

print(solution([[0,0],[0,10],[10,5]]))
print(solution([[-2,3],[-2,6],[-2,9]]))
print(solution([[4,7],[-3,5],[2,4]]))
def solution(cards1, cards2, goal):
    point1 = 0 
    point2 = 0
    for i in goal:
        if i  == cards1[point1]:
            if point1 < len(cards1)-1:
                point1 +=1
            else:
                continue 
        elif i == cards2[point2]:
            if point2 < len(cards2)-1:
                point2 +=1
            else:
                continue 
        else:
            return "No"
    return "Yes"

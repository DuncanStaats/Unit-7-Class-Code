"""
Name:Duncan Staats
Date:12/16/2024
Description: Assignment
"""
import math

def slope(point1:tuple,point2:tuple)->float:
    x1, y1 = point1
    x2, y2 = point2
    return (y2 - y1) / (x2 - x1)

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main(point1: tuple, point2: tuple):
    result = slope(point1, point2)
    slope_distance = distance(point1, point2)
    
    print(f"Slope between {point1} and {point2}: {result}")
    print(f"Distance between {point1} and {point2}: {slope_distance}")
    

if __name__ == "__main__":
    main((5, 10), (27, 42))


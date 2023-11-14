class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = []
        for pos, speed in zip(position, speed):
            cars.append((pos, float(speed)))
        
        def key(item):
            return item[0]
        cars.sort(key = key)
        
        i = len(cars) - 1
        stack = []
        
        def time(car):
            return (target - car[0])/car[1]

        while (i >= 0):
            stack.append(cars[i])
            if len(stack) >= 2:
                carAhead = stack[-2]
                carBehind = stack[-1]
                if time(carAhead) >= time(carBehind):
                    stack.pop() 
            i -= 1
        return len(stack)
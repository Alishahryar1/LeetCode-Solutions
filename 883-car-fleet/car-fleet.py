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
        
        cars.sort(key = lambda car: car[0])
        
        stack = []
        
        time = lambda car: (target - car[0])/car[1]

        for i in reversed(range(len(cars))):
            stack.append(cars[i])
            if len(stack) >= 2:
                carAhead = stack[-2]
                carBehind = stack[-1]
                if time(carAhead) >= time(carBehind):
                    stack.pop() 
        
        return len(stack)
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        full_b1 = int(numBottles)
        emp_b1 = 0
        drank1 = 0

        def drink(emp_b, full_b, drank):
            #drink
            emp_b += full_b
            drank += full_b
            # full_b=0


            #exchange
            full_b = emp_b//numExchange
            emp_b = emp_b%numExchange

            if full_b > 0:
                return drink(emp_b, full_b, drank)
            else: 
                return drank
        return drink(emp_b=emp_b1, full_b=full_b1, drank=drank1)
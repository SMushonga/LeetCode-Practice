class Solution(object):
    def solveEquation(self, s):
        sides = s.split('=')
        
        left_sides_plus = sides[0].split('+')
        right_sides_plus = sides[1].split('+')
        x_count = 0
        value = 0
        
        for equation in left_sides_plus:
            if 'x' in equation:
                if '-' in equation:
                    minuses = equation.split('-')
                    for i, substraction in enumerate(minuses):
                        if i == 0 and 'x' in substraction:
                            x_count += int(substraction[0:substraction.find('x')]) if len(substraction)>1 else 1
                        elif i == 0:
                            value += int(substraction) if len(substraction)>=1 else 0
                        elif 'x' in substraction:
                            x_count -= int(substraction[0:substraction.find('x')]) if len(substraction)>1 else 1
                        else:
                            value -= int(substraction)
                
                else:
                        x_count += int(equation[0:equation.find('x')]) if len(equation)>1 else 1
            else:
                value += eval(equation)
        for equation in right_sides_plus:
            if 'x' in equation:
                if '-' in equation:
                    minuses = equation.split('-')
                    for i, substraction in enumerate(minuses):
                        if i == 0 and 'x' in substraction:
                            x_count -= int(substraction[0:substraction.find('x')]) if len(substraction)>1 else 1
                        elif i == 0:
                            value -= int(substraction) if len(substraction)>=1 else 0
                        elif 'x' in substraction:
                            x_count += int(substraction[0:substraction.find('x')]) if len(substraction)>1 else 1
                        else:
                            value += int(substraction)
                else:
                        x_count -= int(equation[0:equation.find('x')]) if len(equation)>1 else 1        
            else:
                value -= eval(equation)
        if value==0 and x_count == 0:
            return('Infinite solutions')
        if x_count==0:
            return('No solution') 
        answer = 'x={}'.format(int(-1*value/x_count))
        return(answer)
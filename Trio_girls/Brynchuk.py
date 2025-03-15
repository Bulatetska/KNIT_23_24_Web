def linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Рівняння має безліч розв'язків"
        else:
            return "Рівняння не має розв'язку"
    else:
        return -b / a
    
   

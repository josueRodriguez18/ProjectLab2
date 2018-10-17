import connection
from connection import parsed
import logic

main = logic.Field()
#main.Ball.x = parsed["Ball"][" Object Center"]["X"]

shapes = [ "Triangle", "Circle", "Square"]
it = 0
while True:
    main.RedTriangle.x = parsed["Red Team Data"]["Triangle"]["Object Center"]['X']
    main.RedTriangle.y = parsed["Red Team Data"]["Triangle"]["Object Center"]['Y']


    main.RedCircle.x = parsed["Red Team Data"]["Circle"]["Object Center"]['X']
    main.RedCircle.y = parsed["Red Team Data"]["Circle"]["Object Center"]['Y']

    main.RedSquare.x = parsed["Red Team Data"]["Square"]["Object Center"]['X']
    main.RedSquare.y = parsed["Red Team Data"]["Square"]["Object Center"]['Y']

    main.Ball.x = parsed["Ball"]["Object Center"]['X']
    main.Ball.y = parsed["Ball"]["Object Center"]['Y']

    main.BlueTriangle.x = parsed["Blue Team Data"]["Triangle"]["Object Center"]['X']
    main.BlueTriangle.y = parsed["Blue Team Data"]["Triangle"]["Object Center"]['Y']

    main.BlueCircle.x = parsed["Blue Team Data"]["Circle"]["Object Center"]['X']
    main.BlueCircle.y = parsed["Blue Team Data"]["Circle"]["Object Center"]['Y']

    main.BlueSquare.x = parsed["Blue Team Data"]["Square"]["Object Center"]['X']
    main.BlueSquare.y = parsed["Blue Team Data"]["Square"]["Object Center"]['Y']
    
    main.closest()
    print(main.closest().x)
    print(main.closest().y)
    input()
    
    





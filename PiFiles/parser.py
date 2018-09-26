from connection import parsed
import logic
main = logic.Field()

#main.Ball.pos[0] = parsed["Ball"]["Object Center"]["X"]
sample = [0,0,0,0]

main.RedTeam[0].pos[0] = parsed["Red Team Data"]["Circle"]["Object Center"]['X']
main.RedTeam[0].pos[1] = parsed["Red Team Data"]["Circle"]["Object Center"]['Y']

sample[0] = parsed["Red Team Data"]["Square"]["Object Center"]['X']
sample[1] = parsed["Red Team Data"]["Square"]["Object Center"]['Y']

main.RedTeam[1].pos[0] = sample[0]
main.RedTeam[1].pos[1] = sample[1]

sample[2] = parsed["Red Team Data"]["Square"]["Object Center"]['X']
sample[3] = parsed["Red Team Data"]["Square"]["Object Center"]['Y']

main.RedTeam[2].pos[0] = sample[2]
main.RedTeam[2].pos[1] = sample[3]

main.Ball.pos[0] = parsed["Ball"]["Object Center"]["X"]
main.Ball.pos[1] = parsed["Ball"]["Object Center"]["Y"]

sample[0] = parsed["Red Team Data"]["Triangle"]["Object Center"]['X']
sample[1] = parsed["Red Team Data"]["Triangle"]["Object Center"]['Y']


print(main.RedTeam[0].pos[0])
print(main.RedTeam[0].pos[1])

print(main.RedTeam[1].pos[0])
print(main.RedTeam[1].pos[1])

print(sample[0])
print(sample[1])


#close = main.closest()


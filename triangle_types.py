AB , BC , CA = [int(n) for n in (input("Enter the side AB , BC , CA : ")).split()]
if AB == BC ==CA:
    print("Equilateral triangle")
elif AB!=BC== CA or AB== BC!= CA or CA==AB!=BC :
    print("Isosceles triangle")
elif AB != BC != CA:
    print("Scalene or right angled-triangle")
else:
    print(AB,BC,CA)
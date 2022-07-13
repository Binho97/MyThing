employeeCategory=int(input("Enter employee category(1/2/3/4): "))
state=input("Enter state(NY/NZ/PA/TX/LA/FL): ")
state1=["NY","NJ","PA"]

color=""
if employeeCategory==1:
    if state.upper() in state1:
        color="Blue"
    else:
        color="White"
elif employeeCategory==2:
    if state.upper() in state1:
        color="Purple"
    else:
        color="Green"
elif employeeCategory==3:
    if state.upper() in state1:
        color="Red"
    else:
        color="Maroon"
else:
    if state.upper() in state1:
        color="Black"
    else:
        color="Grey"

print("Color code to follow:",color)

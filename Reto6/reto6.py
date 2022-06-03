import numpy as np

a=np.array([[[12346],"Pepe",15,"Español",True],
[32156,"Maria",17,"Matematicas",False],
[23476,"Jose",18,"Español",False],
[56743,"Mario",14,"Fisica",False],
[98712,"luz",16,"Matematicas",True],
[45621,"Santiago",15,"Español",True]])

#matriz = np.array(a)

print('********Promedio***********')
def Promedio():
    print("promedio:", a[:,2].mean())
    print("edades:", a[:,2])
Promedio()

    
    




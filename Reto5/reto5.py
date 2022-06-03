import random

Listas_C_P=[
    'Ajolote','Aldeano','Bacalao','Burro','Caballo','Caballo','Calamar',
    'Calamar_brillante','Cerdo','Champiñaca','Conejo','Gallina','Gato',
    'Gólem_de_nieveLavagante','Loro','Mula','Mirciélago','Ocelote',
    'Oso','Oveja','Pez_tropical','Piglin','Salmón','Tortuga','Vaca','Vendedor',
    'Zorro'
]

Listas_C_H=[ 
'Ahogado','Aldeano','zombi','Ánima','Blaze','Bruja','Creeper','Cubo_de_magma','Devastador',
'Dragón_del_End','Endermite','Esqueleto','Esqueleto_glacial','Esqueleto_wither',
'Fantasma','Ghast','Guardián','Guardián_anciano','Hoglin','Invocador','Jinete_avícola',
'Jinete_arácnido','Jinete_devastador','Jinete_esquelético','Lepisma','Piglin_bruto','Saqueador','Shulker','Slime',
'Vindicador','Warden','Wither','Zoglin','Zombi_P','Zombi_desértico'
]

total = len(Listas_C_P) + len(Listas_C_H) 
print("total_animales",total)

CP = int(input('digite numeros de criaturas pasivas'))
CH = int(input('digite numeros de criaturas hostiles'))
totalA = CP + CH 
if (CP < totalA and CH < totalA ) and (totalA<=50):
    A1 = random.sample(Listas_C_H,CH)
    A2 = random.sample(Listas_C_P,CP)
    print('CH',A1,'CP',A2)
else:
    print('error ingresar la longitud adecuada menores que 50')









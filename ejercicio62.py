#Ejercicio 62
#Un supermercado esta ofrciendo el 60% de descuento en una 
# ariedad de productos descontinuados. El supermercado quyiere 
#ayudar a sus clientes a determinar el precio reducido de su 
#mercancia con una tabla impresa en los aparadores dond emuestre 
#los precios originales y los precios despues de aplicarse el
#descuento. Escribe un programa que use un ciclo while para 
#generar esta tabla mostrando el precio original, el descuento
#y el nuevo precio para los productos de 4.95, 9.95, 14.95,
#19.95, 24.95. Loes descuentos y los nuevos precuios deben de 
#ser redondiados a 2 decimales. 


print('precio original  |   descuento   |   precio final')
print('__________________________________________________')
precio_original = 4.95 
while precio_original <= 24.95:
     descuento = precio_original * 0.60
     precio_final = precio_original - descuento
     print('$ %.2f' %precio_original,    '|',  '$ %.2f' %descuento,    '|',  '$ %.2f' %precio_final)
     precio_original = precio_original + 5
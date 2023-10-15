# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
renta = float(input('Cual es su renta anual: '))

if renta < 1000:
    print('tramo impositivo es de 5%')
    tramo_impositivo = 5
elif renta < 20000:
    print('el tramo impositivo es de 15%')
    tramo_impositivo = 15
elif renta < 35000:
    print('el tramo impositivo es de 20%')
    tramo_impositivo = 20
elif renta < 6000:
    print('el tramo impositivo es de 30%')
    tramo_impositivo = 30
else:
    print('el tramo impositivo es de 45%')
    tramo_impositivo = 45

print('tienes que pagar ',renta * tramo_impositivo / 100 , "€" , sep="")
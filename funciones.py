from sympy import *

def Empresa(nombre,productos,numeroMaquinas,restriccion_produccion,
            costoFuncMaquina,supervisores,numPedidos,fecha,salario):

    print("Empresa: " + nombre + "\nTipo de producto: " + productos +
                "\nNumero de Maquinas: ",numeroMaquinas,
                "\nProduccion de juguetes por hora: " ,restriccion_produccion,
                "\nCosto de funcionamiento por Maquina: ",costoFuncMaquina,
                "\nNumero de supervisores: ", supervisores,"\ncantidad de pedidos: "
                ,numPedidos,"\naño: " + fecha,"\nSalario por hora: $", salario)

    lista=[nombre,productos,numeroMaquinas,restriccion_produccion,
           costoFuncMaquina,supervisores,numPedidos,fecha,salario]
    return lista


def minimizacionCostos(lista):
    print("\nEcuacion la grange")
    #4.8x+20y+λ(30xy-8000)
    x = Symbol('x')
    y = Symbol('y')
    λ = Symbol('λ')
    fxyλ=lista[8]*x+lista[4]*y+(λ*lista[3]*x*y)-λ*lista[6]
    print("fxyλ = ",fxyλ)
    dfx=Derivative(fxyλ,x).doit()
    dfy=Derivative(fxyλ,y).doit()
    dfλ=Derivative(fxyλ,λ).doit()

    print("\nSistema de Ecuaciones")
    print("dfx = ",dfx,"= 0")
    print("dfy = ",dfy,"= 0")
    print("dfλ = ",dfλ,"= 0")

    resultado = solve([dfx, dfy, dfλ], [x, y, λ])
    print("")
    print (resultado)
    return resultado

def empresaPYCCA(lista,lista2):
    #print(lista[0])
    print("\nDeterminar el número de máquinas que deberán ponerse en "
          "funcionamiento para que el costo de producción sea mínimo.")
    print("Se necesita",round(abs(lista[0][1]),2)," de ",lista2[2],"máquinas que deberán ponerse en funcionamiento "
                                                                   "para que el "
                                                          "costo de producción sea mínimo")

    print("\n¿Determine el número de horas trabajaran las máquinas "
          "para cumplir con el pedido y cuanto ganara el supervisor?")
    print("El número de horas trabajada por la maquina será de",round(abs(lista[0][0]),2)," horas")
    costoSupervisor=lista2[8]*lista[0][0]
    print("El supervisor ganara $",round(abs(costoSupervisor),2))
    print("\nObtener el costo de puesta en funcionamiento del numero óptimo de máquinas")
    Cm=lista2[4]*round(abs(lista[0][1]),2)
    print("Costo del numero óptimo de máquinas en funcionamiento es: $",Cm)








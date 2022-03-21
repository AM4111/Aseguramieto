# ---------------------  Funciones  Axuiliares------------------------------------------------
def cal_G(dia, mes, anno):
    if(mes==2 and dia<=28):
        return (bool(1))
    
    elif (R2(anno) and dia<=29):
        return (bool(1))
    
    elif(mes==4 or mes==6 or mes==9 or mes==11 and dia<=30):
        return (bool(1))

    elif(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia<=31):
        return (bool(1))
    
    else:
        print('Cantidad de dias incorrecto')
        return (bool(0))
#R0 ---------------------------------------------------------------------
#mari
def R0(fecha_es_tupla):
    if(len(fecha_es_tupla) != 3):
        print('Fecha no valida')
        return (bool(0))
    else:
        for i in range(3):
            if (fecha_es_tupla[i]<= 0):
                print('negativo')
                return (bool(0))
        if (len(str(fecha_es_tupla[0]))==4):
            if (fecha_es_tupla[1]<=12):
                if (fecha_es_tupla[2]<=32):
                    print('Fecha valida')
                    return (bool(1))
            else:
                 print('Mes no valida')
                 return (bool(0))
        else:            
             print('Año no valida')
             return (bool(0))



#R1 ---------------------------------------------------------------------
#joshua
def R1(fecha_es_valida):
    if (fecha_es_valida%4 == 0):
		return True
	elif (fecha_es_valida%100 == 0) and (fecha_es_valida%400 == 0):
		return True
	else:
		return False


#R2 --------------------     fecha valida G.     ------------------------------
#mari

def cal_G(dia, mes, anno):
    if(mes==2 and dia<=28):
        return (bool(1))
    
    elif (R1(anno) and dia<=29):
        return (bool(1))
    
    elif(mes==4 or mes==6 or mes==9 or mes==11 and dia<=30):
        return (bool(1))

    elif(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia<=31):
        return (bool(1))
    
    else:
        print('Cantidad de dias incorrecto')
        return (bool(0))
    
def R2(fecha_es_valida):
    if(R0(fecha_es_valida)):
        if (cal_G(fecha_es_valida[2],fecha_es_valida[1],fecha_es_valida[0])):
            print('Fecha valida calendario gregoriano')
            return (bool(1))
    else:
        print('Fecha no valida')
        return (bool(0))
        

#R3 --------------------     dia siguiente       -------------------------------------
#joshua
def R3(dia_siguiente): #Calcula el dia siguiente, dado una fecha. Puede mejorarse
	Dias_31 = [1,3,5,7,8,10,12]
	Dias_30 = [4,6,9,11]
	if (R2(dia_siguiente) == True):
		esBisiesto = bisiesto(dia_siguiente[0])
		dia = dia_siguiente[2]
		mes = dia_siguiente[1]
		if (mes in Dias_31) and (dia == 31):
			fecha = (dia_siguiente[0],dia_siguiente[1]+1,1)
			return dia_siguiente
		if (mes in Dias_30) and (dia == 30):
			fecha = (dia_siguiente[0],dia_siguiente[1]+1,1)
			return dia_siguiente
		if (esBisiesto) and (mes == 2):
			if (dia == 29):
				dia_siguiente = (dia_siguiente[0],dia_siguiente[1]+1,1)
				return dia_siguiente
			else:
				dia_siguiente = (dia_siguiente[0],dia_siguiente[1],dia_siguiente[2]+1)
				return dia_siguiente
		elif (mes == 2) and (dia == 28):
			fecha = (dia_siguiente[0],dia_siguiente[1]+1,1)
			return dia_siguiente
		else:
			dia_siguiente = (dia_siguiente[0],dia_siguiente[1],dia_siguiente[2]+1)
			return dia_siguiente
		#01,03,05,07,08,10,12
		#04,06,09,11
	else:
		print("La fecha ingresada no es válida")
            
#R4 --------------------     ordinal             ------------------------------------------
#mari
            
#R5 --------------------     calendario          ------------------------------------------
#joshua

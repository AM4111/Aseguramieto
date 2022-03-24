#---------------------------Referencias------------------------------------------------------
#https://pyformat.info/#string_pad_align


#R0 ---------------------------------------------------------------------
#mari
def R0(fecha_es_tupla):
    if(len(fecha_es_tupla) != 3):
        print('tupla no valida')
        return (bool(0))
    else:
        for i in range(3):
            if (fecha_es_tupla[i]<= 0):
                print('no todos son enteros positivos')
                return (bool(0))
        if (fecha_es_tupla[1]<=12):
            if (fecha_es_tupla[2]<=32):
                print('tupla valida')
                return (bool(1))
        else:
             print('Mes no valida')
             return (bool(0))

#(15,1,12) = valido     (2000,2,0)=falso


#R1 ---------------------------------------------------------------------
#joshua
def R1(fecha_es_valida):
    if(fecha_es_valida >= 1582):
        if(fecha_es_valida%4 == 0):
            return True
        elif (fecha_es_valida%100 == 0) and (fecha_es_valida%400 == 0):
            return True
        else:
            return False

#R2 --------------------     fecha valida G.     ------------------------------
#mari

def cal_G(dia, mes, anno):
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]

    if(anno==1582):
        if (mes==10 and dia>=15 and dia<=31):
            return (bool(1))
        elif (mes==11 and dia<=30):
            return (bool(1))
        elif (mes==12 and dia<=31):
            return (bool(1))
        else:
            return (bool(0))
        
    elif(mes==2 and dia<=28):
        return (bool(1))
        
    elif (R1(anno)and dia<=29):
        return (bool(1))
        
    elif(mes in Dias_30 and dia<=30):
        print(dia)
        return (bool(1))
        
    elif(mes in Dias_31 and dia<=31):
        return (bool(1))
        
    else:
        print('Cantidad de dias incorrecto')
        return (bool(0))
    
def R2(fecha_es_valida):
    if(R0(fecha_es_valida)):
        if(fecha_es_valida[0]>=1582):
            if (cal_G(fecha_es_valida[2],fecha_es_valida[1],fecha_es_valida[0])):
                print('Fecha valida calendario gregoriano')
                return (bool(1))
            else:
                print('Fecha invalida calendario gregoriano')
                return (bool(0))
        else:
            print('año fuera de rango')
            return (bool(0))
    else:
        print('Fecha no valida')
        return (bool(0))
        

#R3 --------------------     dia siguiente       -------------------------------------
#joshua
def R3(dia_siguiente): #Calcula el dia siguiente, dado una fecha. Puede mejorarse
	Dias_31 = [1,3,5,7,8,10,12]
	Dias_30 = [4,6,9,11]
	if (R2(dia_siguiente) == True):
		esBisiesto = R1(dia_siguiente[0])
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
def R4(ordinal_dia):
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    dias = 0
    if(R2(ordinal_dia)):
        for i in range(ordinal_dia[1]):
            if (i in Dias_30):
                dias = dias + 31
            elif (i in Dias_31):
                dias = dias + 30
        dias = dias + ordinal_dia[2]
        return (dias)
            
#R5 --------------------     calendario          ------------------------------------------
#joshua

def R5(Imprimir_3x4):
    Meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    Dias = "  D L M M J V S  "
    Fechas = "|" + " "*15 +  "|"
    x = 1
    while (x < 13):
        if (x % 4 != 0):
            print('{:^18}'.format(Meses[x-1]), end = " ")
        else:
            c = 0
            print('{:^18}'.format(Meses[x-1]))
            print('{:^10} '.format(Dias)*4)
            while ( c < 4):
                print('| {:^2}{:^2}{:^2}{:^2}{:^2}{:^2}{:^2}| '.format("a","b","c","d","e","f","g")*4)
                c += 1 
        x += 1


#-------------------------------PRUEBAS----------------------------------------------------

#print(R3((2020,3,22)))
#print(R5(1))

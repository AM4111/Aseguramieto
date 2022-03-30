#---------------------------Referencias------------------------------------------------------
#https://pyformat.info/#string_pad_align


#R0 ---------------------------------------------------------------------
#mari
def fecha_es_tupla(fecha):
    if(len(fecha) != 3):
        #print('tupla no valida')
        return (bool(0))
    else:
        for i in range(3):
            if (fecha[i]<= 0):
                #print('no todos son enteros positivos')
                return (bool(0))
        if (fecha[1]<=12):
            if (fecha[2]<=32):
                return (bool(1))
        else:
             #print('Mes no valida')
             return (bool(0))

#(15,1,12) = valido     (2000,2,0)=falso

def cal_Dia(fecha):
    formatoMeses = {1:11,2:12,3:1,4:2,5:3,6:4,7:5,8:6,9:7,10:8,11:9,12:10}
    dia = fecha[2] #Dia del año
    mes = formatoMeses[fecha[1]] #Mes del año, se cuenta desde marzo (Marzo = 1)
    anno = fecha[0]
    if (mes == 12) or (mes == 11): #Se cuentan los ultimos dos meses del año pasado como enero y febrero
        anno -=1 
    PD = anno//100 #Primeros dos digitos del año
    UD = anno%100 #Ultimos dos digitos del año
    
    NumDia = (dia+( (13*mes-1)//5 )+UD+(UD//4)+(PD//4)-2*PD)%7 #Numero correspondiente al día de la semana de esa fecha en particular
    return NumDia

#R1 ---------------------------------------------------------------------
#joshua
def bisiesto(fecha):
    if(fecha >= 1582):
        if(fecha%4 == 0):
            return True
        elif (fecha%100 == 0) and (fecha%400 == 0):
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
        #print(dia)
        return (bool(1))
        
    elif(mes in Dias_31 and dia<=31):
        return (bool(1))
        
    else:
        return (bool(0))
    
def fecha_es_valida(fecha):
    if(R0(fecha)):
        if(fecha[0]>=1582):
            if (cal_G(fecha[2],fecha[1],fecha[0])):
                return (bool(1))
            else:
                return (bool(0))
        else:
            return (bool(0))
    else:
        return (bool(0))
        

#R3 --------------------     dia siguiente       -------------------------------------
#joshua
def dia_siguiente(dia_actual): #Calcula el dia siguiente, dado una fecha. Puede mejorarse
	Dias_31 = [1,3,5,7,8,10,12]
	Dias_30 = [4,6,9,11]
	if (R2(dia_actual) == True):
		esBisiesto = R1(dia_actual[0])
		dia = dia_actual[2]
		mes = dia_actual[1]
		if (mes in Dias_31) and (dia == 31):
			fecha = (dia_actual[0],dia_actual[1]+1,1)
			return dia_actual
		if (mes in Dias_30) and (dia == 30):
			fecha = (dia_actual[0],dia_actual[1]+1,1)
			return fecha
		if (esBisiesto) and (mes == 2):
			if (dia == 29):
				dia_actual = (dia_actual[0],dia_actual[1]+1,1)
				return dia_actual
			else:
				dia_actual = (dia_actual[0],dia_actual[1],dia_actual[2]+1)
				return dia_actual
		elif (mes == 2) and (dia == 28):
			fecha = (dia_actual[0],dia_actual[1]+1,1)
			return dia_actual
		else:
			dia_actual = (dia_actual[0],dia_actual[1],dia_actual[2]+1)
			return dia_actual
		#01,03,05,07,08,10,12
		#04,06,09,11
	else:
		print("La fecha ingresada no es válida")
            
#R4 --------------------     ordinal             ------------------------------------------
#mari
def ordinal_dia(ordinal):
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    dias = 0
    if(R2(ordinal)):
        for i in range(ordinal[1]):
            if (i ==2):
                if (R1(ordinal[0])):
                    #print("isiesto")
                    dias = dias + 29
                else:
                    dias = dias + 28
            elif (i in Dias_30):
                dias = dias + 30
            elif (i in Dias_31):
                dias = dias + 31
        dias = dias + ordinal[2]
        return (dias)
            
#R5 --------------------     CALENDARIO          ------------------------------------------
#joshua y mari

def Imprimir_3x4(calendario):
    Dias_31 = [1,3,5,7,8,10,12]
    Dias_30 = [4,6,9,11]
    if calendario <= 1582:
        print("La fecha no es correcta")
    else:
        Meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        Dias = "   D  L  M  M  J  V  S  "
        x = 1
        print("----------------------------------------------------------------------------------------------------")
        print("                                    Calendario      ",calendario)
        while (x < 4):
            #print(' {:^10}{:^10}{:^10}{:^10} '.format("Enero","Febrero","Marzo","Abril"))
            if  x == 1:
                print("----------------------------------------------------------------------------------------------------")
                print(' {:^15}{:^45}{:^5}{:^45} '.format("Enero","Febrero","Marzo","Abril"))
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S")*3, end = "")
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S"))
                m1 = (calendario,1,1)
                d1= (calendario,1,1)
                d2 = (calendario,2,1)
                d3 = (calendario,3,1)
                d4 = (calendario,4,1)
            elif  x == 2:
                print("                                                                                                    ")
                print(' {:^15}{:^45}{:^5}{:^45} '.format("Mayo","Junio","Julio","Agosto"))
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S")*3, end = "")
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S"))
                m1 = (calendario,5,1)
                d1= (calendario,5,1)
                d2 = (calendario,6,1)
                d3 = (calendario,7,1)
                d4 = (calendario,8,1)

            else:
                print("                                                                                                    ")
                print(' {:^20}{:^35}{:^5}{:^45} '.format("Septiembre","Octubre","Noviembre","Diciembre"))
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S")*3, end = "")
                print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format("D","L","K","M","J","V","S"))
                m1 = (calendario,9,1)
                d1= (calendario,9,1)
                d2 = (calendario,10,1)
                d3 = (calendario,11,1)
                d4 = (calendario,12,1)

            c = 0
            i=0
            j = 0
            f1=0
            f2=0
            f3=0
            f4=0
            while (i < 24):
                p1 = " "
                p2 = " "
                p3 = " "
                p4 = " "
                p5 = " "
                p6 = " "
                p7 = " "
                if (i == 0 or i == 4 or i == 8 or i == 12 or i == 16 or i == 20):
                    m1 = d1
                    ff = f1
                    if (i > 0):
                        m1 = R3(m1)
                elif (i == 1 or i == 5 or i == 9 or i == 13 or i == 17  or i == 21):
                    m1 = d2
                    ff = f2
                    if (i > 1):
                        m1 = R3(m1)
                elif (i == 2 or i == 6 or i == 10 or i == 14 or i == 18 or i == 22):
                    m1 = d3
                    ff = f3
                    if (i > 2):
                        m1 = R3(m1)
                elif (i == 3 or i == 7 or i == 11 or i == 15 or i == 19 or i == 23):
                    m1 = d4
                    ff = f4
                    if (i > 3):
                        m1 = R3(m1)
                c = cal_Dia(m1)
                if (c == 0 ):
                    if(m1[1]== 2):
                        if(R1(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p1 = str(m1[2])
                                
                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p2 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p3 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p4 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=29 and ff==0):
                                                if (m1[2]==29):
                                                    ff = 1
                                                p5 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=29 and ff==0):
                                                    if (m1[2]==29):
                                                        ff = 1
                                                    p6 = str(m1[2])

                                                    m1 = R3(m1)
                                                    if (m1[2]<=29 and ff==0):
                                                        if (m1[2]==29):
                                                            ff = 1
                                                        p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p1 = str(m1[2])
                                
                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p2 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p3 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p4 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=28 and ff==0):
                                                if (m1[2]==28):
                                                    ff = 1
                                                p5 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=28 and ff==0):
                                                    if (m1[2]==28):
                                                        ff = 1
                                                    p6 = str(m1[2])

                                                    m1 = R3(m1)
                                                    if (m1[2]<=28 and ff==0):
                                                        if (m1[2]==28):
                                                            ff = 1
                                                        p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p1 = str(m1[2])
                            
                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=30 and ff==0):
                                            if (m1[2]==30):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=30 and ff==0):
                                                if (m1[2]==30):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=30 and ff==0):
                                                    if (m1[2]==30):
                                                        ff = 1
                                                    p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p1 = str(m1[2])
                            
                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=31 and ff==0):
                                            if (m1[2]==31):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=31 and ff==0):
                                                if (m1[2]==31):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=31 and ff==0):
                                                    if (m1[2]==31):
                                                        ff = 1
                                                    p7 = str(m1[2])
                elif (c == 1):
                    if(m1[1]== 2):
                        if(R1(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=29 and ff==0):
                                                if (m1[2]==29):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=29 and ff==0):
                                                    if (m1[2]==29):
                                                        ff = 1
                                                    p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p2 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p3 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p4 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p5 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=28 and ff==0):
                                                if (m1[2]==28):
                                                    ff = 1
                                                p6 = str(m1[2])

                                                m1 = R3(m1)
                                                if (m1[2]<=28 and ff==0):
                                                    if (m1[2]==28):
                                                        ff = 1
                                                    p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p2 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=30 and ff==0):
                                            if (m1[2]==30):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=30 and ff==0):
                                                if (m1[2]==30):
                                                    ff = 1
                                                p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p2 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=31 and ff==0):
                                            if (m1[2]==31):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=31 and ff==0):
                                                if (m1[2]==31):
                                                    ff = 1
                                                p7 = str(m1[2])

                    
                elif (c == 2):
                    if(m1[1]== 2):
                        if(R1(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=29 and ff==0):
                                                if (m1[2]==29):
                                                    ff = 1
                                                p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p3 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p4 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p5 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p6 = str(m1[2])

                                            m1 = R3(m1)
                                            if (m1[2]<=28 and ff==0):
                                                if (m1[2]==28):
                                                    ff = 1
                                                p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p3 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=30 and ff==0):
                                            if (m1[2]==30):
                                                ff = 1
                                            p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p3 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=31 and ff==0):
                                            if (m1[2]==31):
                                                ff = 1
                                            p7 = str(m1[2])
                elif (c == 3):
                    if(m1[1]== 2):
                        if(R1(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=29 and ff==0):
                                            if (m1[2]==29):
                                                ff = 1
                                            p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p4 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p5 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p6 = str(m1[2])

                                        m1 = R3(m1)
                                        if (m1[2]<=28 and ff==0):
                                            if (m1[2]==28):
                                                ff = 1
                                            p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p4 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=30 and ff==0):
                                        if (m1[2]==30):
                                            ff = 1
                                        p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p4 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=31 and ff==0):
                                        if (m1[2]==31):
                                            ff = 1
                                        p7 = str(m1[2])
                elif (c == 4):
                    if(m1[1]== 2):
                        if(R1(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=29 and ff==0):
                                        if (m1[2]==29):
                                            ff = 1
                                        p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p5 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p6 = str(m1[2])

                                    m1 = R3(m1)
                                    if (m1[2]<=28 and ff==0):
                                        if (m1[2]==28):
                                            ff = 1
                                        p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p5 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=30 and ff==0):
                                    if (m1[2]==30):
                                        ff = 1
                                    p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p5 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=31 and ff==0):
                                    if (m1[2]==31):
                                        ff = 1
                                    p7 = str(m1[2])
                elif (c == 5):
                    if(m1[1]== 2):
                        if(R1(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=29 and ff==0):
                                    if (m1[2]==29):
                                        ff = 1
                                    p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p6 = str(m1[2])

                                m1 = R3(m1)
                                if (m1[2]<=28 and ff==0):
                                    if (m1[2]==28):
                                        ff = 1
                                    p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p6 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=30 and ff==0):
                                if (m1[2]==30):
                                    ff = 1
                                p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p6 = str(m1[2])

                            m1 = R3(m1)
                            if (m1[2]<=31 and ff==0):
                                if (m1[2]==31):
                                    ff = 1
                                p7 = str(m1[2])
                elif (c == 6):
                    if(m1[1]== 2):
                        if(R1(m1[0])):
                            if (m1[2]<=29 and ff==0):
                                if (m1[2]==29):
                                    ff = 1
                                p7 = str(m1[2])
                        else:
                            if (m1[2]<=28 and ff==0):
                                if (m1[2]==28):
                                    ff = 1
                                p7 = str(m1[2])
                    if(m1[1]in Dias_30):
                        if (m1[2]<=30 and ff==0):
                            if (m1[2]==30):
                                ff = 1
                            p7 = str(m1[2])
                    if(m1[1]in Dias_31):
                        if (m1[2]<=31 and ff==0):
                            if (m1[2]==31):
                                ff = 1
                            p7 = str(m1[2])

                if (j == 0 or j == 4 or j == 8 or j == 12 or i == 16 or i == 20):
                    d1 = m1
                    f1 = ff
##                        print(d1)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7), end = "")
                elif (j == 1 or j == 5 or j == 9 or j == 13 or i == 17 or i == 21):
                    d2 = m1
                    f2 = ff
##                        print(d2)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7), end = "")
                elif (j == 2 or j == 6 or j == 10 or j == 14 or i == 18 or i == 22):
                    d3 = m1
                    f3 = ff
##                        print(d3)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7), end = "")
                elif (j == 3 or j == 7 or j == 11 or j == 15 or i == 19 or i == 23):
                    d4 = m1
                    f4 = ff
##                        print(d4)
##                        print(m1)
                    print('| {:^3}{:^3}{:^3}{:^3}{:^3}{:^3}{:^3}| '.format(p1,p2,p3,p4,p5,p6,p7))
                i += 1
                j += 1
            x += 1
        

#-------------------------------    1b           ----------------------------------------------------


#R6 --------------------     dia_semana          ------------------------------------------
#parametro: fecha tipo (año,mes,dia)
#devuelve: # segun dia 

def dia_semana(fecha):
    formatoMeses = {1:11,2:12,3:1,4:2,5:3,6:4,7:5,8:6,9:7,10:8,11:9,12:10}
    dia = fecha[2] #Dia del año
    mes = formatoMeses[fecha[1]] #Mes del año, se cuenta desde marzo (Marzo = 1)
    anno = fecha[0]
    if (mes == 12) or (mes == 11): #Se cuentan los ultimos dos meses del año pasado como enero y febrero
        anno -=1 
    PD = anno//100 #Primeros dos digitos del año
    UD = anno%100 #Ultimos dos digitos del año
    
    NumDia = (dia+( (13*mes-1)//5 )+UD+(UD//4)+(PD//4)-2*PD)%7 #Numero correspondiente al día de la semana de esa fecha en particular
    return NumDia


#R7 --------------------     fecha_futura          ------------------------------------------
#tupla y umero, devolver ua tupla??

#R8 --------------------     dias_entre          ------------------------------------------
#lista que tiee 2 tuplas o 2 parametros diferetes

#R9 --------------------     edad_al          ------------------------------------------
#lista que tiee 2 tuplas
#retur (años que tiee, meses,dias)
#validar co R0

#R10 --------------------     fecha_hoy          ------------------------------------------

#R11 --------------------     edad_hoy          ------------------------------------------
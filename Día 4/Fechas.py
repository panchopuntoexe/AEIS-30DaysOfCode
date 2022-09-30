from datetime import date, timedelta

#Toma un rango de fechas y retorna los días sin fines de semana
def dias_laborables_entre_fechas(fecha_inicio,fecha_fin):
    dias_laborables=0

    #Se itera por el rango incluyendo la fecha final
    for n in range((fecha_fin - fecha_inicio).days+1):

        #Se verifica que sea dia laborable con weekday()
        #Este retorna 0 si es lunes, 1 si es martes, etc. Siendo 4 viernes.
        if (fecha_inicio + timedelta(days=n)).weekday()<=4:
            dias_laborables+=1
    return dias_laborables

#Se toma las horas y divide por los días laborables, 
#se transforma al formato de horas con timedelta
def distribuir_horas(horas,fecha_inicio,fecha_fin):
    tiempo = horas/dias_laborables_entre_fechas(fecha_inicio,fecha_fin)
    return timedelta(hours=tiempo)

print(distribuir_horas(155,date(2022, 9, 1),date(2022, 9, 29)))
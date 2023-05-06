import time

hora_actual = time.localtime().tm_hour
minutos_actuales = time.localtime().tm_min
segundos_actuales = time.localtime().tm_sec

if hora_actual >= 19:
    print("Es hora de irte a casa")
else:
    horas_restantes = (
        19 - hora_actual - (1 if minutos_actuales > 0 or segundos_actuales > 0 else 0)
    )
    minutos_restantes = (60 - minutos_actuales) if minutos_actuales > 0 else 0
    segundos_restantes = (60 - segundos_actuales) if segundos_actuales > 0 else 0

    print(
        f"Todavia faltan {horas_restantes} horas {minutos_restantes} minutos {segundos_restantes} segundos para irte"
    )

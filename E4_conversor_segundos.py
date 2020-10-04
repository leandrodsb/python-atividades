convert_sec = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dia = convert_sec//86400
hora = (convert_sec%86400)//3600
minutos = ((convert_sec%86400)%3600)//60
segundos = ((convert_sec%86400)%3600)%60
print(dia,"dias,",hora,"horas,",minutos,"minutos, e",segundos,"segundos.")

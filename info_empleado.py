def datos_empleado(nombre, cargo, anios):
    anios = int(anios)
    if anios > 5 :
        print('El empleado '+nombre+' trabaja como '+cargo+' y tiene '+str(anios)+' años, empleado con experiencia senior')
    else :
        print('El empleado '+nombre+' trabaja como '+cargo+' y tiene '+str(anios)+' años de experiencia')


datos_empleado('Mayra', 'secretaria', '3')
datos_empleado('Lucas', 'programador', '7')
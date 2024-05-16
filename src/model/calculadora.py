def calcular_retencion(salario_basico, valor_uvt):
    if not isinstance(salario_basico, (int, float)):
        raise ValueError("El salario básico debe ser un número")
    retencion = 0
    salario_basico = float(salario_basico)
    ingreso_uvt = salario_basico / valor_uvt

    if ingreso_uvt <= 95:
        pass
    elif ingreso_uvt <= 150:
        base_uvt = ingreso_uvt - 95
        retencion = base_uvt * 0.19 * valor_uvt
    elif ingreso_uvt <= 360:
        base_uvt = ingreso_uvt - 150
        retencion = base_uvt * 0.28 * valor_uvt + 10 * valor_uvt
    elif ingreso_uvt <= 640:
        base_uvt = ingreso_uvt - 360
        retencion = base_uvt * 0.33 * valor_uvt + 69 * valor_uvt
    elif ingreso_uvt <= 945:
        base_uvt = ingreso_uvt - 640
        retencion = base_uvt * 0.35 * valor_uvt + 162 * valor_uvt
    elif ingreso_uvt <= 2300:
        base_uvt = ingreso_uvt - 945
        retencion = base_uvt * 0.37 * valor_uvt + 268 * valor_uvt
    else:
        base_uvt = ingreso_uvt - 2300
        retencion = base_uvt * 0.39 * valor_uvt + 770 * valor_uvt
    
    # Agregamos un límite superior para la retención del 40% del ingreso
    retencion = min(retencion, salario_basico * 0.4)
    
    return round(retencion, 2)

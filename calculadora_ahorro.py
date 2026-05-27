# Herramienta sencilla para planificar metas de ahorro
try:
    meta = float(input("¿Cuánto dinero necesitas reunir (en DH)?: "))
    ahorro_diario = float(input("¿Cuánto puedes guardar cada día?: "))

    if ahorro_diario > 0:
        dias = meta / ahorro_diario
        print(f"\nPara alcanzar {meta} DH, necesitas ahorrar durante {dias:.1f} días.")
        print("¡Sigue adelante con tu esfuerzo!")
    else:
        print("\nEl ahorro diario debe ser mayor que 0.")
except ValueError:
    print("\nPor favor, introduce solo números.")

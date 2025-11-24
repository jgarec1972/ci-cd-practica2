# Este archivo contiene la lógica de negocio y el Quality Gate (las pruebas).

# --- LÓGICA DE NEGOCIO ---
def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    # NOTA: En la FASE 2 de la práctica, los estudiantes deben introducir un bug aquí.
    return a - b # La lógica correcta inicialmente.

# --- PRUEBAS UNITARIAS (QUALITY GATE) ---
def test_suite():
    """
    Función que ejecuta todas las pruebas unitarias.
    Si cualquier 'assert' falla, el script Python termina con un código de error,
    lo que provoca que el paso de GitHub Actions falle.
    """
    print("=============================================")
    print("🚦 Iniciando Quality Gate: Pruebas Unitarias...")
    
    # Prueba 1: Verificar la suma
    assert sumar(5, 3) == 8, "ERROR: La función sumar falló (5+3 != 8)"
    
    # Prueba 2: Verificar la resta (¡Este fallará en la FASE 2!)
    assert restar(10, 4) == 6, "ERROR: La función restar falló (10-4 != 6)"
    
    # Prueba 3: Caso borde con cero
    assert sumar(0, 5) == 5, "ERROR: La función sumar con cero falló"

    print("✅ Quality Gate APROBADO. El código es de calidad.")
    print("=============================================")

if __name__ == "__main__":
    try:
        test_suite()
    except AssertionError as e:
        # Imprime el error y asegura que el script termine con un código de salida distinto de 0 (FALLA)
        print(f"\n❌ FALLA DEL QUALITY GATE DETECTADA: {e}")
        import sys
        sys.exit(1) # Código de falla para CI


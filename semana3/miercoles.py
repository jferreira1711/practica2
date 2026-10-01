class SaldoInsuficienteError(Exception):
    pass

def retirar_dinero(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(f"Necesitas ${monto}, pero solo tienes ${saldo}")
    return saldo - monto

try:
    retirar_dinero(100, 150)
except SaldoInsuficienteError as e:
    print(f"No se pudo procesar: {e}")
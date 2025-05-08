# Conversão de três temperaturas de Celsius para Fahrenheit (30°C, 100°C e 0°C).

def fahrenheit(temperatura):
    resultado = (temperatura * 1.8) + 32
    print(f"A temperatura {temperatura:.2f} ºC em Fahrenheit é: {resultado:.2f} ºF")
    return resultado

fahrenheit(30)
fahrenheit(100)
fahrenheit(0)
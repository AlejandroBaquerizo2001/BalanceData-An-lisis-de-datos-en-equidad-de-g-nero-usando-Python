# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Datos ficticios sobre equidad de género (salarios en USD)
data = {
    "País": ["País A", "País B", "País C", "País D", "País E"],
    "Salario Hombres": [3000, 3200, 3100, 2900, 3300],
    "Salario Mujeres": [2500, 2700, 2600, 2400, 2800],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Función para calcular la brecha salarial
def calcular_brecha_salarial(df):
    df["Brecha Salarial"] = df["Salario Hombres"] - df["Salario Mujeres"]
    return df

# Función para graficar la brecha salarial
def graficar_brecha_salarial(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df["País"], df["Brecha Salarial"], color="red")
    plt.title("Brecha Salarial entre Hombres y Mujeres por País")
    plt.xlabel("País")
    plt.ylabel("Brecha Salarial (USD)")
    plt.show()

# Función para calcular estadísticas básicas
def calcular_estadisticas(df):
    media_brecha = statistics.mean(df["Brecha Salarial"])
    print(f"La brecha salarial promedio es: {media_brecha} USD")

# Ejecutar las funciones
df = calcular_brecha_salarial(df)
print(df)  # Mostrar el DataFrame con la brecha salarial
graficar_brecha_salarial(df)
calcular_estadisticas(df)
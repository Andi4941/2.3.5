def realizar_encuesta():
    encuesta = {
        "¿Cómo calificarías tu nivel de atención durante las clases?": ["Muy baja", "Baja", "Media", "Alta", "Muy alta"],
        "¿Con qué frecuencia completas tus tareas escolares a tiempo?": ["Nunca", "Raramente", "A veces", "Frecuentemente", "Siempre"],
        "¿Qué tan bien te comunicas con tus compañeros y profesores?": ["Muy mal", "Mal", "Regular", "Bien", "Muy bien"],
        # Agrega las demás preguntas con sus opciones de respuesta aquí
    }

    respuestas = {}
    for pregunta, opciones in encuesta.items():
        print(pregunta)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        respuesta = int(input("Selecciona el número correspondiente (1-5): "))
        respuestas[pregunta] = respuesta

    return respuestas

def calcular_puntaje(respuestas):
    total_preguntas = len(respuestas)
    respuestas_correctas = sum(respuesta == 4 for respuesta in respuestas.values())  # Respuesta "Muy alta"
    porcentaje_correcto = (respuestas_correctas / total_preguntas) * 100
    return porcentaje_correcto

def categorizar_alumno(porcentaje):
    if porcentaje >= 75:
        return "Usted es un alumno de buen desempeño."
    elif porcentaje >= 50:
        return "Usted es un alumno que puede mejorar."
    elif porcentaje >= 25:
        return "Usted es un alumno con algunos desafíos."
    else:
        return "Usted es un alumno con muchos desafíos."

def main():
    print("Bienvenido al centro de psicología del estudiante")
    print("Por favor, responde las siguientes preguntas:")
    respuestas = realizar_encuesta()
    porcentaje = calcular_puntaje(respuestas)
    categoria = categorizar_alumno(porcentaje)
    print("Su categoría es:", categoria)

if __name__ == "__main__":
    main()
import random
import string
string_digits = string.digits
exit_status = 0
score = 0
# Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?", "¿Cuál de las siguientes opciones es un número entero en Python?", "¿Cómo se solicita entrada del usuario en Python?", "¿Cuál de las siguientes expresiones es un comentario válido en Python?", "¿Cuál es el operador de comparación para verificar si dos valores son iguales?"
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
    
for question, answer_options, correct_index in (questions_to_ask):
    print(question)

    for i, option in enumerate(answer_options):
        print(f'{i + 1}. {option}')
        
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if not user_answer.isdigit():
            print("Respuesta no válida")
            exit_status = 1
            break
        
        user_answer = int(user_answer) - 1
        
        if not (0 <= user_answer <= 3):
            print("Respuesta no válida")
            exit_status = 1
            break
    
        if user_answer == correct_index: 
            print("¡Correcto!")
            score += 1
            break
        else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
            if intento == 0:
                print("Incorrecto, intenta de nuevo")
            else:
                print("Incorrecto. La respuesta correcta es:")
                print(answer_options[correct_index])
            score -= 0.5
            
    if exit_status == 1:
        break
                
    # Se imprime un blanco al final de la pregunta
    print()
    
print("Fin del juego")
print(f'Puntaje total obtenido: {score}')
import requests
import json

# Pega aquí tu URL real de Google Apps Script entre las comillas
URL_GAS = "https://script.google.com/macros/s/AKfycbw-bG22Fk-OkifBzTbkC1I0vXrGey2tGIqoKZ-N_x0B8HYgIynORi2wOG-RGI4iD7t2/exec"

def hablar_con_asistente(mensaje):
    payload = {"mensaje": mensaje}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(URL_GAS, json=payload, headers=headers)
        data = response.json()
        if data.get("status") == "success":
            return data.get("respuesta")
        else:
            return "Error en el servidor: " + str(data.get("mensaje"))
    except Exception as e:
        return f"Error de conexión: {e}"

if __name__ == "__main__":
    print("🤖 Lilith iniciada. Escribe 'salir' para terminar.")
    while True:
        texto_usuario = input("\nTú: ")
        if texto_usuario.lower() == 'salir':
            print("Lilith: ¡Adiós!")
            break
        
        respuesta = hablar_con_asistente(texto_usuario)
        print(f"Lilith: {respuesta}")
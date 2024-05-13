import speech_recognition as sr
import webbrowser
import pyttsx3 

# Inicialización del reconocedor de voz y del motor de texto a voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Función para escuchar al usuario y convertir su voz en texto
def talk():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source, timeout=4)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f'Dijiste: {text}')
        return text.lower()
    except sr.UnknownValueError:
        print("Lo siento, no entendí lo que dijiste. ¿Podrías repetirlo?")
        return ""  # Devuelve una cadena vacía en caso de error
    except sr.RequestError as e:
        print(f"No se puede obtener la transcripción; {e}")
        return ""  # Devuelve una cadena vacía en caso de error

# Función para que el usuario elija la tienda en la que quiere buscar
def choose_store():
    engine.say('Hola usuario ¿En qué tienda quieres que busque? Amazon, Mercado Libre o eBay.')
    engine.runAndWait()
    text = talk()
    if 'amazon' in text:
        return 'amazon'
    elif 'mercado libre' in text or 'mercadolibre' in text or 'mercado' in text or 'libre' in text:
        return 'mercado libre'
    elif 'ebay' in text or 'ibey' in text or 'ibei' in text or 'abey' in text:
        return 'ebay'
    else:
        print('Tienda no reconocida. Por favor, inténtalo de nuevo.')
        return choose_store()

# Función para buscar productos en la tienda seleccionada por el usuario
def search_store(store):
    if store == 'amazon':
        engine.say('¿Qué quieres comprar en Amazon?')
        engine.runAndWait()
        text = talk()
        if text:
            webbrowser.open(f'https://www.amazon.es/s?k={text}')
    elif store == 'mercado libre':
        engine.say('¿Qué quieres comprar en Mercado Libre?')
        engine.runAndWait()
        text = talk()
        if text:
            webbrowser.open(f'https://listado.mercadolibre.com.co/{text}')
    elif store == 'ebay':
        engine.say('¿Qué quieres comprar en eBay?')
        engine.runAndWait()
        text = talk()
        if text:
            webbrowser.open(f'https://www.ebay.com/sch/i.html?_nkw={text}')
    else:
        print('Tienda no reconocida. Por favor, inténtalo de nuevo.')

# Lógica principal del programa
if __name__ == "__main__":
    chosen_store = choose_store()
    search_store(chosen_store)

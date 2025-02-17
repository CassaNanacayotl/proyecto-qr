import secrets
import string

def generate_secret_key(length=32):
    """
    Genera una SECRET_KEY segura de la longitud especificada.
    Por defecto genera una clave de 32 caracteres.
    """
    # Define los caracteres que se utilizarán
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Genera la clave usando la biblioteca secrets
    secret_key = ''.join(secrets.choice(alphabet) for i in range(length))
    
    return secret_key

# Genera y muestra varias opciones de SECRET_KEY
print("Aquí tienes algunas opciones de SECRET_KEY seguras:")
for i in range(3):
    print(f"Opción {i+1}: {generate_secret_key()}")

# También genera una versión más simple (solo letras y números) por si prefieres algo más legible
simple_alphabet = string.ascii_letters + string.digits
simple_key = ''.join(secrets.choice(simple_alphabet) for i in range(32))
print(f"\nVersión más simple (solo letras y números):\n{simple_key}")
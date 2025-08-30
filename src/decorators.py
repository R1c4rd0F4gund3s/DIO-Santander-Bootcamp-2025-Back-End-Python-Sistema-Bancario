from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{data_hora}] Chamando função: {func.__name__}")
        print(f"  Args: {args}")
        print(f"  Kwargs: {kwargs}")
        
        resultado = func(*args, **kwargs)
        
        print(f"[{data_hora}] Função {func.__name__} retornou: {resultado}")
        return resultado
    return wrapper

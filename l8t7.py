import os 

print(os.path.abspath(os.path.dirname(__file__)))

print(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 

print(os.path.abspath(__file__))

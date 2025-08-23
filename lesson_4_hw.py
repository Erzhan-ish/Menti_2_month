"""
Библиотека: colorama
Зачем нужна:
- Делает вывод в консоли цветным (текст/фон).
- Полезно для красивых логов и CLI-приложений.
"""
from colorama import Fore, Back, Style, init

# Инициализация colorama (нужна на Windows, на Linux/macOS работает сразу)
init(autoreset=True)

def demo_colors():
    print(Fore.RED + "красный текст")
    print(Fore.GREEN + "зелёный текст")
    print(Fore.BLUE + "синий текст")
    print(Back.YELLOW + Fore.BLACK + "Чёрный текст на жёлтом фоне")
    print(Style.BRIGHT + "Яркий стиль текста")
    print("Обычный текст (после autoreset)")


demo_colors()

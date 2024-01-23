
from colorama import init, Fore
from rectangle import Rectangle
from square import Square
from circle import Circle

def main():
    init(autoreset=True)  # Инициализация colorama для сброса цвета после каждого использования

    blue_rectangle = Rectangle(5, 7, Fore.BLUE)
    green_circle = Circle(4, Fore.GREEN)
    red_square = Square(6, Fore.RED)

    print(blue_rectangle)
    print(green_circle)
    print(red_square)

if __name__ == "__main__":
    main()

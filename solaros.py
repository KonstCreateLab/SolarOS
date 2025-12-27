import os
import sys
import time
import random
import math
import subprocess
import platform
import shutil
from datetime import datetime
try:
    import winsound  # Только для Windows
    WINSOUND_AVAILABLE = True
except ImportError:
    WINSOUND_AVAILABLE = False

# Константы
VERSION = "1.21.0"
DEVELOPER = "KonstCreateLab"
CMDS_LIMIT = float('inf')  # Бесконечное количество команд

class SolarOS:
    def __init__(self):
        self.running = True
        self.easter_egg_activated = False
        self.easter_egg_count = 0
        self.secret_code = "52437682"
        self.boot_time = datetime.now()
        
        # Инициализация всех команд
        self.commands = {
            "help": self.show_help,
            "cls": self.clear_screen,
            "clear": self.clear_screen,
            "info": self.show_info,
            "cmd": self.open_cmd,
            "time": self.show_time,
            "date": self.show_date,
            "exit": self.exit_os,
            "quit": self.exit_os,
            "ver": self.show_version,
            "dir": self.list_directory,
            "ls": self.list_directory,
            "pwd": self.show_current_dir,
            "cd": self.change_directory,
            "mkdir": self.make_directory,
            "rmdir": self.remove_directory,
            "echo": self.echo_message,
            "sysinfo": self.show_system_info,
            "calc": self.calculator,
            "shutdown": self.shutdown,
            "reboot": self.reboot,
            "color": self.change_color,
            "history": self.show_history,
            "uptime": self.show_uptime,
            "matrix": self.matrix_effect,
            "secret": self.secret_menu,
            "moon": self.moon_phase,
            "stars": self.starfield,
            "neofetch": self.neofetch,
        }
        self.history = []
        self.current_dir = os.getcwd()
        self.easter_egg_commands = [self.secret_code, "konst", "createlab", "solar", "moonbase", "alpha"]
    
    def play_beep(self, frequency=1000, duration=100):
        """Воспроизвести звуковой сигнал (только Windows)"""
        if platform.system() == "Windows" and WINSOUND_AVAILABLE:
            try:
                winsound.Beep(frequency, duration)
            except:
                pass
    
    def show_bios_screen(self):
        """Показать экран BIOS при загрузке"""
        print("\033[32m")  # Зеленый цвет для BIOS
        
        bios_logo = """
        ╔═══════════════════════════════════════════════════════════╗
        ║                   KONST CREATE LAB BIOS                   ║
        ║                    Version 3.14.15                        ║
        ║                 SolarOS Boot Manager                      ║
        ╚═══════════════════════════════════════════════════════════╝
        """
        print(bios_logo)
        print("\033[37m")  # Белый цвет
        
        # Эффект загрузки BIOS
        print("Initializing system components...")
        time.sleep(0.5)
        
        components = [
            "CPU: Quantum Core i9-13900KS (8.0 GHz)",
            "RAM: Testing 128GB DDR5-8000... OK",
            "GPU: NVIDIA RTX 5090 Ti (48GB VRAM)... OK",
            "Storage: 10TB Quantum SSD... OK",
            "Network: 100Gbps Quantum Link... OK",
            "Power: Solar Fusion Reactor... ONLINE",
        ]
        
        for component in components:
            print(f"  {component}")
            time.sleep(0.3)
        
        print("\nChecking boot devices...")
        time.sleep(0.5)
        
        boot_devices = [
            "[SATA-0] SolarOS System Disk ... OK",
            "[SATA-1] User Data Partition ... OK",
            "[NVMe-0] Quantum Cache ... OK",
            "[USB-3]  Recovery Tools ... Not present",
        ]
        
        for device in boot_devices:
            print(f"  {device}")
            time.sleep(0.2)
        
        print("\n\x1b[33mPress F2 for BIOS Setup | F12 for Boot Menu | DEL for Q-Flash\x1b[0m")
        time.sleep(0.5)
        
        # Прогресс-бар загрузки
        print("\n\x1b[36mBooting SolarOS...\x1b[0m")
        print("[" + " " * 50 + "] 0%", end="")
        
        for i in range(1, 51):
            time.sleep(0.03)
            print(f"\r[{'█' * i}{' ' * (50 - i)}] {i*2}%", end="")
        
        print()
        print("\n\x1b[32m✓ System boot completed successfully\x1b[0m")
        time.sleep(0.5)
        
        # Звуковой сигнал успешной загрузки
        self.play_beep(800, 100)
        self.play_beep(1200, 100)
        
        print("\033[0m")  # Сброс цвета
        time.sleep(0.3)
    
    def print_banner(self):
        """Вывод заголовка системы"""
        colors = ["\033[36m", "\033[35m", "\033[34m", "\033[33m"]
        color = random.choice(colors)
        
        print(f"{color}")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(f"█                                                      █")
        print(f"█          ██████╗  ██████╗ ██╗      █████╗           █")
        print(f"█          ██╔══██╗██╔═══██╗██║     ██╔══██╗          █")
        print(f"█          ██████╔╝██║   ██║██║     ███████║          █")
        print(f"█          ██╔══██╗██║   ██║██║     ██╔══██║          █")
        print(f"█          ██████╔╝╚██████╔╝███████╗██║  ██║          █")
        print(f"█          ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝          █")
        print(f"█               Advanced Operating System              █")
        print(f"█                    Version {VERSION}                    █")
        print(f"█         Commands limit: INFINITE • Quantum Ready     █")
        print(f"█                                                      █")
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        print("\033[0m")
    
    def show_help(self, *args):
        """Показать справку по командам"""
        help_text = f"""
SolarOS {VERSION} - Командная оболочка

ОСНОВНЫЕ КОМАНДЫ:
  help          - Показать эту справку
  cls / clear   - Очистить экран
  info          - Информация о системе
  ver           - Показать версию SolarOS
  neofetch      - Красивая информация о системе
  
ФАЙЛОВАЯ СИСТЕМА:
  dir / ls      - Список файлов и папок
  pwd           - Текущая директория
  cd <path>     - Сменить директорию
  mkdir <name>  - Создать папку
  rmdir <name>  - Удалить папку (только пустую)
  
СИСТЕМНЫЕ КОМАНДЫ:
  time          - Текущее время
  date          - Текущая дата
  sysinfo       - Информация о системе
  uptime        - Время работы системы
  cmd           - Открыть командную строку Windows
  calc          - Простой калькулятор
  
УТИЛИТЫ:
  echo <text>   - Вывести текст
  color <code>  - Изменить цвет текста (0-15)
  history       - История команд
  matrix        - Эффект матрицы
  stars         - Звездное небо
  moon          - Фазы луны
  
СЕКРЕТНЫЕ КОМАНДЫ (после активации):
  secret        - Секретное меню
  
УПРАВЛЕНИЕ:
  exit / quit   - Выйти из SolarOS
  shutdown      - Завершить работу
  reboot        - Перезагрузка системы
  
Для получения информации о конкретной команде: help <команда>
        """
        print(help_text)
    
    def show_info(self, *args):
        """Показать информацию о системе"""
        info = f"""
╔════════════════════════════════════════╗
║           SolarOS Information          ║
╠════════════════════════════════════════╣
║ Версия:         {VERSION:26} ║
║ Разработчик:    {DEVELOPER:26} ║
║ Язык:           Python 3.x            ║
║ Платформа:      {platform.system():26} ║
║ Текущая папка:  {self.current_dir[:30]:30} ║
║ Доступно команд: Бесконечно           ║
╚════════════════════════════════════════╝
        """
        print(info)
    
    def clear_screen(self, *args):
        """Очистить экран"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def open_cmd(self, *args):
        """Открыть командную строку Windows"""
        if platform.system() == "Windows":
            os.system("start cmd")
            print("Командная строка запущена")
        else:
            print("Эта команда доступна только в Windows")
    
    def show_time(self, *args):
        """Показать текущее время"""
        now = datetime.now()
        print(f"Текущее время: {now.strftime('%H:%M:%S')}")
    
    def show_date(self, *args):
        """Показать текущую дату"""
        now = datetime.now()
        print(f"Сегодня: {now.strftime('%d.%m.%Y')}")
    
    def show_version(self, *args):
        """Показать версию SolarOS"""
        print(f"SolarOS версии {VERSION}")
        print(f"Разработчик: {DEVELOPER}")
    
    def list_directory(self, *args):
        """Показать содержимое текущей директории"""
        try:
            items = os.listdir(self.current_dir)
            print(f"\nСодержимое '{self.current_dir}':")
            print("-" * 50)
            
            for item in items:
                full_path = os.path.join(self.current_dir, item)
                if os.path.isdir(full_path):
                    print(f"[DIR]  {item}")
                else:
                    size = os.path.getsize(full_path)
                    print(f"[FILE] {item} ({size} байт)")
            print("-" * 50)
            print(f"Всего: {len(items)} объектов")
            
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def show_current_dir(self, *args):
        """Показать текущую директорию"""
        print(f"Текущая директория: {self.current_dir}")
    
    def change_directory(self, *args):
        """Сменить директорию"""
        if not args:
            print("Использование: cd <путь>")
            return
        
        path = ' '.join(args)
        
        # Специальные пути
        if path == "..":
            new_dir = os.path.dirname(self.current_dir)
        elif path == "~" or path == "/":
            new_dir = os.path.expanduser("~")
        else:
            # Проверяем абсолютный или относительный путь
            if os.path.isabs(path):
                new_dir = path
            else:
                new_dir = os.path.join(self.current_dir, path)
        
        try:
            if os.path.exists(new_dir) and os.path.isdir(new_dir):
                self.current_dir = os.path.abspath(new_dir)
                os.chdir(self.current_dir)
                print(f"Директория изменена на: {self.current_dir}")
            else:
                print(f"Директория не существует: {new_dir}")
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def make_directory(self, *args):
        """Создать директорию"""
        if not args:
            print("Использование: mkdir <имя_папки>")
            return
        
        dir_name = ' '.join(args)
        full_path = os.path.join(self.current_dir, dir_name)
        
        try:
            os.makedirs(full_path, exist_ok=True)
            print(f"Папка создана: {full_path}")
        except Exception as e:
            print(f"Ошибка при создании папки: {e}")
    
    def remove_directory(self, *args):
        """Удалить директорию"""
        if not args:
            print("Использование: rmdir <имя_папки>")
            return
        
        dir_name = ' '.join(args)
        full_path = os.path.join(self.current_dir, dir_name)
        
        try:
            if os.path.exists(full_path):
                shutil.rmtree(full_path)
                print(f"Папка удалена: {full_path}")
            else:
                print(f"Папка не существует: {full_path}")
        except Exception as e:
            print(f"Ошибка при удалении папки: {e}")
    
    def echo_message(self, *args):
        """Вывести сообщение"""
        if args:
            print(' '.join(args))
    
    def show_system_info(self, *args):
        """Показать информацию о системе"""
        print("\n=== ИНФОРМАЦИЯ О СИСТЕМЕ ===")
        print(f"Операционная система: {platform.system()} {platform.release()}")
        print(f"Версия Python: {platform.python_version()}")
        print(f"Архитектура: {platform.machine()}")
        print(f"Имя компьютера: {platform.node()}")
        print(f"Текущий пользователь: {os.getlogin()}")
        print(f"Количество процессоров: {os.cpu_count()}")
        print(f"Разрядность системы: {platform.architecture()[0]}")
    
    def calculator(self, *args):
        """Простой калькулятор"""
        if not args:
            print("Использование: calc <выражение>")
            print("Пример: calc 5 + 3 * 2")
            return
        
        try:
            expression = ' '.join(args)
            # Безопасное вычисление выражения
            result = eval(expression, {"__builtins__": {}}, {})
            print(f"{expression} = {result}")
        except Exception as e:
            print(f"Ошибка вычисления: {e}")
    
    def change_color(self, *args):
        """Изменить цвет текста (только для Windows)"""
        if platform.system() != "Windows":
            print("Смена цвета доступна только в Windows")
            return
        
        if not args:
            print("Использование: color <код>")
            print("Коды цвета (0-15):")
            print("0 - Черный, 1 - Синий, 2 - Зеленый, 3 - Голубой")
            print("4 - Красный, 5 - Фиолетовый, 6 - Желтый, 7 - Белый")
            print("8 - Серый, 9 - Светло-синий, A - Светло-зеленый")
            return
        
        color_code = args[0]
        os.system(f"color {color_code}")
        print(f"Цвет изменен на: {color_code}")
    
    def show_history(self, *args):
        """Показать историю команд"""
        if not self.history:
            print("История команд пуста")
            return
        
        print("\n=== ИСТОРИЯ КОМАНД ===")
        for i, cmd in enumerate(self.history[-20:], 1):  # Последние 20 команд
            print(f"{i:3}. {cmd}")
        print(f"Всего команд в истории: {len(self.history)}")
    
    def shutdown(self, *args):
        """Завершить работу системы"""
        print("Система завершает работу...")
        self.running = False
    
    def reboot(self, *args):
        """Перезагрузить систему"""
        print("Перезагрузка системы...")
        self.clear_screen()
        self.print_banner()
    
    def exit_os(self, *args):
        """Выйти из SolarOS"""
        print("Спасибо за использование SolarOS!")
        self.running = False
    
    def show_uptime(self, *args):
        """Показать время работы системы"""
        uptime = datetime.now() - self.boot_time
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"\n⏱  ВРЕМЯ РАБОТЫ СИСТЕМЫ:")
        print(f"  Запущена: {self.boot_time.strftime('%d.%m.%Y %H:%M:%S')}")
        print(f"  Работает: {uptime.days} дней, {hours} часов, {minutes} минут, {seconds} секунд")
        
        if self.easter_egg_activated:
            print(f"  ⭐ Секретных активаций: {self.easter_egg_count}")
    
    def matrix_effect(self, *args):
        """Эффект матрицы"""
        print("\033[32m")  # Зеленый цвет
        chars = "01█▓▒░╬╫╪╨╧╩╦╥╤╣╢╡╠╟╞╝╜╛╚╙╘╗╖╕╔╓╒═║╶╴╵╷┃━┅┄┈┊┋╍╌"
        
        for _ in range(20):
            line = ""
            for _ in range(60):
                if random.random() < 0.3:
                    line += random.choice(chars)
                else:
                    line += " "
            print(line)
            time.sleep(0.05)
        print("\033[0m")
    
    def starfield(self, *args):
        """Эффект звездного неба"""
        print("\033[37m" + " " * 20 + "✦ СОЗВЕЗДИЕ SOLAROS ✦" + " " * 20 + "\033[0m")
        
        stars = ["✦", "★", "☆", "⋆", "✧", "✶", "✴", "✵", "⭑", "⭒"]
        
        for _ in range(15):
            line = " " * 20
            for _ in range(20):
                if random.random() < 0.2:
                    line += random.choice(stars)
                else:
                    line += " "
            print(line)
            time.sleep(0.1)
        print("\033[0m")
    
    def moon_phase(self, *args):
        """Показать фазы луны"""
        moon_phases = [
            "      🌑 Новолуние     ",
            "      🌒 Растущий серп ",
            "      🌓 Первая четверть",
            "      🌔 Растущая луна ",
            "      🌕 Полнолуние    ",
            "      🌖 Убывающая луна",
            "      🌗 Последняя четверть",
            "      🌘 Убывающий серп",
        ]
        
        for phase in moon_phases:
            print(" " * 20 + "\033[37m" + phase + "\033[0m" + " " * 20)
            time.sleep(0.2)
    
    def neofetch(self, *args):
        """Красивая информация о системе (как neofetch)"""
        colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
        
        print("\n" + "═" * 50)
        print("\033[36m" + " " * 15 + "╔══════════════════════╗" + "\033[0m")
        print("\033[36m" + " " * 15 + "║      SOLAROS INFO     ║" + "\033[0m")
        print("\033[36m" + " " * 15 + "╚══════════════════════╝" + "\033[0m")
        
        info_lines = [
            f"OS: SolarOS {VERSION}",
            f"Host: {platform.node()}",
            f"Kernel: Python {platform.python_version()}",
            f"Uptime: {self.show_uptime_detailed()}",
            f"Shell: SolarOS Terminal",
            f"CPU: {platform.processor()[:30]}...",
            f"Memory: {self.get_memory_info()}",
        ]
        
        for i, line in enumerate(info_lines):
            color = colors[i % len(colors)]
            print(f"  {color}{line}\033[0m")
        
        print("═" * 50)
    
    def show_uptime_detailed(self):
        """Детальное время работы для neofetch"""
        uptime = datetime.now() - self.boot_time
        return f"{uptime.days}d {uptime.seconds // 3600}h {(uptime.seconds % 3600) // 60}m"
    
    def get_memory_info(self):
        """Получить информацию о памяти"""
        try:
            import psutil
            memory = psutil.virtual_memory()
            return f"{memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB"
        except:
            return "Недоступно"
    
    def activate_easter_egg(self):
        """Активировать пасхалку с кодом 52437682"""
        self.easter_egg_activated = True
        self.easter_egg_count += 1
        
        print("\n" + "="*60)
        print("\033[35m" + "★" * 25 + " EASTER EGG ACTIVATED " + "★" * 25 + "\033[0m")
        print("="*60 + "\n")
        
        # Случайный эффект пасхалки
        effects = [
            self.easter_egg_effect_matrix,
            self.easter_egg_effect_stars,
            self.easter_egg_effect_dna,
            self.easter_egg_effect_moon,
            self.easter_egg_effect_solar,
        ]
        
        effect = random.choice(effects)
        effect()
        
        print("\n\033[32m" + "✓ Секретный код 52437682 распознан!")
        print("  Доступ к скрытым функциям SolarOS разрешен!")
        print("  Активирован уровень доступа: QUANTUM")
        print("  Количество активаций:", self.easter_egg_count, "\033[0m")
        
        # Специальное сообщение
        messages = [
            "Поздравляем! Вы нашли секретную команду разработчиков!",
            "Добро пожаловать в бэкдоры SolarOS!",
            "Системные ограничения сняты. Полный доступ предоставлен.",
            "Загрузка квантовых вычислений... Успешно!",
            "Доступ к лунной базе 'Альфа' разрешен."
        ]
        
        print("\n\033[36m" + random.choice(messages) + "\033[0m")
        print("\n" + "="*60)
        
        # Звуковые эффекты
        self.play_beep(800, 80)
        self.play_beep(1200, 80)
        self.play_beep(1600, 80)
        self.play_beep(2000, 80)
        self.play_beep(1600, 80)
        self.play_beep(1200, 80)
    
    def easter_egg_effect_matrix(self):
        """Эффект матрицы для пасхалки"""
        self.matrix_effect()
    
    def easter_egg_effect_stars(self):
        """Эффект звездного неба для пасхалки"""
        self.starfield()
    
    def easter_egg_effect_dna(self):
        """Эффект спирали ДНК"""
        print("\033[36m" + " " * 25 + "КВАНТОВАЯ СПИРАЛЬ" + " " * 25 + "\033[0m")
        
        for i in range(20):
            offset = i % 10
            left = " " * (20 + offset) + "█"
            right = " " * (20 - offset) + "█"
            
            if i % 2 == 0:
                print(left + "   ║   " + right)
            else:
                print(right + "   ║   " + left)
            time.sleep(0.1)
        print("\033[0m")
    
    def easter_egg_effect_moon(self):
        """Лунный эффект"""
        self.moon_phase()
    
    def easter_egg_effect_solar(self):
        """Солнечный эффект"""
        print("\033[33m" + " " * 20 + "☼ СОЛНЕЧНАЯ АКТИВНОСТЬ ☼" + " " * 20 + "\033[0m")
        
        for radius in range(1, 10):
            sun = " " * (25 - radius) + "☼" + "°" * (radius * 2) + "☼"
            print(sun)
            time.sleep(0.1)
        
        for radius in range(9, 0, -1):
            sun = " " * (25 - radius) + "☼" + "°" * (radius * 2) + "☼"
            print(sun)
            time.sleep(0.1)
        print("\033[0m")
    
    def secret_menu(self, *args):
        """Секретное меню (доступно после активации пасхалки)"""
        if not self.easter_egg_activated:
            print("\033[31mДоступ запрещён. Требуется активация секретного кода.\033[0m")
            return
        
        print("\n" + "="*60)
        print("\033[35m╔══════════════════════════════════════════════════════╗")
        print("║                  СЕКРЕТНОЕ МЕНЮ SOLAROS                ║")
        print("╚══════════════════════════════════════════════════════╝\033[0m")
        print()
        
        secrets = {
            "1": ("Квантовый калькулятор", self.quantum_calculator),
            "2": ("Система диагностики", self.system_diagnostic),
            "3": ("Генератор кодов", self.code_generator),
            "4": ("Лунный календарь", self.lunar_calendar),
            "5": ("Тайная переписка", self.secret_message),
            "6": ("Телепорт (симуляция)", self.teleport_sim),
            "7": ("Пасхальные яйца", self.show_easter_eggs),
            "8": ("Выйти", lambda: print("Выход из секретного меню"))
        }
        
        for key, (name, _) in secrets.items():
            print(f"  {key}. {name}")
        
        choice = input("\nВыберите опцию (1-8): ").strip()
        
        if choice in secrets:
            secrets[choice][1]()
        else:
            print("Неверный выбор!")
    
    def quantum_calculator(self):
        """Квантовый калькулятор"""
        print("\n\033[36m🔮 КВАНТОВЫЙ КАЛЬКУЛЯТОР 🔮\033[0m")
        print("Введите выражение (поддерживаются: +, -, *, /, ^, √, sin, cos):")
        
        expr = input(">> ").strip()
        
        try:
            # Безопасное вычисление
            expr = expr.replace('^', '**')
            expr = expr.replace('√', 'math.sqrt')
            expr = expr.replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            
            result = eval(expr, {"__builtins__": {}, "math": math}, {})
            
            print(f"\n\033[32mРезультат: {result}\033[0m")
            
            # Квантовые эффекты
            if random.random() < 0.3:
                print("\033[33m⚠  Обнаружена квантовая суперпозиция!")
                print(f"   Альтернативный результат: {result * random.uniform(0.9, 1.1)}\033[0m")
                
        except Exception as e:
            print(f"\033[31mОшибка: {e}\033[0m")
    
    def system_diagnostic(self):
        """Секретная диагностика системы"""
        print("\n\033[36m🛠  СЕКРЕТНАЯ ДИАГНОСТИКА СИСТЕМЫ 🛠\033[0m")
        
        checks = [
            ("Проверка квантового процессора", random.choice(["✅ ОК", "⚠  НЕСТАБИЛЬНО", "✅ ОПТИМАЛЬНО"])),
            ("Сканирование временных линий", random.choice(["✅ СТАБИЛЬНО", "⚠  АНОМАЛИИ", "✅ НОРМА"])),
            ("Мониторинг солнечной активности", random.choice(["✅ НИЗКАЯ", "✅ СРЕДНЯЯ", "⚠  ВЫСОКАЯ"])),
            ("Проверка лунной связи", random.choice(["✅ ОНЛАЙН", "❌ ОФФЛАЙН", "⚠  ПЕРЕМЕНЧИВО"])),
            ("Анализ энергощита", random.choice(["✅ 100%", "✅ 87%", "⚠  65%"])),
            ("Диагностика телепортации", random.choice(["✅ ГОТОВО", "⚠  КАЛИБРОВКА", "❌ ОШИБКА"])),
        ]
        
        for check, status in checks:
            print(f"  {check:40} {status}")
            time.sleep(0.3)
        
        print(f"\n\033[32m✓ Диагностика завершена. Время: {datetime.now().strftime('%H:%M:%S')}\033[0m")
    
    def code_generator(self):
        """Генератор секретных кодов"""
        print("\n\033[36m🔐 ГЕНЕРАТОР СЕКРЕТНЫХ КОДОВ 🔐\033[0m")
        
        codes = []
        for i in range(5):
            code = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
            codes.append(code)
            print(f"  Код {i+1}: {code}")
            time.sleep(0.2)
        
        print("\n\033[33m⚠  Коды самоуничтожатся через 10 секунд...\033[0m")
        time.sleep(3)
        print("\033[31mКоды уничтожены!\033[0m")
    
    def lunar_calendar(self):
        """Лунный календарь"""
        print("\n\033[36m🌙 ЛУННЫЙ КАЛЕНДАРЬ 🌙\033[0m")
        
        phases = [
            ("🌑 Новолуние", "Начало новых проектов"),
            ("🌒 Растущий серп", "Планирование и подготовка"),
            ("🌓 Первая четверть", "Активные действия"),
            ("🌔 Растущая луна", "Развитие и рост"),
            ("🌕 Полнолуние", "Завершение и результаты"),
            ("🌖 Убывающая луна", "Анализ и подведение итогов"),
            ("🌗 Последняя четверть", "Отпускание старого"),
            ("🌘 Убывающий серп", "Отдых и подготовка"),
        ]
        
        for phase, meaning in phases:
            print(f"  {phase:20} - {meaning}")
            time.sleep(0.3)
    
    def secret_message(self):
        """Тайная переписка"""
        print("\n\033[36m✉  ТАЙНАЯ ПЕРЕПИСКА ✉\033[0m")
        message = input("Введите сообщение для шифрования: ")
        
        # Простое шифрование
        encrypted = ''.join(chr(ord(c) + 3) for c in message)
        print(f"\nЗашифрованное сообщение: \033[33m{encrypted}\033[0m")
        print("Ключ шифрования: +3 к коду символа")
    
    def teleport_sim(self):
        """Симулятор телепортации"""
        print("\n\033[36m🌀 СИМУЛЯЦИЯ ТЕЛЕПОРТАЦИИ 🌀\033[0m")
        
        locations = [
            "Лунная база 'Альфа'",
            "Орбитальная станция 'Солнечный луч'",
            "Марсианская колония 'Красный рассвет'",
            "Пояс астероидов C-137",
            "Квантовое пространство Ω",
        ]
        
        for i in range(5, 0, -1):
            print(f"  Телепортация через {i}...")
            time.sleep(0.5)
        
        destination = random.choice(locations)
        print(f"\n\033[32m✓ Успешно телепортирован в: {destination}\033[0m")
    
    def show_easter_eggs(self):
        """Показать найденные пасхалки"""
        print("\n\033[36m🥚 НАЙДЕННЫЕ ПАСХАЛКИ 🥚\033[0m")
        print(f"  Основной код (52437682): {'✅ Найден' if self.easter_egg_activated else '❌ Не найден'}")
        print(f"  Количество активаций: {self.easter_egg_count}")
        print("\nДругие пасхальные команды:")
        print("  konst, createlab, solar, moonbase, alpha")
    
    def execute_command(self, command):
        """Выполнить команду"""
        self.history.append(command)
        
        # Проверка на пасхалку
        if command.strip() == self.secret_code:
            self.activate_easter_egg()
            return
        
        # Проверка на другие пасхальные команды
        if command.strip().lower() in [cmd.lower() for cmd in self.easter_egg_commands if cmd != self.secret_code]:
            print("\033[33mПасхалка обнаружена! Но правильный код: 52437682\033[0m")
            return
        
        # Разбиваем команду на части
        parts = command.strip().split()
        if not parts:
            return
        
        cmd_name = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Проверяем существование команды
        if cmd_name in self.commands:
            try:
                self.commands[cmd_name](*args)
            except Exception as e:
                print(f"Ошибка выполнения команды: {e}")
        else:
            # Пытаемся выполнить как системную команду
            try:
                os.system(command)
            except:
                print(f"Команда не найдена: {cmd_name}")
                print("Введите 'help' для списка доступных команд")
    
    def run(self):
        """Главный цикл SolarOS"""
        self.show_bios_screen()
        time.sleep(0.5)
        self.clear_screen()
        self.print_banner()
        
        print("Введите 'help' для списка команд")
        print("Введите 'exit' для выхода")
        print("\033[33m" + "💡 Подсказка: попробуйте ввести код 52437682" + "\033[0m")
        print()
        
        while self.running:
            try:
                # Формируем приглашение с текущей директорией
                dir_name = os.path.basename(self.current_dir) if self.current_dir else "~"
                prompt_base = f"SolarOS:{dir_name}"
                
                if self.easter_egg_activated:
                    prompt = f"\033[35m⭐{prompt_base}>\033[0m "
                else:
                    prompt = f"\033[36m{prompt_base}>\033[0m "
                
                command = input(prompt).strip()
                
                if command:
                    self.execute_command(command)
                    
            except KeyboardInterrupt:
                print("\n\nДля выхода введите 'exit'")
            except EOFError:
                print("\n\nЗавершение работы...")
                self.running = False
            except Exception as e:
                print(f"Критическая ошибка: {e}")
                self.running = False
        
        print("\nSolarOS завершил работу. До свидания!")

def main():
    """Точка входа в программу"""
    try:
        print("\033[0m")  # Сброс цветов
        print("Запуск SolarOS Quantum Edition...")
        time.sleep(0.5)
        
        os_system = SolarOS()
        os_system.run()
    except Exception as e:
        print(f"Ошибка запуска SolarOS: {e}")
        input("\nНажмите Enter для выхода...")
    finally:
        print("\033[0m")  # Всегда сбрасываем цвет перед выходом

if __name__ == "__main__":
    main()

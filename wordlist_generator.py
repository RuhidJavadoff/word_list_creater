import itertools
import os
import time

def display_header():
    """
    Bu funksiya proqram başlayanda ekrana başlığı, yəni "RJ" bannerini 
    və təlimatları çıxarır.
    """
    # Terminalı təmizləyir (Windows üçün 'cls', digərləri üçün 'clear')
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    # "RJ" üçün sadə ASCII art banner
    print("="*50)
    print(r"""
          ____  _      
         |  _ \(_)     
         | |_) |_ _ __ 
         |  _ <| | '__|
         |_| \_\ | |   
              |_|_|   
    """)
    print("="*50)
    print("\n--- Wordlist Generator ---")
    
    # İki dildə açıqlama
    print("\nEN: Enter characters, min/max length, and I will generate a wordlist for you.")
    print("AZ: Wordlist yaratmaq üçün simvolları, minimum/maksimum uzunluğu daxil edin.")
    print("-"*50)

def generate_wordlist():
    """
    Əsas funksiya: istifadəçidən məlumatları alır və wordlist-i yaradır.
    """
    display_header()
    
    # İstifadəçidən məlumatların alınması
    chars = input("\n[?] Characters to use (İstifadə ediləcək simvollar): ")
    
    # Rəqəm daxil edilməsini yoxlamaq üçün döngü
    while True:
        try:
            min_len = int(input("[?] Minimum length (Minimum uzunluq): "))
            max_len = int(input("[?] Maximum length (Maksimum uzunluq): "))
            if min_len > 0 and max_len >= min_len:
                break
            else:
                print("\n[!] XƏTA: Minimum uzunluq 0-dan böyük, maksimum isə minimumdan kiçik olmamalıdır.")
        except ValueError:
            print("\n[!] XƏTA: Zəhmət olmasa, uzunluq üçün yalnız rəqəm daxil edin.")

    output_file = input("[?] Output file name (Yekun faylın adı) [wordlist.txt]: ")
    if not output_file:
        output_file = "wordlist.txt"

    print("\n" + "="*50)
    print(f"[*] Proses başlayır... Simvollar: '{chars}', Uzunluq: {min_len}-{max_len}")
    print(f"[*] Nəticələr '{output_file}' faylına yazılacaq.")
    print("="*50 + "\n")

    start_time = time.time()
    word_count = 0
    
    try:
        # Faylı 'yazma' rejimində açırıq
        with open(output_file, 'w', encoding='utf-8') as f:
            # Minimum və maksimum uzunluq arasında döngü yaradırıq
            for length in range(min_len, max_len + 1):
                print(f"[*] {length} simvol uzunluğunda kombinasiyalar yaradılır...")
                # itertools.product ilə bütün mümkün kombinasiyaları yaradırıq
                for item in itertools.product(chars, repeat=length):
                    word = "".join(item)
                    f.write(word + '\n')
                    word_count += 1
        
        end_time = time.time()
        duration = end_time - start_time
        
        print("\n" + "="*50)
        print(f"[SUCCESS] Proses uğurla başa çatdı!")
        print(f"[i] Cəmi {word_count} söz yaradıldı.")
        print(f"[i] Proses {duration:.2f} saniyə çəkdi.")
        print(f"[i] Nəticələr '{output_file}' faylında saxlandı.")
        print("="*50)

    except Exception as e:
        print(f"\n[!] XƏTA: Faylın yazılması zamanı problem yarandı: {e}")

# Proqramı başladan əsas hissə
if __name__ == "__main__":
    generate_wordlist()

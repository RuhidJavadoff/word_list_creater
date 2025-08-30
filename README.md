🔑 RJ Wordlist Generator
<p align="center">
A powerful and user-friendly command-line tool written in Python to generate custom wordlists based on a specific character set, with defined minimum and maximum lengths.
</p>

🌟 About The Project
RJ Wordlist Generator is a simple yet effective script for creating wordlists for various purposes, such as penetration testing, password recovery drills, or data generation. The tool prompts the user to enter a set of characters (letters, numbers, symbols), specify the minimum and maximum length for the words, and then generates all possible combinations, saving them to a .txt file.

To ensure it's easy to use for everyone, the interface provides instructions in both English and Azerbaijani.

✅ Key Features:
Custom Character Sets: Use any combination of letters, numbers, and symbols you need.

Flexible Length: Define a minimum and maximum length for the generated words.

User-Friendly CLI: An interactive command-line interface that guides you through the process.

Dual Language Support: Instructions are provided in both English (EN) and Azerbaijani (AZ).

High Performance: Built with Python's highly optimized itertools library for fast combination generation.

Cross-Platform: Works on Windows, macOS, and Linux.

🚀 Usage Demonstration
Here is a quick demonstration of how the script works in the terminal.

$ python wordlist_generator.py

==================================================
          ____  _      
         |  _ \(_)     
         | |_) |_ _ __ 
         |  _ <| | '__|
         |_| \_\ | |   
              |_|_|   
    
==================================================

--- Wordlist Generator ---

EN: Enter characters, min/max length, and I will generate a wordlist for you.
AZ: Wordlist yaratmaq üçün simvolları, minimum/maksimum uzunluğu daxil edin.
--------------------------------------------------

[?] Characters to use (İstifadə ediləcək simvollar): rj12
[?] Minimum length (Minimum uzunluq): 3
[?] Maximum length (Maksimum uzunluq): 4
[?] Output file name (Yekun faylın adı) [wordlist.txt]: my_words.txt

==================================================
[*] Proses başlayır... Simvollar: 'rj12', Uzunluq: 3-4
[*] Nəticələr 'my_words.txt' faylına yazılacaq.
==================================================

[*] 3 simvol uzunluğunda kombinasiyalar yaradılır...
[*] 4 simvol uzunluğunda kombinasiyalar yaradılır...

==================================================
[SUCCESS] Proses uğurla başa çatdı!
[i] Cəmi 320 söz yaradıldı.
[i] Proses 0.01 saniyə çəkdi.
[i] Nəticələr 'my_words.txt' faylında saxlandı.
==================================================

🛠️ How to Use (Setup & Run)
To get this script running on your local machine, follow these simple steps.

Prerequisites
You need to have Python installed on your system. If you don't have it, you can download it from python.org.

Installation & Execution
Get the code
Clone the repository or download the ZIP file.

git clone [https://github.com/RuhidJavadoff/RJ-Wordlist-Generator.git](https://github.com/RuhidJavadoff/RJ-Wordlist-Generator.git)

(Note: Repository URL will be your actual URL)

Navigate to the project directory
Open your terminal or command prompt and move into the project folder.

cd RJ-Wordlist-Generator

Run the script!
Execute the Python script with the following command:

python wordlist_generator.py

The script will then guide you through the next steps interactively.

⚠️ Important Warning
Please be aware that the number of possible combinations grows exponentially with the number of characters and the length of the words. Generating a wordlist with a large character set and a high maximum length can take a very long time and create an extremely large file (many Gigabytes or even Terabytes). Start with small character sets and lengths to understand the performance.

💖 Support Us
If you find this project useful and wish to support its development, you can do so through the methods below. Your support is greatly appreciated!

<p align="center">
<a href="mailto:ruhidjavadoff@gmail.com">
<img src="https://img.shields.io/badge/Support-Email_PayPal-blue?style=for-the-badge&logo=paypal" alt="Email PayPal">
</a>
<a href="https://ruhidjavadoff.site/donate/" target="_blank">
<img src="https://img.shields.io/badge/Support-Web_Site-green?style=for-the-badge&logo=donate" alt="Support via Website">
</a>
</p>

🌐 Follow Us & Contact
Stay updated on my projects and feel free to contact me via the links below:

<p align="center">
<a href="https://ruhidjavadoff.site/followme/" target="_blank">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Follow_Me-Social_Media-purple%3Fstyle%3Dfor-the-badge%26logo%3Drss" alt="Follow Us on Social Media">
</a>
<a href="https://wa.me/994506636031" target="_blank">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/WhatsApp-Contact_Me-25D366%3Fstyle%3Dfor-the-badge%26logo%3Dwhatsapp%26logoColor%3Dwhite" alt="Contact via WhatsApp">
</a>
</p>

📄 License
This project is licensed under the MIT License - see the LICENSE file for details. You are free to use, modify, and distribute it.

🧑‍💻 Author
Ruhid Javadoff / veb.developher.az

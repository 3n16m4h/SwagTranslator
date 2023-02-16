import os   
import time
import random
import pyfiglet
from termcolor import colored

# Swag
swag_ascii = pyfiglet.figlet_format("Swag")
swag_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print(colored(swag_ascii, swag_color))

# Input
message = input("Inserisci la stringa da tradurre: ")

# C++
cpp_translation = 'std::cout << "' + message + '" << std::endl;'
cpp_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("C++:", colored(cpp_translation, cpp_color))

# C#
csharp_translation = 'Console.WriteLine("' + message + '");'
csharp_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("C#:", colored(csharp_translation, csharp_color))

# Java
java_translation = 'System.out.println("' + message + '");'
java_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Java:", colored(java_translation, java_color))

# JavaScript
js_translation = 'console.log("' + message + '");'
js_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("JavaScript:", colored(js_translation, js_color))

# PHP
php_translation = 'echo "' + message + '";'
php_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("PHP:", colored(php_translation, php_color))

# HTML
html_translation = "<p>" + message + "</p>"
html_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("HTML:", colored(html_translation, html_color))

# Brainfuck
bf_translation = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
bf_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Brainfuck:", colored(bf_translation, bf_color))

# Rust
rust_translation = 'println!("' + message + '");'
rust_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Rust:", colored(rust_translation, rust_color))

# R
r_translation = 'print("' + message + '")'
r_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("R:", colored(r_translation, r_color))

# Swift
swift_translation = 'print("' + message + '")'
swift_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Swift:", colored(swift_translation, swift_color))

# Go
go_translation = 'fmt.Println("' + message + '")'
go_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Go:", colored(go_translation, go_color))

# Ruby
ruby_translation = 'puts "' + message + '"'
ruby_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Ruby:", colored(ruby_translation, ruby_color))

# Ook
ook_translation = ""
for char in message:
    ook_translation += "+".rjust(ord(char)+1, "!") + "."
ook_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Ook!:", colored(ook_translation, ook_color))

# Moo
moo_translation = "m" * len(message) + " oO" + "\n" + "MOO" + "!" * len(message)
moo_color = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan"])
print("Moo:", colored(moo_translation, moo_color))

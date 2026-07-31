# Bandit Level 12

## Goal


host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit12
hasło: sprawdz level-11

ssh bandit12@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p

Celem tego poziomu jest znalezienie hasła znajdującego się w pliku data.txt który jest:
- zrzutem szesnastkowym pliku
- plik ten był wielokrotnie kompresowany
Na tym poziomie przydatne będzie utworzenie katalogu w /tmp w którym będziemy mogli pracować.

Użyjemy do tego komendy:
`mktemp -d`

Tworzy ona folder z randomowa nazwa:
`/tmp/tmp.m6iy6xfFqK`

W poleceniu mamy do wykonania następujące kroki:
- skopiuj plik danych za pomocą cp i zmień jego nazwe za pomocą mv

### Solution
A więc:
`cp data.txt /tmp/tmp.m6iy6xfFqK`

Następnie przechodzimy do folderu tmp.

Sprawdzamy co to za plik:
`file data.txt`

`data.txt: ASCII text`

Wiemy że to hexdump, cofniemy hexdump do postaci binarnej
użyjemy:
`xxd -r data.txt > data.bin`

Normalnie, rozpakowywalibyśmy to ręcznie używając komend: 
`tar, gzip, gunzip, bzip2`

Możemy jednak zautomatyzować to zadanie za pomocą pythonowego skryptu:

```
# Bandit assumption: # archive contains exactly one file

import subprocess
import os
import gzip
import bz2
import tarfile
import shutil
import sys
import time

if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <file>')
        sys.exit()


filename = sys.argv[1]

time.sleep(1)
print(f"Startuje od: {filename}\n")
time.sleep(1)


def detect_file_type(filename):

        with open(filename, 'rb') as file:
                header = file.read(512)

                if header[:2] == b'\x1f\x8b':
                        return 'gzip'
                if header[:3] == b'BZh':
                        return 'bzip2'
                if header[257:262] == b"ustar":
                        return "tar"

                return 'text'




while True:
        filetype = detect_file_type(filename)
        print(f"filetype -> {filetype}")

        if filetype == 'gzip':
                new_name = filename + "_tmp"

                with gzip.open(filename, 'rb') as src:
                        with open(new_name, 'wb') as dst:
                                shutil.copyfileobj(src, dst)
                os.remove(filename)
                os.rename(new_name, filename)

        elif filetype == 'bzip2':
                new_name = filename + '_tmp'

                with bz2.open(filename, 'rb') as src:
                        with open(new_name, 'wb') as dst:
                                shutil.copyfileobj(src, dst)


                os.remove(filename)
                os.rename(new_name, filename)

        elif filetype == 'tar':
                new_name = filename + '_tmp'

                with tarfile.open(filename) as tar:
                        members = tar.getmembers()

                        member = members[0]
                        tar.extract(member)
                os.remove(filename)
                filename = member.name

        else:
                print('--- ZAWARTOŚĆ ---\n')
                with open(filename, 'r') as file:
                        print(file.read())
                break

```


Tak znajdujemy hasło i automatyzujmy proces:)

### Lessons learned

- file nie patrzy na rozszerzenie, tylko na sygnaturę pliku
- gzip != archiwum, tylko kompresja jednego pliku
- tar może zawierać wiele plików
- magic bytes pozwalają rozpoznać format
- sys.argv pozwala przekazywać pliki do skryptu
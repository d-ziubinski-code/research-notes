# Bandit Level 03

## Goal

Celem tego poziomu jest znalezienie hasła znajdującego w jedynym pliku czytelny dla człowieka w katalogu inhere.




host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit4
hasło: sprawdz level-03

ssh bandit4@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit4@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls

W tym levelu problemem jest to, że w folderze w ktorym jest nasz plik, jest kilka innych plikow.

Plik ktory musimy znalezc to plik czytelny dla czlowieka

Mozemy to zrobic za pomoca komendy:

file -i inhere/*

tym sposobem uzyskamy liste plikow i ich charset

inhere/-file00: application/octet-stream; charset=binary
inhere/-file01: application/octet-stream; charset=binary
inhere/-file02: application/octet-stream; charset=binary
inhere/-file03: application/octet-stream; charset=binary
inhere/-file04: application/octet-stream; charset=binary
inhere/-file05: application/octet-stream; charset=binary
inhere/-file06: application/octet-stream; charset=binary
inhere/-file07: text/plain; charset=us-ascii
inhere/-file08: application/octet-stream; charset=binary
inhere/-file09: application/octet-stream; charset=binary

Jak mozna zauwazyc plik -file-07 jest tekstowy i ma charset ascii czyli czytelny dla czlowieka

Wyswietlamy zawartosc pliku pamietajac, ze ma znak "-" na poczatku co moze powodowac blad bez argumentu --

wyswietlamy plik nastepująco:

cat -- inhere/-file-07

Wyswietla sie hasło :D


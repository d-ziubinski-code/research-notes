# Bandit Level 03

## Goal

Celem tego poziomu jest znalezienie hasła znajdującego się w ukrytym pliku w folderze inhere



host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit3
hasło: sprawdz level-02

ssh bandit3@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit3@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls

W tym levelu problemem jest to, że folder jest ukryty.

Ukryte foldery, mozemy zobacazym w prosty sposob

komenda:

ls -la inhere

wyswietli ukryte pliki w folderze do ktorego sciezke podamy

nastepnie mozemy przeczytac zawartosc ukrytego pliku

cat inhere/...Hiding-From-You

Tak zdobywamy hasło do poziomu 4


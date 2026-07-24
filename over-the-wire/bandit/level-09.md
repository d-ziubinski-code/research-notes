# Bandit Level 09

## Goal

Celem tego poziomu jest znalezienie słowa znajdującego się w pliku data.txt, oraz występującego tylko raz

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit9
hasło: sprawdz level-08

ssh bandit9@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit9@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls


Na tym poziomie, celem jest znalezienie hasla w pliku data,txt w kilku czytelnych dla czlowieka stringach.

W linuxie, mamy polecenie wyciagania human-readable stringow z plikow, jest to polecenie strings

uzywamy wiec:
strings data.txt

Dostajemy wszystkie mozliwe do przeczytania dla czlowieka znaki, ciezko znalezc w tym haslo.

Mamy jednak jeszcze jedna informacje, string ktorego szukamy zaczyna sie od kilku "="

W taki przypadku mozemy uzyc polecenia grep w pipeline z naszym wczesniejszym strings:

strings data.txt | grep "=*"


Tak znajdujemy haslo.
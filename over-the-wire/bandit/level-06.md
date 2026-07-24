# Bandit Level 06

## Goal

Celem tego poziomu jest znalezienie hasła znajdującego sie "gdzieś na serwerze" oraz:
	- Właścicielem pliku jest user bandit7
	- Grupą do której należy plik jest bandit6
	- zajmuje 33 bajty pamięci



host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit6
hasło: sprawdz level-05

ssh bandit6@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit6@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls


Tak jak w przypadku poziomu 5, musimy użyc komendy find:

dinr -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null

/var/lib/dpkg/info/bandit7.password



"2>/dev/null" - dzieki temu dopiskowi nie widzimy folderow w ktorych pliku nie znaleziono, w teminalu wyswietla sie jedynie sciezka do poprawnego pliku.


następnie wyswietlamy zawartosc

cat /var/lib/dpkg/info/bandit7.password

Zdobyliśmy hasło do levelu 7 :)

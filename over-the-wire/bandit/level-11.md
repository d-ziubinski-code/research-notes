# Bandit Level 11

## Goal

Celem tego poziomu jest znalezienie słowa znajdującego się w pliku data.txt, gdzie wszystkie małe i wielkie litery a-z zostaly przesuniete o 13 pozycji

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit11
hasło: sprawdz level-10

ssh bandit10@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit11@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls

Hasło znajduję się w pliku `data.txt` który zawiera tekst w którym każda litera została przesunięta o 13 pozycji.

Najpierw sprawdźmy co to za plik:
`file data.txt`

Zwraca:
`data.txt: ASCII text`

`file` potwierdza, że zawartość pliku jest tekstem ASCII. Rozszerzenie `data.txt` również to sugeruje, jednak `file` określa typ na podstawie zawartości pliku, a nie jego nazw

Teraz możemy wyświetlić początek jego zawartości:
`head -c 64 data.txt`

Zwróci:
`Gur cnffjbeq vf TEBbmJCB8DlA0zTewHxVQ0JPLxMvDkeA`

Aby odwrócić każdą literę o 13 pozycji, napiszemy skrypt w języku Python.

Nie możemy tworzyć nowych plików w katalogu usera bandit 11.

W takim razie, przejdziemy do folderu tmp/ (temporary) w ktorym powinnismy moc utworzyc skrypt

`cd ../../tmp`

W tym folderze, tworzymy nowy plik `main` z roszerzeniem `.py`

`nano main.py`


Zaimplementujemy funkcję `rot13()`, która dla każdej litery:

- zamieni ją na pozycję w alfabecie,
- przesunie o 13 miejsc,
- zawinie alfabet za pomocą operatora `%`,
- zamieni wynik z powrotem na znak.

```
def rot13(letter):
	#duze litery
	
	if 'A' <= letter <= 'Z':
		position = ord(letter) - ord('A')
		position = (position + 13) % 26  #zwraca reszte z dzielenia
		return chr(position + ord('A'))
		
	elif 'a' <= letter <= 'z':
		position = ord(letter) - ord('a')
		position = (position + 13) % 26
		return chr(position + ord('a'))
		
	return letter
	
	

data = open('../home/bandit11/data.txt').read().strip()

output = ""

for letter in data:
	output += rot13(letter)
	
print(output)
```

Skrypt uruchamiamy z katalogu `/tmp`, dlatego używamy ścieżki względnej `../home/bandit11/data.txt`.

W funkcji rot13, uzywamy `%` ze względu na to, że w przypadku dalszych liter alfabetu, do których dodanie 13 bedzię sie równało więcej niż 26 (czyli tyle ile jest mozliwych liter w alfabecie). "Zawijamy" w ten sposób alfabet.

Po zapisaniu `Ctrl + X`, możemy odpalić nasz skrypt:
`python3 main.py`

Dostajemy hasło:

## Czego nauczyłem się na tym poziomie?

- `file` identyfikuje typ pliku na podstawie zawartości.
- Nie każdy katalog jest zapisywalny przez użytkownika.
- `/tmp` służy do przechowywania plików tymczasowych.
- `ord()` zamienia znak na jego kod ASCII.
- `chr()` zamienia kod ASCII na znak.
- Operator `%` pozwala "zawinąć" alfabet po przekroczeniu litery `Z` lub `z`.
- Problem można rozwiązać zarówno własnym skryptem, jak i narzędziami systemowymi.
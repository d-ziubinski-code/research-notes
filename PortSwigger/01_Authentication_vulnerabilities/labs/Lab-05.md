## Podatności

- nieskuteczny mechanizm account lockout / rate limiting
- **password spraying**
- **Password Brute-force** - atak słownikowy na hasło użytkownika `carlos`.

Ten lab jest podatny na wyliczanie nazw użytkowników.
Wykorzystuje ono blokowanie kont.

## Metodologia: Lab 5

#### Krok 1: Username Enumeration

**Zasada działania podatności:** Aplikacja blokuje konto po określonej liczbie nieudanych prób logowania (5 błędnych hasłach dla _tego samego_ użytkownika).

- Wyślij listę kandydatów na nazwy użytkowników (Candidate usernames) w narzędziu Intruder (Cluster Bomb), dla password daj wartosw null bytes. Pamietaj zeby ustawic 5 wygenerowanych payloadow.
    
- Dla każdego użytkownika wyślij serię prób z błędnymi hasłami, aż konto zostanie zablokowane.
    
- Obserwuj komunikat o błędzie (np. _“Account locked”_ vs _“Invalid username or password”_).
    
- Jeśli licznik błędnych prób **nie resetuje się** globalnie lub występuje luka w logice resetowania licznika po poprawnej próbie dla _innego_ konta, możesz wyliczyć poprawne konto.

##### Sposób 2 - skrypt Python

1. Tworzymy folder dla naszego skryptu, tworzymy w nim dwa pliki: `usernames.txt` i `main.py`
2. Do `usernames.txt` wklejamy podane nazwy użytkownika podane w opisie zadania 
3. Naszym celem będzię stworzenie nowego pliku w którym każda nazwa użytkownika będzie powtórzona 5 razy:
```
with open("usernames.txt", 'r+') as f:
	new_tab = [line.strip() for line in f if line.strip() for _ in range(5)]
	
	f.seek(0)
	f.truncate()
	
	f.write("\n".join(new_tab) + "\n")
print("Zapisano...")
```

4. Po poprawnym stworzeniu nowej listy przechodzimy do Burp Suite i wybieramy atak typu **Pitchfork attack**.
5. Wklejamy przygotowaną listę jako **pierwszy payload** dla nazw użytkowników. Dla haseł wybieramy payload typu **Null payloads** i ustawiamy wygenerowanie odpowiedniej liczby payloadów (np. 505 ze względu na liczbę nazw użytkowników).
6. Obserwujemy kolumnę **Length** - dla zablokowanego konta długość odpowiedzi będzie większa.


#### Krok 2: Znalezienie hasła dla użytkownika

Gdy masz już potwierdzone konto :

1. Skonfiguruj Intruder wyłącznie dla znalezionego usera. Wybierz atack - "Sniper attack"
    
2. Podepnij słownik haseł (Candidate passwords).
    
3. Uważaj na mechanizm blokady – po 5 próbach konto blokuje się na minutę, należy ustawić request delay na 60000 ms - atak będzie trwać max 100 minut.
4. Przy poprawnym zalogowaniu otrzymamy inną wartość w kolumnie `length` - to właśnie nasze hasło

#### Krok 3: Zaliczenie laba
1. Wejdź na stronę konta usera, aby rozwiązać lab.
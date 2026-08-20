## Podatności
- **Username Enumeration** - enumeracja nazw użytkowników
- **Password Brute Force** - atak słownikowy na hasło

W tym labie różnica, której szukamy, **jest bardzo niewielka i nie jest widoczna na pierwszy rzut oka**.

## Metodologia: Lab 02
Formularz logowania zwracał taki sam status HTTP dla każdej próby:

```
200 OK
```

Sam kod HTTP nie pozwalał więc określić, czy użytkownik istnieje.

Teoretycznie nie pomagał w tym również komunikat zwracany przez aplikację:

```
Invalid username or password.
```

Dlatego konieczne było przeanalizowanie pełnej odpowiedzi HTTP i znalezienie subtelnej różnicy między requestami.

## Username Enumeration
Pierwszym krokiem było znalezienie poprawnego username.

Do tego wykorzystamy **Burp Suite Intruder**.

Przeprowadzamy atak na parametr `username`, pozostawiając losowe, niepoprawne hasło. Jako payload wykorzystujemy listę `usernames` podaną w treści zadania.

Po uruchomieniu ataku widzimy, że odpowiedzi są bardzo podobne i ciężko zauważyć jakąkolwiek anomalię.

Możemy więc spróbować dodać odpowiednie filtrowanie.

W tym przypadku przefiltrujemy odpowiedzi na podstawie treści komunikatu wyświetlanego po próbie logowania.

W Intruderze przechodzimy do zakładki `Settings`, a następnie do sekcji `Grep - Extract`.

Znajdujemy interesującą nas wartość w response i zaznaczamy ją.

Po zastosowaniu filtra i ponownym uruchomieniu ataku otrzymujemy dodatkową kolumnę zawierającą wyodrębnioną wartość z odpowiedzi każdego requestu.

Następnie sortujemy wyniki według tej kolumny. Na samej górze pojawia się request, którego odpowiedź różni się od pozostałych.

W większości odpowiedzi komunikat wyglądał tak:

```
Invalid username or password.
```

Natomiast w jednej odpowiedzi brakowało końcowej kropki:

```
Invalid username or password
```

Ta niewielka różnica może wskazywać na istniejącego użytkownika.

## Password Brute Force
Mając prawdopodobnie poprawny username, przeprowadzamy atak słownikowy na hasło.

Wklejamy listę haseł podaną w treści zadania jako payload w miejsce parametru `password`.

Następnie uruchamiamy atak.

W wynikach widzimy, że większość requestów zwraca ten sam status HTTP, natomiast jeden z nich zwraca:

```
302 Found
```

Jest to anomalia na tle pozostałych odpowiedzi i może wskazywać na poprawne uwierzytelnienie.
Próbujemy zalogować się przy użyciu znalezionego wcześniej username oraz hasła.

Aplikacja zwraca:
```
Login Successful!
```
Oznacza to, że znaleźliśmy poprawne dane logowania i przejęliśmy konto użytkownika.
## !
- Nie zawsze kod HTTP wskazuje sukces lub porażkę — **zależy to od sposobu implementacji aplikacji**.
- Podczas testowania logowania należy analizować pełną odpowiedź HTTP.
- Warto zwracać uwagę na różnice w **status code, response length, response body, nagłówkach oraz redirectach**.
- W tym przypadku **HTTP 302** był wskaźnikiem poprawnego uwierzytelnienia, ponieważ pozostałe próby zwracały inny status.
- Username Enumeration często jest pierwszym krokiem przed atakiem na hasło.
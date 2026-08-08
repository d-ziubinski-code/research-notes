### Podatność

- Username Enumeration (enumeracja nazw użytkowników)
- Password Brute Force (atak słownikowy na hasło)

### Cel

Znaleźć poprawną nazwę, użytkownika, następnie przeprowadzić atak brute-force na hasło i uzyskać dostęp do konta użytkownika.

Mamy podane dwie listy usernames i passwords, w nich znajduje sie poprawny login i haslo.

### Solution

Formularz logowania zwracał taki sam status HTTP dla każdej próby:

`200 OK`


Sam kod HTTP nie pozwalał określić, czy użytkownik istnieje.

Należało więc przeanalizować inne elementy odpowiedzi:

- Response length
- Response body
- komunikaty błędów
- Response time

## Username Enumeration

Pierwszym krokiem było znalezienie poprawnego username.

Można zrobić to ręcznie, wysyłając różne nazwy użytkowników wraz z losowym hasłem i obserwując różnice w odpowiedziach.

Bardziej efektywną metodą jest użycie Burp Suite Intruder.

Po znalezieniu poprawnej nazwy użytkownika aplikacja zwracała inny komunikat:

`Invalid password`

Oznaczało to, że konto istnieje, ale hasło jest niepoprawne.

## Password Brute Force

Mając poprawny username, przeprowadzamy atak słownikowy na hasło.

Wykorzystałem listę dostępnych haseł i ponownie przeanalizowałem odpowiedzi.

Ponieważ wszystkie odpowiedzi miały ten sam status HTTP:
`200 OK`

należało znaleźć inną anomalię.

W tym przypadku poprawne hasło wyróżniało się inną wartością:
`Response length`

Na podstawie tej różnicy udało się znaleźć poprawne dane logowania.


---

### Important

- Nie zawsze kod HTTP wskazuje sukces lub porażkę.
- Podczas testowania logowania należy analizować pełną odpowiedź HTTP.
- Username enumeration często jest pierwszym krokiem przed atakiem na hasła.
- Różnice w długości odpowiedzi mogą ujawnić ukryte informacje.
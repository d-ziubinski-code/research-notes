# Authentication Vulnerabilities

## Authentication

### Definicja

Authentication (uwierzytelnianie) sprawdza, **kim jest użytkownik**.

Odpowiada na pytanie:

> Czy naprawdę jesteś tą osobą?

---

### Czynniki uwierzytelniania

**Knowledge**

- hasło
- PIN

**Possession**

- telefon
- token
- aplikacja OTP

**Inherence**

- odcisk palca
- FaceID
- biometria

---

## Authentication vs Authorization

Authentication

> Kim jesteś?

Authorization

> Co możesz zrobić?

Najpierw Authentication.

Potem Authorization.

---

## Najczęstsze przyczyny podatności 

Najczęstsze przyczyny:

- słabe mechanizmy logowania
- błędy logiki aplikacji

Przykłady:

- brak limitu prób
- możliwość pominięcia logowania
- błędna obsługa sesji
- przewidywalne tokeny

---

## Skutki

Przejęcie konta użytkownika.

Przejęcie konta administratora.

Dostęp do danych.

Możliwy dostęp do infrastruktury.

---

## Co zapamiętać?

Authentication = **Identity**

Authorization = **Permissions**

---

## Jak myśli pentester?

Nie pytam:

> Czy login działa?

Pytam:

- Czy mogę go ominąć?
- Czy mogę podszyć się pod innego użytkownika?
- Czy aplikacja ufa temu, co wysyłam?

# Luki w logowaniu opartym na haśle

W tym scenariuszu, fakt znajomości przez użytkownika hasła jest wystarczający do potwierdzenia tożsamości

Może to zostać osiągnięte na wiele sposobów, jednym z nich jest na przykład brute-force

# Atak Brute-Force

Atak polegający na wielokrotnych próbach logowania aż do odnalezienia poprawnych danych uwierzytelniających.

Najczęściej jest zautomatyzowany i wykorzystuje:

- listy loginów,
- słowniki haseł,
- dane z wcześniejszych wycieków.

Atak nie zawsze polega na losowym zgadywaniu — słowniki mogą być dostosowane do konkretnej firmy lub użytkownika.

Brute force jest skuteczny wtedy gdy aplikacja nie ogranicza prób logowania i pozwala na automatyczne testowanie wielu kombinacji.

# Brute Force nazw użytkowników (User Enumeration)

### Definicja

Nazwy użytkowników często są łatwe do odgadnięcia, ponieważ stosują przewidywaly schemat lub są publicznie ujawniane.

### Dlaczego to działa?

Atakujący nie musi zgadywać loginów, jeśli może je:

- odgadnąć na podstawie schematu (np. `imie.nazwisko@firma.com`),
- znaleźć na stronie,
- odczytać z odpowiedzi serwera.

Im mniej niewiadomych podczas logowania, tym skuteczniejszy jest np. atak brute force.

### Co sprawdzać?

- Czy profile użytkowników są publicznie dostępne?
- Czy nazwa profilu jest jednocześnie loginem?
- Czy aplikacja ujawnia adresy e-mail w odpowiedziach HTTP?
- Czy występują przewidywalne konta, np. `admin`, `administrator`, `root`, `support`, `it`?

# Brute Force hasła

Hasła mogą być podobnie brute-forcowane, z trudnościa bazującą na sile hasła.

Wiele stron ma zasady odnośnie hasła które zmuszają użytkowników do tworzenia mocniejszych, teoretycznie bardziej odpornych na złamanie haseł.


# Przewidywalne hasła

Uzytkownicy, często tworzą hasła które są łatwe do zapamiętania a jedynie spełniają wymagania polityki haseł.

# Dlaczego to działa?

Zamiast losowych znaków użytkownicy wybierają przewidywalne modyfikacje, np.:

- dodanie cyfry (`Password1`)
- dodanie znaku specjalnego (`Password1!`)
- zamiana liter na podobne znaki (`P4$$w0rd`)
- niewielkie zmiany po wymuszonej zmianie hasła (`Password1!` → `Password2!`)

Takie schematy sprawiają, że atakujący może znacząco ograniczyć liczbę prób.

# Co sprawdzam?

- Czy aplikacja wymusza zmianę hasła?
- Czy polityka haseł zachęca do przewidywalnych modyfikacji?
- Czy możliwe jest testowanie popularnych wariantów haseł podczas ataku brute force?

Nie atakujemy komputerów. Atakujemy decyzje ludzi.

Bardzo wiele podatności w web security wynika z tego, że użytkownicy, administratorzy lub programiści zachowują się w przewidywalny sposób.

# Username Enumeration

Technika pozwalająca ustalić, czy podana nazwa użytkownika istnieje, na podstawie różnic w zachowaniu aplikacji

# Dlaczego to działa?

Aplikacja zwraca różne odpowiedzi dla:

- istniejącego użytkownika
- nieistniejącego użytkownika

Dzięki temu atakujący może stworzyć listę poprawnych loginów przed rozpoczęciem ataku brute force.

Możemy wykorzystać również proces rejestracji użytkownika, jeśli wpiszemy jakiś username i dostaniemy komunikat, że dana nazwa już istnieje to mamy informacje którą chcieliśmy :) 

# Co sprawdzam?

- Czy komunikaty błędów różnią się dla niepoprawnego loginu i niepoprawnego hasła?
- Czy odpowiedzi mają różne kody HTTP?
- Czy różni się długość odpowiedzi?
- Czy zmienia się czas odpowiedzi (response time)?
- Czy formularz rejestracji informuje, że użytkownik już istnieje?

Username Enumeration ujawnia, które loginy są poprawne. Dzięki temu atakujący nie musi zgadywać nazwy użytkownika i może skupić się wyłącznie na odgadnięciu hasła.

Przy formularzu logowania, pierwsze pytanie brzmi:

> **Czy aplikacja zdradza, że ten użytkownik istnieje?**

Przykład:

```
admin / test123

→ Incorrect password
```

a dla:

```
nieistniejacy / test123

→ User not found
```

Komunikat ujawnia istnienie konta `admin`

1. Username Enumeration -> zdobywam poprawne loginy
2. Brute Force -> zgaduje hasło tylko dla tych loginów
3. Account Takeover -> przejmuję konto

Podczas testowania logowania należy porównywać odpowiedzi serwera dla różnych prób logowania i szukać różnic wskazujących, że podana nazwa użytkownika istnieje.

### 1. Status Code

Sprawdzam, czy serwer zwraca różne kody HTTP.

Przykład:

```
admin / zlehaslo
→ 200 OK

nieistniejacy / zlehaslo
→ 401 Unauthorized
```

Jeżeli odpowiedzi różnią się kodem HTTP, może to oznaczać, że aplikacja rozpoznaje poprawny login.

---

### 2. Error Message

Porównuję komunikaty błędów.

Przykład:

```
Invalid username
```

vs

```
Incorrect password
```

lub nawet:

```
Invalid username or password.
```

vs

```
Invalid username or password
```

Nawet niewielka różnica może ujawniać istnienie użytkownika.

---

### 3. Response Time

Sprawdzam czas odpowiedzi serwera.

Jeżeli dla jednego loginu odpowiedź trwa dłużej, może to oznaczać, że:

- użytkownik istnieje,
- aplikacja dodatkowo sprawdza hasło,
- wykonywane są kolejne operacje tylko dla poprawnych loginów.

---

# Dlaczego to działa?

Aplikacja wykonuje różne operacje dla:
- istniejącego użytkownika,
- nieistniejącego użytkownika

Te różnice często można zauważyć w odpowiedzi HTTP

Podczas wykrywania **Username Enumeration** porównuję trzy elementy odpowiedzi:

- **Status Code**
- **Error Message**
- **Response Time**

Przy każdym formularzu logowania zadaję sobie trzy pytania:

- Czy zmienia się **Status Code**?
- Czy zmienia się **treść odpowiedzi**?
- Czy zmienia się **czas odpowiedzi**?

Jeśli odpowiedź na którekolwiek z nich brzmi **tak**, mam trop, że aplikacja może ujawniać poprawne nazwy użytkowników.
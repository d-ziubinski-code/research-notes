## Podatności
- **Username Enumeration** - enumeracja nazw użytkowników poprzez czas odpowiedzi
- **IP Based Brute Force Protection Bypass** - obejscie ochrony brute force opartej na blokowaniu ip po zbyt dużej liczbie (5) niepoprawnych prób logowania
- **Password Brute-force** - Atak słownikowy na hasło 

W tym labie, celem jest enumeracja loginu bazując na czasię odpowiedzi serwera, obejście zabezpieczeń w postaci blokowania adresu IP oraz, po uzyskaniu najbardziej prawdopodobnego loginu - brute-force hasła.

## Enumeracja czasowa
Aplikacja poświęca więcej czasu na walidacje istniejącego użytkownika niż nieistniejącego.

- **Niepoprawny Username** - Serwer od razu odrzuca żadanie -> Krótki czas odpowiedzi (~ 50-150ms).
- **Poprawny Username** - Serwer przechodzi do weryfikacji hasła i wykonuje wolną funkcję mieszającą (np. bcrypt/pbkdf2) na podanym haśle -> Dłuższy czas odpowiedzi (300-500ms).

## Obejście blokady IP (X-Forwarded-For)
Serwer zlicza nieudane próby logowania per adres IP.

Modyfikując nagłówek HTTP przy każdym żądaniu:
```
X-Forwarded-For: 1.2.3.1 
X-Forwarded-For: 1.2.3.2
```

Aplikacja uznaje każde żądanie za pochodzące od zupełnie innego użytkownika


## Metodologia: Lab 3 

#### **Krok 1: Wykrycie poprawnego loginu (Username Enumeration)**

1. **Przechwycenie żądania:** Przechwyć żądanie `POST /login` w Burp Proxy i wyślij je do **Intrudera**.
    
2. **Ustawienie pozycji (Positions):**
    
    - Typ ataku: **Pitchfork**
        
    - Dodaj nagłówek spoofujący IP: `X-Forwarded-For: 1.2.3.§1§`
        
    - Ustaw ciało żądania: `username=§admin§&password=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` _(użyj stałego, bardzo długiego hasła bez klamer `§`)_
        
3. **Ustawienie payloadów (Payloads):**
    
    - **Payload Set 1 (IP):** Typ `Numbers` (od `1` do `101`, step `1`)
        
    - **Payload Set 2 (Username):** Wklej listę z _Candidate usernames_
        
4. **Konfiguracja wydajności (Resource pool):**
    
    - W zakładce **Resource pool** ustaw **`Maximum concurrent requests = 1`** _(1 wątek wymusza dokładny pomiar czasu odpowiedzi)_
        
5. **Analiza wyników:**
    
    - Uruchom atak i posortuj kolumnę **`Response received` / `Response time` malejąco**.
        
    - Login z wyraźnie najdłuższym czasem odpowiedzi to poprawny username (np. `americas`).
        

#### **Krok 2: Odgadnięcie hasła (Password Brute-Force)**

1. **Ustawienie pozycji (Positions):**
    
    - Typ ataku: **Pitchfork**
        
    - Wpisz znaleziony login na sztywno: `username=americas&password=§123456§`
        
    - Zachowaj nagłówek IP: `X-Forwarded-For: 1.2.3.§1§`
        
2. **Ustawienie payloadów (Payloads):**
    
    - **Payload Set 1 (IP):** Typ `Numbers` (od `1` do `101`, step `1`)
        
    - **Payload Set 2 (Password):** Wklej listę z _Candidate passwords_
        
3. **Analiza wyników:**
    
    - Posortuj wyniki po kolumnie **`Status`** lub **`Length`**.
        
    - Poprawne hasło zwróci kod **`302 Found`** (przekierowanie po pomyślnym zalogowaniu).
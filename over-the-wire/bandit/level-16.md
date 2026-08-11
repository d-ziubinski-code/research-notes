# Bandit Level 16

## Goal

Aby uzyskać hasło do poziomu 17, musimy przesłać hasło do obecnego poziomu na port znajdujący się w zakresie `31000`–`32000` na `localhost`.

Najpierw należy sprawdzić, na których portach działa serwer.

Następnie trzeba ustalić, które z tych usług obsługują SSL/TLS.

Tylko jeden serwer zwróci dane uwierzytelniające. Pozostałe serwery zwrócą przesłane przez nas dane.

**Host:** `bandit.labs.overthewire.org`

**Username:** `bandit16`

**Password:** hasło z Level 15

```
ssh bandit16@bandit.labs.overthewire.org -p 2220
```

---

# Solution

## 1. Skanowanie portów

Najpierw sprawdzamy, jakie porty w zakresie `31000-32000` są otwarte:

```
nmap -sV -p 31000-32000 localhost
```

Flaga `-p` określa zakres skanowanych portów, natomiast `-sV` próbuje rozpoznać usługę i jej wersję.

Wynik:

```
Starting Nmap 7.98 ( https://nmap.org ) at 2026-08-11 10:43 +0000
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00014s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo
```

Znaleźliśmy pięć otwartych portów:

```
31046  echo
31518  ssl/echo
31691  echo
31790  ssl/unknown
31960  echo
```

Interesują nas przede wszystkim porty `31518` i `31790`, ponieważ Nmap rozpoznał na nich usługę SSL.

---

## 2. Sprawdzenie usług TLS

Do ręcznego testowania usług TLS możemy użyć:

```
openssl s_client -connect localhost:PORT
```

Najpierw sprawdzamy:

```
openssl s_client -connect localhost:31691
```

Otrzymujemy m.in.:

```
no peer certificate available
Cipher is (NONE)
```

Oznacza to, że na tym porcie nie udało się zestawić poprawnego połączenia TLS. Jest to zwykła usługa `echo`, mimo że port znajduje się wśród wyników naszego skanowania.

Następnie sprawdzamy port `31790`:

```
openssl s_client -connect localhost:31790
```

Tym razem handshake TLS zostaje poprawnie wykonany:

```
Protocol  : TLSv1.3
Cipher    : TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
```

Serwer przedstawia również certyfikat:

```
subject=CN=SnakeOil
issuer=CN=SnakeOil
```

Certyfikat jest self-signed, dlatego OpenSSL zgłasza:

```
Verification error: self-signed certificate
Verify return code: 18 (self-signed certificate)
```

Nie oznacza to jednak, że TLS nie działa. Połączenie TLS zostało poprawnie zestawione.

---

## 3. Przesłanie hasła

Musimy teraz przesłać hasło z obecnego poziomu do właściwego serwera.

Możemy przekazać dane do `openssl` przez pipe:

```
echo 'HASŁO' | openssl s_client -connect localhost:31790 -quiet
```

Pipe `|` przekazuje standardowe wyjście (`stdout`) jednego programu jako standardowe wejście (`stdin`) drugiego.

Schemat:

```
echo HASŁO
     │
     │ stdout
     ▼
openssl s_client
     │
     │ TLS
     ▼
localhost:31790
```

`openssl s_client` zestawia połączenie TLS, a następnie przesyła otrzymane dane do serwera.

Flaga `-quiet` ogranicza dodatkowy output klienta TLS, dzięki czemu łatwiej zobaczyć odpowiedź usługi.

Po przesłaniu poprawnego hasła na port `31790` serwer zwraca klucz prywatny SSH potrzebny do uzyskania dostępu do następnego poziomu.

Klucz zapisujemy do pliku:

```
nano /tmp/bandit17.key
```

Następnie nadajemy mu odpowiednie uprawnienia:

```
chmod 600 /tmp/bandit17.key
```

I możemy użyć go do połączenia z kolejnym poziomem:

```
ssh -i /tmp/bandit17.key bandit17@bandit.labs.overthewire.org -p 2220
```

---
# Commands

```
nmap -sV -p 31000-32000 localhost

openssl s_client -connect localhost:31691

openssl s_client -connect localhost:31790

echo 'HASŁO' | openssl s_client -connect localhost:31790 -quiet

chmod 600 /tmp/bandit17.key

ssh -i /tmp/bandit17.key bandit17@bandit.labs.overt
```

# Lessons Learned

- `nmap -sV` pozwala nie tylko znaleźć otwarte porty, ale również spróbować rozpoznać działające na nich usługi.
- Nie należy bezkrytycznie ufać rozpoznaniu usługi przez Nmapa — warto ją ręcznie zweryfikować.
- TCP samo w sobie nie zapewnia szyfrowania.
- TLS może działać jako warstwa zabezpieczająca komunikację działającą nad TCP.
- `openssl s_client` może być używany jako klient do ręcznego testowania usług TLS.
- Certyfikat self-signed nie oznacza, że TLS nie działa — oznacza, że certyfikat nie jest zaufany przez lokalny system.
- Pipe `|` pozwala przekazywać dane pomiędzy programami.
- `stdin`, `stdout` i `stderr` są podstawowymi mechanizmami komunikacji programów w Unix/Linux.
- Możliwe jest automatyzowanie komunikacji z usługami sieciowymi za pomocą prostych poleceń powłoki.
- Przy enumeracji ważne jest nie tylko znalezienie otwartego portu, ale również określenie **co dokładnie działa na tym porcie i jak się z tym komunikować**.
## Related projects -
[Python nmap scanner](https://github.com/d-ziubinski-code/toolbox/tree/main/networking/scanner/nmap-scanner)
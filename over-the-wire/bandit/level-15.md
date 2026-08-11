# Bandit Level 15

## Goal


Aby uzyskać hasło do poziomu 16, musimy przesłać hasło do obecnego poziomu na port 30001 na `localhost`, korzystając z szyfrowania SSL/TLS

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit15
hasło: sprawdz level-14

ssh-i nazwa_pliku bandit15@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p

### Solution

OpenSSL - narzędzie implementujące protokoły kryptograficzne, między innymi SSL/TLS

Można go używać jako:
- klienta TLS
- generatora certyfikatów
- narzędzia do testowania połączeń szyfrowanych
W tym zadaniu używamy go jako klienta TLS.

Normalne TCP:

```
client
  |
  | plaintext
  |
server
```

Dane przesyłane są bez szyfrowania.

TLS:

```
client
  |
  | encrypted data
  |
server
```

W poprzednim poziomie używaliśmy:

`nc localhost 30000`

czyli zwykłego połączenia TCP.

Tym razem serwer wymaga szyfrowania SSL/TLS, dlatego używamy:

```
openssl s_client -connect localhost:30001
```

Po nawiązaniu połączenia wpisujemy hasło aktualnego użytkownika:

```
bandit14_password
```

Serwer zwraca hasło do następnego poziomu.

### Lessons learned

- TCP samo w sobie nie zapewnia szyfrowania
- TLS działa jako dodatkowa warstwa nad TCP
- OpenSSL może działać jako klient do testowania usług TLS
- Narzędzia typu nc i openssl służą do ręcznego testowania usług sieciowych


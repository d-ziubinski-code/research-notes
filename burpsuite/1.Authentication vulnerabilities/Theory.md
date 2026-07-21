
What is Authentication?
Co to uwierzytelnianie?

Uwierzytelnianie to proces weryfikacji tożsamości użytkowanika lub klienta

What is Authorization?
Co to autoryzacja?

Autoryzacja to proces polegający na sprawdzeniu czy użytkownik ma uprawnienia do wykonania określonej czynności


Skąd biorą się luki w zabezpieczeniach uwierzytelniania?

Większość luk w zabezpieczeniach uwierzytelniania występuje na jeden z dwóch sposobów:
- Mechanizmy uwierzytelniania są słabe, ponieważ nie zapewniają odpowiedniej ochrony przed atakami siłowymi
- Błędy logiczne lub wadliwe kodowanie w implementacji umozliwiają atakującemu całkowite ominięcie mechanizmów uwierzytelniania (zjawisko to nazywa się czasami "zepsutym uwierzytelnianiem")

Luki w zabezpieczeniach logowania opartego na haśle:

W przypadku kont związanych z unikalną nazwą użytkownika i sekretnym hasłem fakt znania hasła jest traktowany jako wystarczający do potwierdzenia tożsamości

To oznacza że bezpieczeństwo witryny będzie zagrożone, jeśli atakujący bedzię w stanie uzyskać lub odgadnąć dane logowania innego użytkownika.

Można to osiągnąc na kilka sposobów.

Ataki hasłowe Brute-Force - atak brute force polega na użyciu przez atakującego systemu prób i błędów w celu odgadnięcia prawidłowych danych logowania użytkowania.

Ataki sa zwykle zautomatyzowane przy uzyciu slownika słów.

Mozna dostrajać ataki brute-force aby uzyskac bardziej trafne odgadnięcia.

Strony internetowe, opierające się na logowaniu za pomocą hasła jako jedynej metody uwierzytelniania, mogą byc bardzo podatne na ataki, jesli nie wdroza odpowiedniej ochrony przed brute force.

Brute forcowac mozna takze nazwy uzytkownika.


Enumeracja nazw użytkownika

Enumeracja nazw użytkowników zazwyczaj ma miejsce na stronie logowania. Możemy to zrobic uzyskujac odpowiednie statusy od samej strony na przykład ze błędny login lub ze nazwa usera jest juz zajeta.

Podczas brute-forcowania strony, powinnismy zwraca uwage na: 
-kody statusow HTTP. Wiekszosc bedzie taka sama, ale jesli jakas proba zwraca inny kod to warto sie temu przyjrzeć.
-wiadomosci error - czasami zwracany komunikat rozni sie w zaleznosci od tego czy zarowno nazwa uzytkownika jak i haslo sa bledne czy tylko haslo.
-czasy reakcji: jesli wiekszosc ządan byla obslugiwana z podobnym czasem reakcji, kazde odchylenie sugeruje, że w tle dzialo sie cos innego. To kolejnysygnal zenazwa uzytkownika moze byc poprawna.

Roznica opoznienia moze byc subtelna, ale atakujacy moze to opoznienie bardziej uwidocznic, wprowadzajac bardzo dlugie haslo ktorego obsluga zajmie dluzszy czas.




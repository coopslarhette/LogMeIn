# LogMeIn
just for fun project that creates a simple log-in system

## project outline
* currently it operates out of the terminal. will probably remain a proof of concept (might try and work it into some kind of web shell). 
* uses sha512 hashing and unique, randomly generated salts to implement some kind of cryptographic security
  * hashing is much better than storing passwords in plain text for obvious reasons: if the database was compromised it makes it much, much harder for the attacker to deduce what each user's passwords is
  * salts are unique and random to protect against a rainbow table attack

#przechowywanie stanu konta
#doplacanie hajsu
#wyplacanie hajsu

class Bank:
    def __init__(self, stan_konta):
        self.stan_konta = stan_konta
        
    def plus(self, doplata):
        # self.stan_konta += doplata
        self.stan_konta = self.stan_konta + doplata

    def minus(self, wyplata):
        # self.stan_konta -= wyplata
        self.stan_konta = self.stan_konta - wyplata

hajs = Bank(stan_konta= 6000)
doplata = 2000
wyplata = 500

print('Stan konta wynosi ', hajs.stan_konta)

hajs.plus(doplata)
print('Stan konta wynosi ', hajs.stan_konta)

hajs.minus(wyplata)
print('Stan konta wynosi ', hajs.stan_konta)


import bank
# moje_konto = bank.Bank(stan_konta=100)

class TestBank:
    def test_stan_konta(self):
        hajs = bank.Bank(stan_konta=300)
        assert hajs.stan_konta == 300

    def test_doplata(self):
        hajs = bank.Bank(stan_konta=100)
        hajs.plus(300)
        assert hajs.stan_konta == 400

    def test_wyplata(self):
        hajs = bank.Bank(stan_konta=100)
        hajs.minus(30)
        assert hajs.stan_konta == 69.4

#TERMINAL 1: Pip3 install pytest
#TERMINAL 2: python3 -m pytest test_bank.py
#TERMINAL 3: python3 -m pytest test_bank.py -vvv
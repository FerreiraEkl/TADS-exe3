from config import *


class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    modelo = db.Column(db.String(254))
    ano = db.Column(db.Integer)

    def __str__(self):
        return str(self.id)+") " + self.nome + ", " +\
            self.modelo + ", " + self.ano

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "modelo": self.modelo,
            "ano": self.ano
        }


if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    nome = "Bmw"
    modelo = "X1"
    ano = 2020
    carro = Carro(nome=nome, modelo=modelo, ano=ano)
    db.session.add(carro)

    nome = "Mercedes Bens"
    modelo = "c180"
    ano = 2015
    carro = Carro(nome=nome, modelo=modelo, ano=ano)
    db.session.add(carro)

    nome = "VW Golf"
    modelo = "GTI"
    ano = 2015
    carro = Carro(nome=nome, modelo=modelo, ano=ano)
    db.session.add(carro),

    nome = "GM CAPTIVA"
    modelo = "SPORT 2.4"
    ano = 2015
    carro = Carro(nome=nome, modelo=modelo, ano=ano)
    db.session.add(carro)

    db.session.commit()

    for p in db.session.query(Carro).all():
        print(p)

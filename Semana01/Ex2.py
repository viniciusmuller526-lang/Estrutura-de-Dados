#Crux Sacra Sit Mihi Lux

class Contato:

    def __init__(self, nome, contato, email):

        self.nome = nome
        self.contato = contato
        self.email = email

marcia = Contato("Márcia", 5551999445911, "marcia@gmail.com")
pedro = Contato("Pedro", 5551999445912, "pedro@gmail.com")
alberto = Contato("Alberto", 5551999445913, "alberto@gmail.com")

agenda = []
agenda.extend([marcia, pedro, alberto])

for contatos in agenda:

    print("Nome: ", contatos.nome, "Contato: ", contatos.contato, "E-Mail: ", contatos.email)

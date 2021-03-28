from libpythonpro_exercicio.spam.enviador_email import Enviador
from libpythonpro_exercicio.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'gjsantana@gmail.com',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )

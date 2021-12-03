class Enviador:
    def enviar(self, rementente, destinatario, assunto, corpo):
        if '@' not in rementente:
            raise EmailInvalido(f'Email de remetente invalido{rementente}')
        return rementente


class EmailInvalido(Exception):
    pass
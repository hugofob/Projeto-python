
class Chat:
    '''
    Estrutura básica de pesquisa do gpt
    '''
    def perguntar(self, pergunta):
        pergunta = pergunta.lower()#transforma em letras minúsculas

        if 'python' in pergunta:
            return 'Python e uma linguagem de programação, muito utilizada.'
        elif 'olá' in pergunta or 'oi' in pergunta:
            return 'Olá! como posso te ajudar?'
        elif 'quem e você' in pergunta:
            return 'Sou assistente virtual.'
        else:
            return 'Não sei responder está pergunta.'

meu_chat = Chat()#criando objeto da classe

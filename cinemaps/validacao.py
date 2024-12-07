import re

# Entre 4 e 16 caracteres, não pode iniciar nem terminar com número ou underline
USUARIO_REGEX = "^[A-Za-z][A-Za-z0-9_]{3,16}$"

# Mínimo de oito caracteres, ao menos uma letra, um número e um caractere especial
SENHA_REGEX = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

EMAIL_REGEX = "^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"


def nome_usuario_valido(usuario: str) -> bool:
    """Valida um nome de usuário com base nos critérios de:
        - Possui entre 4 e 16 caracteres
        - Não inicia nem termina com número ou underline

    Args:
        usuario (str): A string do nome de usuário

    Returns:
        bool: Verdadeiro se atende aos critérios, falso do contrário
    """
    
    return re.match(USUARIO_REGEX, usuario)


def senha_valida(senha: str, senha_confirmar: str) -> bool:
    """Valida uma senha com base nos seguintes critérios:
        - Possui mais de 8 caracteres
        - Possui ao menos uma letra
        - Possui ao menos um número
        - Possui ao menos um caractere especial

    Args:
        senha (str): A senha a ser validada
        senha_confirmar (str): A confirmação da senha feita pelo usuário

    Returns:
        bool: Verdadeiro se atende aos critérios, falso do contrário
    """
    
    return senhas_iguais(senha, senha_confirmar) and re.match(SENHA_REGEX, senha)


def senhas_iguais(senha: str, senha_confirmar: str) -> bool:
    return senha == senha_confirmar


def validar_email(email: str) -> bool:
    """Valida umm email, é redundante mas evita o usuário que tente burlar o sistema alterando o tipo do input.

    Args:
        email (str): A string do email

    Returns:
        bool: Verdadeiro se é um email válido, falso do contrário
    """
    
    return re.match(EMAIL_REGEX, email)
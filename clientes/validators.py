import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Valida se o celular é valido (11 91234-1234)"""
    modelo = '[0-9]{2} 9[0-9]{4}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta

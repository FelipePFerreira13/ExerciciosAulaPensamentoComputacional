import re
class Validar:
    
    def Validar_cpf(cpf):
        # Remove caracteres não numéricos
        cpf = re.sub(r'[^0-9]', '', cpf)
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False
        # Verifica se não são todos dígitos iguais
        if cpf == cpf[0] * 11:
            return False
        # Formato para exibição: 123.456.789-00
        padrao_formatado = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_formatado):        
            return True
    
    def Validar_placa(placa):
        if len(placa) == 7 and (re.match("[A-Z][A-Z][A-Z][0-9][A-Z][0-9][0-9]", placa) or re.match("[A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9]", placa)):
            return True
        else:
            return False
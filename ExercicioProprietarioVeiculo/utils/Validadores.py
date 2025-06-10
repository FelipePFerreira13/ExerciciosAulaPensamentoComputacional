import re
class Validar:
    
    def Validar_cpf(cpf):

        cpf = re.sub(r'[^0-9]','',cpf)
        calc = 0

        i = 0

        if (cpf[0]*len(cpf))==cpf:
            return False

        for n in reversed(range(2, 11)):

            calc += int(cpf[i]) * n

            i+=1


        digito1 = calc * 10 % 11 if calc * 10 % 11 < 10 else 0
        
        if digito1 == int(cpf[9]):

            i = 0

            calc = 0

            for n in reversed(range(2, 12)):

                calc += int(cpf[i]) * n

                i+=1

            digito2 = calc * 10 % 11 if calc * 10 % 11 < 10 else 0

            if digito2 == int(cpf[10]):
                return True


        return False
    
    def Validar_placa(placa):
        if len(placa) == 7 and (re.match("[A-Z][A-Z][A-Z][0-9][A-Z][0-9][0-9]", placa) or re.match("[A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9]", placa)):
            return True
        else:
            return False
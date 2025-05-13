def testeVeiculo():
    
    from models.Veiculos import Veiculos

    hb20 = Veiculos('Hyundai', 'HB20', 2019, 'aaa1a11', 'Branco')

    hb20.ver_velocidade()

    hb20.acelerar(10 , 8)

    hb20.ver_velocidade()

    hb20.frear(5, 2)

    hb20.ver_velocidade()

    hb20.placa = "bbb2b22"

    hb20.ver_velocidade()

    msg = f"O carro {hb20.modelo}, placa {hb20.placa}, ano {hb20.ano}, marca {hb20.marca} está andando "
    msg += f"a {hb20.velocidade}km/h, com latitude de {hb20.latitude} e longitude de {hb20.longitude}"

    print(msg)
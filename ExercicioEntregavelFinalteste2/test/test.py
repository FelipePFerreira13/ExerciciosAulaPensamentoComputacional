# Exemplo de uso dos modelos e relacionamento entre Prédio e Apartamento

from database.database_tools import session
from database.database import Predio, Apartamento

# Cria um novo prédio e adiciona ao banco
novo_predio = Predio(
    rua="Rua do Inter",
    numero="1010",
    bairro="Centro",
    cidade="Floripa",
    estado="SC"
)
session.add(novo_predio)
session.commit()

# Cria um novo apartamento vinculado ao prédio recém-criado
novo_ap = Apartamento(
    id_predio=novo_predio.id,
    numero_apartamento="100",
    valor=200000.00
)
session.add(novo_ap)
session.commit()
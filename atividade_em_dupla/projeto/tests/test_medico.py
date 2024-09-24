import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def pessoa_valida():
    medico = Medico("1111", "Vitoriano", "71988514932", "vitoriano@gmail.com", "12574896802", "14852974", 
                    "8479", Setores.SAUDE, "10000", 
                    Endereco("Avenida C", "22", "Em frente ao joia", "21234", "Salvador", UF.BAHIA), 
                    "17/03/1997", Generos.FEMININO, EstadoCivil.SEPARADO, "7444")
    return medico

def test_medico_id_valido(pessoa_valida):
     assert pessoa_valida.id == "1111"

def test_medico_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Vitoriano"
import pytest
from projeto.models import engenheiro
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def pessoa_valida():
    engenheiro = Engenheiro("321312", "Breno", "7199932921", "Breno@gmail.com", "3123231", "12312313", 
                    "832233", Setores.ENGENHARIA, "424224", 
                    Endereco("Rua pedro alvares", "22", "igreja", "21223123", "Salvador", UF.BAHIA), 
                    "20/08/200", Generos.MASCULINO, EstadoCivil.SEPARADO, "3123123")
    return engenheiro

def test_engenheiro_id_valido(pessoa_valida):
     assert pessoa_valida.id == "321312"

def test_engenheiro_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Breno"
import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estadoCivil import EstadoCivil
from projeto.models.enums.generos import Generos
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF

@pytest.fixture
def pessoa_valida():
    advogado = Advogado("1111", "Moura", "71988514981", "guilherme@gmail.com", "12345678", "12345678", 
                    "1929", Setores.JURIDICO, "10000", 
                    Endereco("Rua anisio", "12", "igreja de sao jorge", "40430510", "Salvador", UF.BAHIA), 
                    "03/03/2006", Generos.FEMININO, EstadoCivil.SEPARADO, "4444")
    return advogado

def test_advogado_id_valido(pessoa_valida):
     assert pessoa_valida.id == "1111"

def test_advogado_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Moura"
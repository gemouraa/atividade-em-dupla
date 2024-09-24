import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.cliente import Cliente
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    cliente = Cliente("3323", "Arthur", "719879392", "arthur@gmail.com", 
                      Endereco("amaralina", "99", "Frente a bom preco", "434124", "Salvador", UF.BAHIA), "30/03/2000", 
                      Generos.MASCULINO, EstadoCivil.DIVORCIADO, "12223413234")
    return cliente

def test_cliente_id_valido(pessoa_valida):
     assert pessoa_valida.id == "3323"

def test_cliente_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Arthur"

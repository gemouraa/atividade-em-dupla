import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.pessoaFisica import PessoaFisica 
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    pessoaFisica = PessoaFisica("333", "Mateus", "7198854726", "Mateus@gmail.com", 
                                Endereco("Rua F", "11", "Em frente a Fazenda", "74858-100", "Salvador", UF.BAHIA), "19/12/2000", 
                                Generos.MASCULINO, EstadoCivil.CASADO)
    return pessoaFisica

def test_pessoaJuridica_id_valido(pessoa_valida):
     assert pessoa_valida.id == "333"

def test_pessoaJuridica_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Mateus"

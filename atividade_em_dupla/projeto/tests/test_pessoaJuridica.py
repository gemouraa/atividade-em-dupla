import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.fornecedor import Produto
from projeto.models.pessoaJuridica import PessoaJuridica
from projeto.models.prestacaoServico import PrestacaoServico

@pytest.fixture
def pessoa_valida():
    pessoaJuridica = PessoaJuridica("555", "Marta", "7188445967", "marta@gmail.com", 
                                    Endereco("Avenida 9", "79", "Ao lado da farmacia", "453233", "Salvador", UF.BAHIA), 
                                    "748532", "Tudo", 
                                    PrestacaoServico("14-03-2001", "15-10-2007"), Produto("Sim"))
    return pessoaJuridica

def test_pessoaJuridica_id_valido(pessoa_valida):
     assert pessoa_valida.id == "555"

def test_pessoaJuridica_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Marta"

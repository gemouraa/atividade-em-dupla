from abc import abstractmethod
import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.setores import Setores
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.funcionario import Funcionario
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    funcionario = Funcionario("2222", "Joao", "71988514981", "joao@gmail.com", "323221", "324414", "5676", 
                              Setores.ENGENHARIA, "4555", Endereco("Rua B", "77", "do lado do bar", 
                                                                    "3231", "Salvador", UF.BAHIA), "12/11/2002", 
                                                                    Generos.MASCULINO, EstadoCivil.VIUVO)
    return funcionario

def test_funcionario_id_valido(pessoa_valida):
     assert pessoa_valida.id == "2222"

def test_funcionario_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Joao"
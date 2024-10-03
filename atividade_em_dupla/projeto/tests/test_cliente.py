import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadeFederativa import UF
from projeto.models.cliente import Cliente
from projeto.models.enums.generos import Generos
from projeto.models.enums.estadoCivil import EstadoCivil

@pytest.fixture
def pessoa_valida():
    cliente = Cliente(3323, "Arthur", "719879392", "arthur@gmail.com", 
                      Endereco("amaralina", "99", "Frente a bom preço", "434124", "Salvador", UF.BAHIA), "30/03/2000", 
                      Generos.MASCULINO, EstadoCivil.SOLTEIRO, "12223413234")
    return cliente

def test_cliente_id_valido(pessoa_valida):
     assert pessoa_valida.id == 3323

def test_cliente_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Arthur"
def test_validar_telefone_cliente(pessoa_valida):
    assert pessoa_valida.telefone == "719879392"

def test_validar_email_cliente(pessoa_valida):
    assert pessoa_valida.email == "arthur@gmail.com"

def test_validar_genero_cliente(pessoa_valida):
    assert pessoa_valida.genero == Generos.MASCULINO

def test_validar_estado_civil_cliente(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.SOLTEIRO

def test_validar_data_nascimento_cliente(pessoa_valida):
    assert pessoa_valida.dataNascimento == "30/03/2000"

def test_validar_protocolo_atendimento_cliente(pessoa_valida):
    assert pessoa_valida.protocoloAtendimento == "12223413234"

def test_validar_endereco_logradouro_cliente(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "amaralina"

def test_validar_endereco_numero_cliente(pessoa_valida):
    assert pessoa_valida.endereco.numero == "99"

def test_validar_endereco_complemento_cliente(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Frente a bom preço"

def test_validar_endereco_cep_cliente(pessoa_valida):
    assert pessoa_valida.endereco.cep == "434124"

def test_validar_endereco_cidade_cliente(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_validar_endereco_uf_cliente(pessoa_valida):
    assert pessoa_valida.endereco.uf == UF.BAHIA    




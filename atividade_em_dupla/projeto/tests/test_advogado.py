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
                    "03/03/2006", Generos.MASCULINO,EstadoCivil.SEPARADO, "4444")
    return advogado

def test_advogado_id_valido(pessoa_valida):
     assert pessoa_valida.id == "1111"

def test_advogado_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Moura"

def test_validar_telefone_advogado(pessoa_valida):
    assert pessoa_valida.telefone == "71988514981"

def test_validar_email_advogado(pessoa_valida):
    assert pessoa_valida.email == "guilherme@gmail.com"

def test_validar_genero_advogado(pessoa_valida):
    assert pessoa_valida.genero == Generos.MASCULINO

def test_validar_estado_civil_advogado(pessoa_valida):
    assert pessoa_valida.estadoCivil == EstadoCivil.SEPARADO

def test_validar_data_nascimento_advogado(pessoa_valida):
    assert pessoa_valida.dataNascimento == "03/03/2006"

def test_validar_cpf_advogado(pessoa_valida):
    assert pessoa_valida.CPF == "12345678"

def test_validar_rg_advogado(pessoa_valida):
    assert pessoa_valida.RG == "12345678"

def test_validar_matricula_advogado(pessoa_valida):
    assert pessoa_valida.matricula == "1929"

def test_validar_setor_advogado(pessoa_valida):
    assert pessoa_valida.setor == Setores.JURIDICO

def test_validar_salario_advogado(pessoa_valida):
    assert pessoa_valida.salario == "10000"

def test_validar_crea_advogado(pessoa_valida):
    assert pessoa_valida.OAB == "4444"

def test_validar_endereco_logradouro_advogado(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Rua anisio"

def test_validar_endereco_numero_advogado(pessoa_valida):
    assert pessoa_valida.endereco.numero == "12"

def test_validar_endereco_complemento_advogado(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "igreja de sao jorge"

def test_validar_endereco_cep_advogado(pessoa_valida):
    assert pessoa_valida.endereco.cep == "40430510"

def test_validar_endereco_cidade_advogado(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_validar_endereco_uf_advogado(pessoa_valida):
    assert pessoa_valida.endereco.uf == UF.BAHIA


        
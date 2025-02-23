import unittest
import datetime
from my_twitter import Tweet, Perfil, PessoaFisica, PessoaJuridica, RepositoriosUsuarios, MyTwitter
from excecoes import UJCException, UNCException, PPException, PDException, PIException, MFPException, SIException


class TestRepositoriosUsuarios(unittest.TestCase):
    def test_cadastrar_usuario(self):
        repo = RepositoriosUsuarios()
        perfil = Perfil("usuario1")
        repo.cadastrar(perfil)
        self.assertEqual(repo.buscar("usuario1"), perfil)
    
    def test_cadastrar_usuario_existente(self):
        repo = RepositoriosUsuarios()
        perfil = Perfil("usuario1")
        repo.cadastrar(perfil)
        with self.assertRaises(UJCException):
            repo.cadastrar(perfil)
    
    def test_atualizar_usuario(self):
        repo = RepositoriosUsuarios()
        perfil = Perfil("usuario1")
        repo.cadastrar(perfil)
        novo_perfil = Perfil("usuario1")
        repo.atualizar(novo_perfil)
        self.assertEqual(repo.buscar("usuario1"), novo_perfil)

    
if __name__ == "__main__":
    unittest.main()

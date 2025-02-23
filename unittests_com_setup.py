import unittest
import datetime
from my_twitter import Tweet, Perfil, PessoaFisica, PessoaJuridica, RepositoriosUsuarios, MyTwitter
from excecoes import UJCException, UNCException, PPException, PDException, PIException, MFPException, SIException



class TestRepositoriosUsuarios(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoriosUsuarios()
        self.perfil = Perfil("usuario1")
    
    def tearDown(self):
        del self.repo
        del self.perfil
    
    def test_cadastrar_usuario(self):
        self.repo.cadastrar(self.perfil)
        self.assertEqual(self.repo.buscar("usuario1"), self.perfil)
    
    def test_cadastrar_usuario_existente(self):
        self.repo.cadastrar(self.perfil)
        with self.assertRaises(UJCException):
            self.repo.cadastrar(self.perfil)
    
    def test_atualizar_usuario(self):
        self.repo.cadastrar(self.perfil)
        novo_perfil = Perfil("usuario1")
        self.repo.atualizar(novo_perfil)
        self.assertEqual(self.repo.buscar("usuario1"), novo_perfil)

   
if __name__ == "__main__":
    unittest.main()

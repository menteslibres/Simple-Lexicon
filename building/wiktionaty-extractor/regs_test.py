# -*- coding: UTF-8 -*-
import regs as regs
import unittest


class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(regs.find_title(u"<title>aléman</title>"),u"aléman")

    def test2(self) :
	self.assertEqual(regs.find_word_specs(r"=== {{verbo|fr}} ===  algun contenido === {{sustantivo|es}} ==="),[("verbo","fr"),("sustantivo","es")])
	
    def test3(self) :
	self.assertEqual(regs.clear_words(u":*'''Ejemplos:''' como [[ palabra ]] aquí [http link]"),u"Ejemplos: como palabra aquí ")

    def test4(self) :
	self.assertEqual(regs.clear_words("::''Correr'' tras un ascenso. &lt;small&gt;"),"''Correr'' tras un ascenso. ")

    def test5(self) :
	self.assertEqual(regs.clear_words(" ;1: ;2:")," 1 2")
	
    def test6(self) :
	self.assertEqual(regs.clear_words(r" ;1 {{Tema}}:")," 1 Tema")	
	
    #def test7(self) :
	#self.assertEqual(regs.remove_clear(r" {{clear }}\n"),r" \n")	
	
    def test8(self) :
	self.assertItemsEqual(regs.get_contents(ur" Precontenido === {{verbo|fr}} === primer_contenido === {{sustantivo|es}} ===segundo contenido===FIN==="),[ur" primer_contenido ",ur"segundo contenido"])	
	
    def test9(self) :
	self.assertEqual(regs.get_contents(ur" Precontenido === forma verbal ===  \n  contenído {{entre}} [[categorias]] 2311   === FIN ==="),[ur"  \n  contenído {{entre}} [[categorias]] 2311   "])


if __name__ == '__main__':
    unittest.main()

      
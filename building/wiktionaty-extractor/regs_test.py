# -*- coding: UTF-8 -*-
import regs as regs
import unittest


class TestExtract(unittest.TestCase) :
    
    def test1(self) :
	self.assertEqual(regs.find_title(u"<title>aléman</title>"),u"aléman")

    def test2(self) :
	self.assertEqual(regs.find_word_specs(r"== {{verbo|fr}} =="),["verbo","fr"])
	
    def test3(self) :
	self.assertEqual(regs.word_replace2(u" como [[ link ]] aquí "),u" como link aquí ")

    def test4(self) :
	self.assertEqual(regs.word_replace1(" {{plm|alga}} marina")," alga marina")

    def test5(self) :
	self.assertEqual(regs.number_replace(" ;1: ;2:")," 1 2")
	
    def test6(self) :
	self.assertEqual(regs.remove_clear(r" {{clear }}\n"),r" \n")	
	


if __name__ == '__main__':
    unittest.main()

      
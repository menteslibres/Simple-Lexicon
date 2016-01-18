# -*- coding: UTF-8 -*-
import re
import spanish.lang as lang

class Format :
    def __init__(self) :
	self.double_spaces_re = re.compile(ur'([ \n]{2,})',re.UNICODE)
        self.start_re = re.compile(ur'^[\w]+',re.UNICODE)
        self.end_re = re.compile(ur'$[\s]+',re.UNICODE)


    def clean(self,data) :
	#new_data = data
	new_data = self.double_spaces_re.sub('\0',data)
	#new_data = self.start_re.sub('',new_data)
	#new_data = self.end_re.sub('',new_data)
	return new_data
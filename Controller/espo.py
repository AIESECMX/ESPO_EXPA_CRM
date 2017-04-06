import json 
import requests
import sys
sys.append('..')


class ESPO(object):
	"""docstring for ESPO"""
	def __init__(self, arg):
		super(ESPO, self).__init__()
		self.arg = arg
		


	#this mehotd gets mcs form expa using the sepcified EXPA ID
	def set_MCs(self, mc_id):


	#this mehotd gets LCs form expa using the sepcified EXPA ID
	def get_lc(self,lc_id):

	#this mehotd gets People form expa using the sepcified EXPA ID
	def get_person(self,person_id):

	#this mehotd gets Opportunities form expa using the sepcified EXPA ID
	def get_opportunity(self,person_id):

	#this mehotd gets applications form expa using the sepcified EXPA ID
	def get_application(self,application_id):

	def get_enabler(self,enabler_id):
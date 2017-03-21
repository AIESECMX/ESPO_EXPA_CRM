#this Script is a cntrol script for the operations will be executing with expa
import gis_token_generator
import requests


class EXPA(object):

	def __init__(self,user_mail,user_pass):
		self.url = 
		token_genrator = GIS()
		self.expa_token =  token_genrator.generate_token(user_mail, user_pass)
		self.yop_token =  token_genrator.generate_op_token(user_mail, user_pass)



	#this mehotd gets mcs form expa using the sepcified EXPA ID
	def get_MCs(self, mc_id):


	#this mehotd gets LCs form expa using the sepcified EXPA ID
	def get_lc(self,lc_id):

	#this mehotd gets People form expa using the sepcified EXPA ID
	def get_person(self,person_id):

	#this mehotd gets Opportunities form expa using the sepcified EXPA ID
	def get_opportunity(self,person_id):

	#this mehotd gets applications form expa using the sepcified EXPA ID
	def get_application(self,application_id):

	def get_enabler(self,enabler_id):

#this Script is a cntrol script for the operations will be executing with expa
import json
from gis_token_generator import GIS
import requests
import sys
sys.path.append('..')

class EXPA(object):

#for this file we will create 3 kind of methods for all the entities managed by this class (MC, LC, Opp, EP, App, Enabler)
#generated methods 
#get list of
#get single by id
#get with a set of paramaters that will retorn a json
#
	def __init__(self,user_mail,user_pass):
		self.url = 'https://gis-api.aiesec.org/v2/'
		token_genrator = GIS()
		self.expa_token =  token_genrator.generate_token(user_mail, user_pass)
		#self.yop_token =  token_genrator.generate_op_token(user_mail, user_pass)

	def get_MCs(self, paramaters = None):
		return None

	#this mehotd gets mcs form expa using the sepcified EXPA ID
	def get_MC(self, mc_id):
		return None


	def get_LCs(self,paramaters = None):
		headers = {'access_token': self.expa_token,
		'filters[parent][]':[1589]}
		r = requests.get(self.url+'committees',data = headers)
		print r.text
		return r.text

	#this mehotd gets LCs form expa using the sepcified EXPA ID
	def get_LC(self,lc_id):
		return None

	#this mehotd gets People form expa using the sepcified EXPA ID
	def get_Person(self,person_id):
		return None

	def get_People(self, paramaters = None):
		return None

	#this mehotd gets Opportunities form expa using the sepcified EXPA ID
	def get_Opp(self,opp_id):
		return None

	def get_Opps(self,paramaters = None):
		return None

	#this mehotd gets applications form expa using the sepcified EXPA ID
	def get_Application(self,application_id):
		return None

	def get_Applications(slef,paramaters = None):
		return None

	def get_Enabler(self,enabler_id):
		return None

	def get_Enablers(self, paramaters = None):
		return None

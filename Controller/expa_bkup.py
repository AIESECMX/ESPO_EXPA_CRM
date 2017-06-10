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
		if(paramaters != None):
			params = paramaters
			params['access_token']=self.expa_token 
		else:
			params = {'filters[parent]':[1589],
			'access_token':self.expa_token}
		response = requests.get(self.url+'committees', data=params)
		return json.loads(response.text)['data']

	#this mehotd gets mcs form expa using the sepcified EXPA ID
	def get_MC(self, mc_id = 1589):
		params = {'access_token':self.expa_token}
		response = requests.get(self.url+'committees/' + str(mc_id) + '.json', data=params)
		return json.loads(response.text)


	def get_LCs(self,paramaters = None):
		if(paramaters != None):
			headers = paramaters
<<<<<<< HEAD
			headers['access_token'] = self.expa_token
=======
			headers['access_token']=self.expa_token 
>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b
		else:
			headers = {'access_token': self.expa_token}
			headers['filters[parent]'] = [1589]
		r = requests.get(self.url+'committees', data = headers)
		return json.loads(r.text)['data']

	#this mehotd gets LCs form expa using the sepcified EXPA ID
	def get_LC(self, lc_id = 1014):
		params = {'access_token':self.expa_token}
		response = requests.get(self.url+'committees/' + str(lc_id) + '.json', data=params)
		return json.loads(response.text)

	#this mehotd gets People form expa using the sepcified EXPA ID
	def get_Person(self,person_id):
		params = {'person_id':person_id,
		'access_token':self.expa_token}
		response = requests.get(self.url+'people/' + str(person_id) + '.json', data=params)
		return json.loads(response.text)

	def get_People(self, paramaters = None):
		if(paramaters != None):
			params = paramaters
<<<<<<< HEAD
			params['access_token'] = self.expa_token
=======
			params['access_token']=self.expa_token 
>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b
		else:
			params = {'filters[mcs]':[1589,577],
			'access_token':self.expa_token}
		response = requests.get(self.url+'people', data=params)
		return json.loads(response.text)['data']

	#this mehotd gets Opportunities form expa using the sepcified EXPA ID
	def get_Opp(self,opp_id):
		params = {'access_token':self.expa_token}
		response = requests.get(self.url+'opportunities/' + str(opp_id) + '.json', data=params)
		return json.loads(response.text)

	def get_Opps(self,paramaters = None):
		if(paramaters != None):
			params = paramaters
<<<<<<< HEAD
			params['access_token'] = self.expa_token
=======
			params['access_token']=self.expa_token 
>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b
		else:
			params = {'access_token':self.expa_token}
			params['filters[committee]'] = 1014
		response = requests.get(self.url+'opportunities', data=params)
		return json.loads(response.text)['data']

	#this mehotd gets applications form expa using the sepcified EXPA ID
	def get_Application(self,application_id):
		params = {'access_token':self.expa_token}
		response = requests.get(self.url+'applications/' + str(application_id) + '.json', data=params)
		return json.loads(response.text)

	def get_Applications(self,paramaters = None):
		if(paramaters != None):
			params = paramaters
<<<<<<< HEAD
			params['access_token'] = self.expa_token
=======
			params['access_token']=self.expa_token
>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b
		else:
			params = {'filters[opportunity_home_mc]':[1589],
			'access_token':self.expa_token}
		response = requests.get(self.url+'applications', data=params)
		return json.loads(response.text)['data']

	def get_Enabler(self,enabler_id):
		params = {'access_token':self.expa_token}
		response = requests.get(self.url+'organisations/' + str(enabler_id) + '.json', data=params)
		return json.loads(response.text)

	def get_Enablers(self, paramaters = None):
		if(paramaters != None):
			params = paramaters
<<<<<<< HEAD
			params['access_token'] = self.expa_token
=======
			params['access_token']=self.expa_token 
>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b
		else:
			params = {'filters[committee]':[1589],
			'access_token':self.expa_token}
		response = requests.get(self.url+'organisations', data=params)
<<<<<<< HEAD
		return json.loads(response.text)
=======
		return json.loads(response.text)['data']
>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b

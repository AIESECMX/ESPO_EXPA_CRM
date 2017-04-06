import json 
import requests
import sys
import base64
sys.path.append('..')


#
#For this class we define mehtods to pushinformation into ESPO
#we need to define methods to:
#update each entry by ID
#create by id
#get entity by id
#get list of entity by parameters
#

class ESPO(object):
	"""docstring for ESPO"""
	def __init__(self, user, passwd ,test = False):
		super(ESPO, self).__init__()
		header = {
		'Espo-Authorization': base64.b64encode(user+':'+passwd)
		}
		self.test = test
		if (self.test):
			self.url = 'http://104.197.179.91/espocrm/api/v1/'
		else:
			self.url = 'http://107.178.211.253/espocrm/api/v1/'
		t = requests.get(self.url+'App/user',headers= header)
		self.token =  json.loads(t.text)['user']['token']
				

	#setting the stest mode
	def set_test(self,test = True):
		self.test = test
		if (self.test):
			self.url = 'http://104.197.179.91/espocrm/api/v1/'
		else:
			self.url = 'http://107.178.211.253/espocrm/api/v1/'
		t = requests.get(self.url+'App/user',headers= header)
		self.token =  json.loads(t.text)['user']['token']

	#this mehotd gets mcs form espo using the sepcified espo ID
	def get_MC(self, mc_id):
		return None

	#gets a list of MCs with the specified espo parameters 
	def get_MCs(self, params):
		return None

	#this mehotd gets mcs form espo using the sepcified espo ID
	def create_MC(self, mc_id):
		return None

	#updates an MC that already exists in podio
	def update_MC(self,mc):
		return None




	#this mehotd gets applications form espo using the sepcified espo ID
	def get_application(self, application_id):
		return None

	#gets a list of applications with the specified espo parameters 
	def get_applications(self, params):
		return None

	#this mehotd gets applications form espo using the sepcified espo ID
	def create_application(self, application_id):
		return None

	#updates an application that already exists in podio
	def update_application(self,application):
		return None




	#this mehotd gets enablers form espo using the sepcified espo ID
	def get_enabler(self, enabler_id):
		return None

	#gets a list of enablers with the specified espo parameters 
	def get_enablers(self, params):
		return None

	#this mehotd gets enablers form espo using the sepcified espo ID
	def create_enabler(self, enabler_id):
		return None

	#updates an enabler that already exists in podio
	def update_enabler(self,enabler):
		return None



	#this mehotd gets lcs form espo using the sepcified espo ID
	def get_lc(self, lc_id):
		return None

	#gets a list of lcs with the specified espo parameters 
	def get_lcs(self, params):
		return None

	#this mehotd gets lcs form espo using the sepcified espo ID
	def create_lc(self, lc_id):
		return None

	#updates an lc that already exists in podio
	def update_lc(self,lc):
		return None



	#this mehotd gets opportunities form espo using the sepcified espo ID
	def get_opportunity(self, opportunity_id):
		return None

	#gets a list of opportunities with the specified espo parameters 
	def get_opportunities(self, params):
		return None

	#this mehotd gets opportunitys form espo using the sepcified espo ID
	def create_opportunity(self, opportunity_id):
		return None

	#updates an opportunity that already exists in podio
	def update_opportunity(self,opportunity):
		return None




	#this mehotd gets persons form espo using the sepcified espo ID
	def get_person(self, person_id):
		return None

	#gets a list of persons with the specified espo parameters 
	def get_persons(self, params):
		return None

	#this mehotd gets persons form espo using the sepcified espo ID
	def create_person(self, person_id):
		return None

	#updates an person that already exists in podio
	def update_person(self,person):
		return None

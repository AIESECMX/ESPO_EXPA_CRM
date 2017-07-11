import json 
import requests
import sys
import base64
sys.path.append('..')
from  Model.mc import MC

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
		self.base64 = base64.b64encode(user+':'+passwd)
		header = {
		'Espo-Authorization': self.base64
		}
		self.test = test
		if (self.test):
			self.url = 'http://104.197.10.177/espocrm/api/v1/'
		else:
			self.url = 'http://107.178.211.253/espocrm/api/v1/'
		t = requests.get(self.url,headers= header)
		print t
		print t.text
		sys.exit(0)
		self.token = json.loads(t.text)['user']['token']	
		self.headers = {
		'Authorization': 'Basic '+self.base64,
		'Espo-Authorization': base64.b64encode(user+':'+self.token)
		}

	#if the token is not valid anyomore get a new one
	def new_token():
		header = {
		'Espo-Authorization': self.base64
		}
		self.test = test
		if (self.test):
			self.url = 'http://104.197.10.177/espocrm/api/v1/'
		else:
			self.url = 'http://107.178.211.253/espocrm/api/v1/'
		t = requests.get(self.url+'App/user',headers= header)
		self.token = json.loads(t.text)['user']['token']	
		self.headers = {
		'Espo-Authorization': base64.b64encode(user+':'+self.token)
		}


 	#######################
 	#####  MC Starts ######
 	#######################
	#this mehotd gets mcs form espo using the sepcified espo ID
	def get_MC(self, mc_id):
		r = requests.get(self.url+'MC/'+str(mc_id),headers= self.headers)
		print r.text == ''
		if r.text != '':
			mc_espo = json.loads(r.text)
			return  MC(mc_espo['name'], mc_espo['expaId'], mc_espo['id']) 
		else:
			return None

	#this mehotd gets mcs form espo using the sepcified expa ID
	def get_expa_MC(self, mc_id):
		if self.test:
			params = {
				'where[0][type]':'equals',
				'where[0][attribute]':'expaId',
				'where[0][value]':mc_id
				}
		else:
			params = {
				'where[0][type]':'equals',
				'where[0][attribute]':'expaId',
				'where[0][value]':mc_id
				}
		r = requests.get(self.url+'MC',headers= self.headers,params=params)
		if r.text != '{"total":0,"list":[]}':
			mc_espo = json.loads(r.text)['list'][0]
			print r.text
			return  MC(mc_espo['name'], mc_espo['expaId'], mc_espo['id']) 
		else:
			return None
		
		

	#gets a list of MCs with the specified espo parameters 
	def get_MCs(self, params = None):
		if params is None:
			r = requests.get(self.url+'MC',headers= self.headers)
			print r.text
		else:
			r = requests.get(self.url+'MC',headers= self.headers,params=params)
			return json.loads(r.text)['list']
			

	#this mehotd creates the specified mc in espo
	def create_MC(self, mc):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expaId': mc.expa_id,
		'name':mc.name,
		'assignedUserId':'1',
		'assignedUserName':'Admin',
		'teamsIds[]':[],
		'teamsNames[]':[]
		}
		r = requests.post(self.url+'MC', headers= headers,data=json.dumps(data))
		return json.loads(r.text)

	#updates an MC that already exists in espo
	def update_MC(self,mc):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expaId': mc.expa_id,
		}
		r = requests.request('PATCH',self.url+'MC/'+mc.espo_id, headers= headers,data=json.dumps(data))
		return json.loads(r.text)

 	#######################
 	#####  MC Ends ######
 	#######################


  	#######################
 	#####  APP Starts ######
 	#######################

	#this mehotd gets applications form espo using the sepcified espo ID
	def get_application(self, application_id):
		r = requests.get(self.url+'Application/'+application_id,headers= self.headers)
		return json.loads(r.text) if r.text != '' else  "{}"

	#this mehotd gets applications form espo using the sepcified expa ID
	def get_expa_application(self, application_id):
		params = {
			'where[0][type]':'equals',
			'where[0][attribute]':'expaId',
			'where[0][value]':application_id
			}
		r = requests.get(self.url+'Application',headers= self.headers,params=params)
		return json.loads(r.text)['list']  if r.text != '' else  None

	#gets a list of applications with the specified espo parameters 
	def get_applications(self, params= None):
		if params is None:
			r = requests.get(self.url+'Application',headers= self.headers)
			print r.text
		else:
			r = requests.get(self.url+'Application',headers= self.headers,params=params)
			return json.loads(r.text)['list']
		

	#this mehotd gets applications form espo using the sepcified espo ID
	def create_application(self, application):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': application.expa_id,
		'assignedUserId':'1',
		'assignedUserName':'Admin',
		'teamsIds[]':[],
		'teamsNames[]':[]
		}
		r = requests.post(self.url+'Application', headers= headers,data=json.dumps(data))
		return json.loads(r.text)

	#updates an application that already exists in podio
	def update_application(self,application):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': application.expa_id,
		}
		r = requests.request('PATCH',self.url+'Application/'+application.espo_id, headers= headers,data=json.dumps(data))
		return json.loads(r.text)

 	#######################
 	#####  App Ends ######
 	#######################


 	#######################
 	#####  Enabler Starts ######
 	#######################

	#this mehotd gets enablers form espo using the sepcified espo ID
	def get_enabler(self, enabler_id):
		r = requests.get(self.url+'EnablerEXPA/'+mc_id,headers= self.headers)
		return json.loads(r.text)  if r.text != '' else  "{}"


	#this mehotd gets enablers form espo using the sepcified expa ID
	def get_expa_enabler(self, enabler_id):
		if self.test:
			params = {
				'where[0][type]':'equals',
				'where[0][attribute]':'todo',
				'where[0][value]':enabler_id
				}
		else:
			return None

		r = requests.get(self.url+'EnablerEXPA',headers= self.headers,params=params)
		return json.loads(r.text)['list']


	#gets a list of enablers with the specified espo parameters 
	def get_enablers(self, params=None):
		if params is None:
			r = requests.get(self.url+'EnablerEXPA',headers= self.headers)
			print r.text
		else:
			r = requests.get(self.url+'EnablerEXPA',headers= self.headers,params=params)
			return json.loads(r.text)['list']

	#this mehotd gets enablers form espo using the sepcified espo ID
	def create_enabler(self, enabler):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': enabler.expa_id,
		'assignedUserId':'1',
		'assignedUserName':'Admin',
		'teamsIds[]':[],
		'teamsNames[]':[]
		}
		r = requests.post(self.url+'EnablerEXPA', headers= headers,data=json.dumps(data))
		return json.loads(r.text)

	#updates an enabler that already exists in podio
	def update_enabler(self,enabler):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': enabler.expa_id,
		}
		r = requests.request('PATCH',self.url+'EnablerEXPA/'+enabler.espo_id, headers= headers,data=json.dumps(data))
		return json.loads(r.text)


 	#######################
 	#####  Enabler Ends ######
 	#######################


 	#######################
 	#####  LC Starts ######
 	#######################

	#this mehotd gets lcs form espo using the sepcified espo ID
	def get_lc(self, lc_id):
		r = requests.get(self.url+'LC/'+mc_id,headers= self.headers)
		return json.loads(r.text)  if r.text != '' else  "{}"

	#this mehotd gets lcs form espo using the sepcified expa ID
	def get_expa_lc(self, lc_id):
		if self.test:
			params = {
				'where[0][type]':'equals',
				'where[0][attribute]':'expaId',
				'where[0][value]':lc_id
				}
		else:
			return None

		r = requests.get(self.url+'LC',headers= self.headers,params=params)
		return json.loads(r.text)['list']



	#gets a list of lcs with the specified espo parameters 
	def get_lcs(self, params=None):
		if params is None:
			r = requests.get(self.url+'LC',headers= self.headers)
			print r.text
		else:
			r = requests.get(self.url+'LC',headers= self.headers,params=params)
			return json.loads(r.text)['list']

	#this mehotd gets lcs form espo using the sepcified espo ID
	def create_lc(self, lc):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expaId': lc.expa_id,
		'assignedUserId':'1',
		'name':lc.name,
		'assignedUserName':'Admin',
		'teamsIds[]':[],
		'teamsNames[]':[]
		}
		r = requests.post(self.url+'LC', headers= headers,data=json.dumps(data))
		return json.loads(r.text)

	#setting the MC for an LC
	def set_mc_to_lc(self,lc, mc):
		data ={'mCId': mc.espo_id}
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		r = requests.request('PATCH',self.url+'LC/'+str(lc.espo_id), headers= headers,data=json.dumps(data))
		print r.url
		return r.text



	#updates an lc that already exists in podio
	def update_lc(self,lc):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'eXPAId': lc.expa_id,
		}
		r = requests.request('PATCH',self.url+'LC/'+lc.espo_id, headers= headers,data=json.dumps(data))
		return json.loads(r.text)


 	#######################
 	#####  LC Starts ######
 	#######################


 	#######################
 	#####  Oppo Starts ######
 	#######################


	#this mehotd gets opportunities form espo using the sepcified espo ID
	def get_opportunity(self, opportunity_id):
		r = requests.get(self.url+'OpportunityExpa/'+opportunity_id,headers= self.headers)
		return json.loads(r.text)  if r.text != '' else  "{}"

	#this mehotd gets opportunities form espo using the sepcified expa ID
	def get_expa_opportunity(self, opportunity_id):
		if self.test:
			params = {
				'where[0][type]':'equals',
				'where[0][attribute]':'todo',
				'where[0][value]':opportunity_id
				}
		else:
			return None
		r = requests.get(self.url+'OpportunityExpa',headers= self.headers,params=params)
		return json.loads(r.text)['list']

	#gets a list of opportunities with the specified espo parameters 
	def get_opportunities(self, params=None):
		if params is None:
			r = requests.get(self.url+'OpportunityExpa',headers= self.headers)
			print r.text
		else:
			r = requests.get(self.url+'OpportunityExpa',headers= self.headers,params=params)
			return json.loads(r.text)['list']

	#this mehotd gets opportunitys form espo using the sepcified espo ID
	def create_opportunity(self, opportunity):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': opportunity.expa_id,
		'assignedUserId':'1',
		'assignedUserName':'Admin',
		'teamsIds[]':[],
		'teamsNames[]':[]
		}
		r = requests.post(self.url+'OpportunityExpa', headers= headers,data=json.dumps(data))
		return json.loads(r.text)

	#updates an opportunity that already exists in podio
	def update_opportunity(self,opportunity):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': opportunity.expa_id,
		}
		r = requests.request('PATCH',self.url+'OpportunityExpa/'+opportunity.espo_id, headers= headers,data=json.dumps(data))
		return json.loads(r.text)

 	#######################
 	#####  Opp Ends ######
 	#######################


 	#######################
 	#####  Person Starts ######
 	#######################


	#this mehotd gets persons form espo using the sepcified espo ID
	def get_person(self, person_id):
		r = requests.get(self.url+'Person/'+person_id,headers= self.headers)
		return json.loads(r.text)  if r.text != '' else  "{}"


	#this mehotd gets persons form espo using the sepcified espo ID
	def get_expa_person(self, person_id):
		if self.test:
			params = {
				'where[0][type]':'equals',
				'where[0][attribute]':'todo',
				'where[0][value]':person_id
				}
		else:
			return None

		r = requests.get(self.url+'Person',headers= self.headers,params=params)
		return json.loads(r.text)['list']

	#gets a list of persons with the specified espo parameters 
	def get_persons(self, params=None):
		if params is None:
			r = requests.get(self.url+'Person',headers= self.headers)
			print r.text
		else:
			r = requests.get(self.url+'Person',headers= self.headers,params=params)
			return json.loads(r.text)['list']

	#this mehotd gets persons form espo using the sepcified espo ID
	def create_person(self, person_id):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': person_id,
		'assignedUserId':'1',
		'assignedUserName':'Admin',
		'teamsIds[]':[],
		'teamsNames[]':[]
		}
		r = requests.post(self.url+'Person', headers= headers,data=json.dumps(data))
		return json.loads(r.text)

	#updates an person that already exists in podio
	def update_person(self,person):
		headers = self.headers
		headers['Content-Type'] = 'application/json'
		data ={'expa_id': person.expa_id,
		}
		r = requests.request('PATCH',self.url+'Person/'+person.espo_id, headers= headers,data=json.dumps(data))
		return json.loads(r.text)


	#######################
 	#####  Person ends ######
 	#######################
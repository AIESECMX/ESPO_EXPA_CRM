from Controller.gis_token_generator import GIS
from Controller.espo import ESPO
from Controller.expa import EXPA
<<<<<<< HEAD
#import config
import json
=======
import config
from Model.mc import MC
from Model.lc import LC
from Model.application import Appl
import datetime

#this ehits starts everything up, it searches for applications with their lasninteractiosn in the last day and puts
# in the CRM
def get_appls(expa,espo, date = datetime.date.today()-datetime.timedelta(1) ):

	#TODO: get the lcs form mexico since those will be recurrently used

	params = {
	'filters[last_interaction][from]':date.strftime('%y-%m-%d')

	}
	appls_expa = expa.get_Applications(params)
	#def __init__(self, expa_id,espo_id=0,person_id , op_id ,person_lc_id , op_lc_id = 0):
	for appl in appls_expa:
		print 'appl id:' +str(appl['id'])
		print 'perosn id id:' +str(appl['person']['id'])
		print 'person lc id:' +( str(appl['person']['home_lc']['id']) )
		#print 'person country:' +(appl['person']['home_lc']['country'] if appl['person']['home_lc']['country'] != None else '')
		print 'op id:' +str(appl['opportunity']['id'])
		print 'op lc id:' +str(appl['opportunity']['office']['id'])
		#print 'op country name:'+appl['opportunity']['office']['country']
		print 'op country id:'+str(appl['opportunity']['office']['parent_id'])
		print '\nSEPARADOR LO MAXIMO \n'
		#creando las aplicaciones que tuvieron las updates en el ultimo dia
		appl_espo = Appl(expa_id = appl['id'],person_id= appl['person']['id'], op_id = appl['opportunity']['office']['id'],
			person_lc_id = appl['person']['home_lc']['id'] , op_lc_id = appl['opportunity']['office']['id'])
		#we need to check if the app already exist or if tis a new app (in espo)
		#this line meas that there is somehting in ESPO with this expa ID
		if  espo.get_expa_application(appl['id']):
			#todo check the update works
			espo.update_application(appl_espo)
		#here we dont have this appl in espo and so we need to create it 
		#we need to check if the op and ep lc exist in the CRM
		else:
			#check if the lc exist
			print 'check lc espo'
			check_lc_espo(expa,espo,appl['opportunity']['office']['id'],appl['opportunity']['office']['name'])
			

#this method works to see if the a local committee exists already in espo
def check_lc_espo(expa,espo,lc_id,lc_name):
	#esto quiere decir que el lc no esta en el CRM
	lc =LC(lc_name,lc_id)
	#getting the lcs in espo that could match the id
	lcs_espo = espo.get_expa_lc(lc_id)
	print lcs_espo
	if len(lcs_espo) == 0:
		
		lc_expa = expa.get_LC(lc_id)
		print 'creado lc '
		print lc_expa
		#saving the lc to espo
		lc_espo =  espo.create_lc(lc)
		lc.espo_id = lc_espo['id']
		if lc_expa['parent']:
			#check f the mc is already in expa or put it there
			mc_espo =  check_mc_espo(expa,espo,lc_expa['parent']['id'],lc_expa['parent']['name'],lc)
			#here we will create the relation between mc and lc

	#este else quiere decir que el lc si esta en espo y hay que regresar le id del lc
	else:
		return LC(lcs_espo[0]['name'],lcs_espo[0]['expaId'],lcs_espo[0]['id'])

#check if the mc exist in expa and if not then it puts it in expa
def check_mc_espo(expa,espo,mc_id,mc_name,lc):
	mc = espo.get_expa_MC(mc_id)
	#check if there is the mc in espo
	print 'checking mc '+mc_name
	if  mc == None:
		print 'no se encontro'
		#if the mc is in not in espo the create it
		mc_espo = espo.create_MC(MC(mc_name,mc_id))
		espo.set_mc_to_lc( lc , MC (mc_espo['name'], expa_id=mc_espo['expaId'], espo_id=mc_espo['id']))
		return MC(mc_espo['name'],mc_espo['expaId'],mc_espo['id'])
	else:
		print 'si se encontro'
		#if the mc is in espo then return it
		return  MC(mc.name,mc.expa_id,mc.espo_id) 


>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b


def main():

	#test = True
	#if test:
	#	user = config.CRM_TEST_USER
	#	passwd = config.CRM_TEST_PASSWD
	#else:
	#	user = config.CRM_USER
	#	passwd = config.CRM_PASSWD


<<<<<<< HEAD
	#espo =  ESPO(user,passwd,test = test )
	#print espo.token
	#espo.get_MC('58d192e82587727f1')
	#espo.get_applications()
	#espo.get_persons()
	#espo.get_opportunities()
	#espo.get_lcs()
	#espo.get_enablers()
	
	#Autenticarse en EXPA
	expa =  EXPA('enrique.suarez@aiesec.net','si no leo me aburro')
	
	#gisparser = GIS()
	#print gisparser.generate_token('enrique.suarez@aiesec.net','si no leo me aburro')
	#exit()
	
	#Guardar en cada archivo los datos recibidos.
	with open('data/mc.json','w+') as outfileMC:
		json.dump(expa.get_MC(), outfileMC)
		
	with open('data/mcs.json','w+') as outfileMCs:
		json.dump(expa.get_MCs(), outfileMCs)
		
	with open('data/lc.json','w+') as outfileLC:
		json.dump(expa.get_LC(1287), outfileLC)
		
	with open('data/lcs.json','w+') as outfileLCs:
		json.dump(expa.get_LCs({'filters[home_committee]':[1168]}), outfileLCs)
		
	with open('data/people.json','w+') as outfilePeople:
		json.dump(expa.get_People({'filters[home_committee]':[1168]}), outfilePeople)	
		 
	with open('data/person.json','w+') as outfilePerson:
		json.dump(expa.get_Person(748379), outfilePerson)
		
	with open('data/opps.json','w+') as outfileOpps:
		json.dump(expa.get_Opps({'filters[committee]':[1014]}), outfileOpps)
	
	with open('data/opp.json','w+') as outfileOpp:
		json.dump(expa.get_Opp(820570), outfileOpp)
		
	#print tokeng.generate_token('','')
	#print tokeng.generate_op_token('','')
	print 'exito!'
=======
	espo =  ESPO(user,passwd,test = test )
	#print  espo.get_application('')
	expa =  EXPA(config.EXPA_USER,config.EXPA_PASS)
	get_appls(expa,espo)
	#print expa.get_LCs()
>>>>>>> c9c6d96b523380be0f7df2a02605d744ff3b681b
	
if __name__ == '__main__':
	main()
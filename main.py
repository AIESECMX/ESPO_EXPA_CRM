from Controller.gis_token_generator import GIS
from Controller.espo import ESPO
from Controller.expa import EXPA
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
			check_lc_espo(expa,espo,appl['opportunity']['office']['id'],appl['opportunity']['office']['name'])
			return None

#this method works to see if the a local committee exists already in espo
def check_lc_espo(expa,espo,lc_id,lc_name):
	#esto quiere decir que el lc no esta en el CRM
	if len(espo.get_expa_lc(lc_id)) == 0:
		#todo create the lc in espo
		lc = expa.get_LC(lc_id)
		print 'creado lc '
		print lc 
		#saving the lc to espo
		lc_espo =  espo.create_lc(LC(lc_name,lc_id))
		if lc['parent']:
			print 'si tenia parent'
			#TODO: we are saving the mc but we need to also create the relation with the LC
			mc_espo =  check_mc_espo(expa,espo,lc['parent']['id'],lc['parent']['name'])
			print 'MC ESPO'
			print 'MC ESPO'
			print mc_espo
			#here we will create the relation between mc and lc
			print espo.set_mc_to_lc( LC (lc_espo['name'], espo_id=lc_espo['id']) , MC (mc_espo['name'], espo_id=mc_espo['id']) )

	#este else quiere decir que el lc si esta en espo y hay que regresar le id del lc
	else:
		return None
	print espo.get_expa_lc(lc_id)

def check_mc_espo(expa,espo,mc_id,mc_name):
	mc = espo.get_MC(mc_id)
	if len(mc) == 0:
		return espo.create_MC(MC(mc_name,mc_id))
	else:
		return mc[0] 




def main ():

	test = True
	if test:
		user = config.CRM_TEST_USER
		passwd = config.CRM_TEST_PASSWD
	else:
		user = config.CRM_USER
		passwd = config.CRM_PASSWD


	espo =  ESPO(user,passwd,test = test )
	#print  espo.get_application('')
	expa =  EXPA('enrique.suarez@aiesec.net','si no leo me aburro')
	get_appls(expa,espo)
	#print expa.get_LCs()
	
if __name__ == '__main__':
	main()
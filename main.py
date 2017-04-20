from Controller.gis_token_generator import GIS
from Controller.espo import ESPO
from Controller.expa import EXPA
import config
from Model.mc import MC
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
		print 'person country:' +appl['person']['home_lc']['country']
		print 'op id:' +str(appl['opportunity']['id'])
		print 'op lc id:' +str(appl['opportunity']['office']['id'])
		print 'op country name:'+appl['opportunity']['office']['country']
		print 'op country id:'+str(appl['opportunity']['office']['parent_id'])
		print '\nSEPARADOR LO MAXIMO \n'
		#creando las aplicaciones que tuvieron las updates en el ultimo d
		appl_espo = Appl(expa_id = appl['id'],person_id= appl['person']['id'], op_id = appl['opportunity']['office']['id'],
			person_lc_id = appl['person']['home_lc']['id'] , op_lc_id = appl['opportunity']['office']['id'])
		#we need to check if the app already exist or if tis a new app (in espo)
		#we need to check if the op and ep lc exist in the CRM






def main ():

	test = True
	if test:
		user = config.CRM_TEST_USER
		passwd = config.CRM_TEST_PASSWD
	else:
		user = config.CRM_USER
		passwd = config.CRM_PASSWD


	espo =  ESPO(user,passwd,test = test )
	print  espo.get_application('2806386')
	#expa =  EXPA('enrique.suarez@aiesec.net','si no leo me aburro')
	#get_appls(expa,espo)
	#print expa.get_LCs()
	
if __name__ == '__main__':
	main()
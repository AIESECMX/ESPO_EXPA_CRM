from Controller.gis_token_generator import GIS
from Controller.espo import ESPO
from Controller.expa import EXPA
import config
from Model.mc import MC
import datetime

#this ehits starts everything up, it searches for applications with their lasninteractiosn in the last day and puts
# in the CRM
def get_appls(expa,espo, date = datetime.date.today()-datetime.timedelta(1) ):
	params = {
	'filters[last_interaction][from]':date.strftime('%y-%m-%d')
	}
	appls_expa = expa.get_Applications(params)
	print appls_expa





def main ():

	test = True
	if test:
		user = config.CRM_TEST_USER
		passwd = config.CRM_TEST_PASSWD
	else:
		user = config.CRM_USER
		passwd = config.CRM_PASSWD


	espo =  ESPO(user,passwd,test = test )
	#mc = MC('imaginario',str(9),'58f8f88e3bdb98c4a')
	#espo.create_MC(mc)
	#espo.create_application(7)
	#espo.create_enabler(7)
	#espo.create_lc(7)
	#espo.create_opportunity(7)
	#print espo.token
	#espo.get_MC('58d192e82587727f1')
	#espo.get_MCs()
	#espo.update_MC(mc)
	#print espo.get_expa_MC(1589)
	#espo.get_applications()
	#espo.get_persons()
	#espo.get_opportunities()
	#espo.get_lcs()
	#espo.get_enablers()
	expa =  EXPA('enrique.suarez@aiesec.net','si no leo me aburro')
	get_appls(expa,espo)
	#print expa.get_LCs()
	#print tokeng.generate_token('','')
	#print tokeng.generate_op_token('','')
	
if __name__ == '__main__':
	main()
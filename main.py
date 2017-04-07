from Controller.gis_token_generator import GIS
from Controller.espo import ESPO
from Controller.expa import EXPA
import config


def main ():

	test = True
	if test:
		user = config.CRM_TEST_USER
		passwd = config.CRM_TEST_PASSWD
	else:
		user = config.CRM_USER
		passwd = config.CRM_PASSWD


	#espo =  ESPO(user,passwd,test = test )
	#print espo.token
	#espo.get_MC('58d192e82587727f1')
	#espo.get_applications()
	#espo.get_persons()
	#espo.get_opportunities()
	#espo.get_lcs()
	#espo.get_enablers()
	expa =  EXPA('enrique.suarez@aiesec.net','si no leo me aburro')
	expa.get_LCs()
	#print tokeng.generate_token('','')
	#print tokeng.generate_op_token('','')
	
if __name__ == '__main__':
	main()
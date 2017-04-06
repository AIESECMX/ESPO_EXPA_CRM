from Controller.gis_token_generator import GIS
from Controller.espo import ESPO
import config


def main ():



	print ESPO(config.CRM_USER,config.CRM_PASSWD,test = False).token
	#tokeng =  GIS()
	#print tokeng.generate_token('enrique.suarez@aiesec.net','si no leo me aburro')
	#print tokeng.generate_op_token('enrique.suarez@aiesec.net','si no leo me aburro')
	
if __name__ == '__main__':
	main()
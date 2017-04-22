from Controller.gis_token_generator import GIS
from Controller.espo import ESPO
from Controller.expa import EXPA
#import config
import json


def main():

	#test = True
	#if test:
	#	user = config.CRM_TEST_USER
	#	passwd = config.CRM_TEST_PASSWD
	#else:
	#	user = config.CRM_USER
	#	passwd = config.CRM_PASSWD


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
	
if __name__ == '__main__':
	main()
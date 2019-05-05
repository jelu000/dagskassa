

while 1:
	
	dagskassa = input('intäkter: ')
	dagskassa = float(dagskassa)
	
	babs = input('babs: ')
	babs = float(babs)
	
	forsaljning = input('försäljning: ')
	forsaljning = float(forsaljning)
	
	kassa = dagskassa-babs
	jobbkassa = dagskassa-forsaljning
	
	moms = 0.2*dagskassa
	
	jobbKassaExMoms = 0.8*jobbkassa
	forsaljningExMoms = 0.8*forsaljning
	print('----------------------------------')
	#moms=round(moms, 2)
	#exmoms=round(exmoms, 2)
	print('Babs-1930: ', '{:.2f}'.format(babs))
	print('Kassa-1910: ', '{:.2f}'.format(kassa))
	
	print('Moms-2611: ', '{:.2f}'.format(moms))
	print('FörsäljningTjänst-3041: ', '{:.2f}'.format(jobbKassaExMoms))
	print('Försäljningvaror-3051: ', '{:.2f}'.format(forsaljningExMoms))
	
	if 'n'==input('fler beräkningar? j/n. ') :
		break
	print('---------------------------')	
	
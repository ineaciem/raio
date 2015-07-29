#!/usr/local/bin/python2.7

def raios():
	import time
	raios = []
	with open("convert", "r") as ins:
		for line in ins:
			data=(line).replace(',','').replace('[',' ').replace(']',' ')
			raios.append(data.split())

	x = 0
	while x != len(raios):
		leng_geral1 = float(raios[x][0])
		leng_geral2 = float(raios[x][1])
		leng_geral = (leng_geral1*256)+leng_geral2
		a = int(leng_geral)-1
		y = 32
		b = 58
		while y != len(raios[x][58:a]):
			print(raios[x])
#------------------------------------------------------------------------
			tipe = (raios[x][1+b])
#------------------------------------------------------------------------
			data1 = float(raios[x][2+b])
			data2 = float(raios[x][3+b])
			data3 = float(raios[x][4+b])
			data4 = float(raios[x][5+b])
			seconds_since = time.gmtime((((((data1*256)+data2)*256)+data3)*256)+data4)
			seconds_since1 = str(seconds_since.tm_mday)+'/'+str(seconds_since.tm_mon)+'/'+str(seconds_since.tm_year)+' '+str(seconds_since.tm_hour)+':'+str(seconds_since.tm_min)+':'+str(seconds_since.tm_sec)
#------------------------------------------------------------------------
			lat1 = float(raios[x][10+b])
			lat2 = float(raios[x][11+b])
			lat3 = float(raios[x][12+b])
			lat4 = float(raios[x][13+b])
			lat_pulse_dec = float((((((lat1*256)+lat2)*256)+lat3)*256)+lat4)/10000000
#------------------------------------------------------------------------
			lon1 = float(raios[x][14+b])
			lon2 = float(raios[x][15+b])
			lon3 = float(raios[x][16+b])
			lon4 = float(raios[x][17+b])
			lon_pulse_dec = float((((((lon1*256)+lon2)*256)+lon3)*256)+lon4)/10000000
#------------------------------------------------------------------------
			anp1 = float(raios[x][18+b])
			anp2 = float(raios[x][19+b])
			anp3 = float(raios[x][20+b])
			anp4 = float(raios[x][21+b])
			anp_pulse_dec = float((((((anp1*256)+anp2)*256)+anp3)*256)+anp4)/10000000
#------------------------------------------------------------------------
			ic1 = float(raios[x][22+b])
			ic2 = float(raios[x][23+b])
			ic_pulse_dec = float((ic1*256)+ic2)
#------------------------------------------------------------------------
			n_sensor_pulse = int(raios[x][24+b])
#------------------------------------------------------------------------
			erro_major1 = float(raios[x][25+b])
			erro_major2 = float(raios[x][26+b])
			erro_major_dec = float((erro_major1*256)+erro_major2)
#------------------------------------------------------------------------
			erro_minor1 = float(raios[x][27+b])
			erro_minor2 = float(raios[x][28+b])
			erro_minor_dec = float((erro_minor1*256)+erro_minor2)
#------------------------------------------------------------------------
			erro_ellip1 = float(raios[x][29+b])
			erro_ellip2 = float(raios[x][30+b])
			erro_ellip_dec = float((erro_ellip1*256)+erro_ellip2)
#------------------------------------------------------------------------
			if float(tipe) != 9:
				f = open('pulse.txt','a')
				f.write(str(tipe)+' '+str(seconds_since1)+' '+str(lat_pulse_dec)+' '+str(lon_pulse_dec)+' '+str(anp_pulse_dec)+' '+str(ic_pulse_dec)+' '+str(n_sensor_pulse)+' '+str(erro_major_dec)+' '+str(erro_minor_dec)+' '+str(erro_ellip_dec)+' '+'\n')
				f.close()
			b = 58 + y
			y += 32

#------------------------------------------------------------------------
		tipe = (raios[x][3])
#------------------------------------------------------------------------
		data1 = float(raios[x][4])
		data2 = float(raios[x][5])
		data3 = float(raios[x][6])
		data4 = float(raios[x][7])
		seconds_since = time.gmtime((((((data1*256)+data2)*256)+data3)*256)+data4)
		seconds_since1 = str(seconds_since.tm_mday)+'/'+str(seconds_since.tm_mon)+'/'+str(seconds_since.tm_year)+' '+str(seconds_since.tm_hour)+':'+str(seconds_since.tm_min)+':'+str(seconds_since.tm_sec)
#------------------------------------------------------------------------
		lat1 = float(raios[x][12])
		lat2 = float(raios[x][13])
		lat3 = float(raios[x][14])
		lat4 = float(raios[x][15])
		lat_pulse_dec = float((((((lat1*256)+lat2)*256)+lat3)*256)+lat4)/10000000
#------------------------------------------------------------------------
		lon1 = float(raios[x][16])
		lon2 = float(raios[x][17])
		lon3 = float(raios[x][18])
		lon4 = float(raios[x][19])
		lon_pulse_dec = float((((((lon1*256)+lon2)*256)+lon3)*256)+lon4)/10000000
#-----------------------------------------------------------------------
		anp1 = float(raios[x][20])
		anp2 = float(raios[x][21])
		anp3 = float(raios[x][22])
		anp4 = float(raios[x][23])
		anp_pulse_dec = float((((((anp1*256)+anp2)*256)+anp3)*256)+anp4)/10000000
#------------------------------------------------------------------------
		ic1 = float(raios[x][24])
		ic2 = float(raios[x][25])
		ic_pulse_dec = float((ic1*256)+ic2)
#------------------------------------------------------------------------
		n_sensor_pulse = int(raios[x][26])
#------------------------------------------------------------------------
		ic_multiple = int(raios[x][27])
#------------------------------------------------------------------------
		cg_multiple = int(raios[x][28])
#------------------------------------------------------------------------
		st1 = float(raios[x][29])
		st2 = float(raios[x][30])
		st3 = float(raios[x][31])
		st4 = float(raios[x][32])
		st = time.gmtime((((((st1*256)+st2)*256)+st3)*256)+st4)
#------------------------------------------------------------------------
		timenano1 = float(raios[x][33])
		timenano2 = float(raios[x][34])
		timenano3 = float(raios[x][35])
		timenano4 = float(raios[x][36])
		timenano = time.gmtime((((((timenano1*256)+timenano2)*256)+timenano3)*256)+timenano4)
#------------------------------------------------------------------------
		duracao1 = float(raios[x][37])
		duracao2 = float(raios[x][38])
		duracao3 = float(raios[x][39])
		duracao4 = float(raios[x][40])
		duracao = time.gmtime((((((duracao1*256)+duracao2)*256)+duracao3)*256)+duracao4)
#------------------------------------------------------------------------
		ullat1 = float(raios[x][41])
		ullat2 = float(raios[x][42])
		ullat3 = float(raios[x][43])
		ullat4 = float(raios[x][44])
		ullat = float((((((ullat1*256)+ullat2)*256)+ullat3)*256)+ullat4)/10000000
#-----------------------------------------------------------------------
		ullon1 = float(raios[x][45])
		ullon2 = float(raios[x][46])
		ullon3 = float(raios[x][47])
		ullon4 = float(raios[x][48])
		ullon = float((((((ullon1*256)+ullon2)*256)+ullon3)*256)+ullon4)/10000000
#------------------------------------------------------------------------
		lrlat1 = float(raios[x][49])
		lrlat2 = float(raios[x][50])
		lrlat3 = float(raios[x][51])
		lrlat4 = float(raios[x][52])
		lrlat_pulse_dec = float((((((lrlat1*256)+lrlat2)*256)+lrlat3)*256)+lrlat4)/10000000
#------------------------------------------------------------------------
		lrlon1 = float(raios[x][53])
		lrlon2 = float(raios[x][54])
		lrlon3 = float(raios[x][55])
		lrlon4 = float(raios[x][56])
		lrlon_pulse_dec = float((((((lrlon1*256)+lrlon2)*256)+lrlon3)*256)+lrlon4)/10000000
#------------------------------------------------------------------------
		if float(tipe) != 9:
			f = open('flash.txt','a')
			f.write(str(tipe)+' '+str(seconds_since1)+' '+str(lat_pulse_dec)+' '+str(lon_pulse_dec)+' '+str(anp_pulse_dec)+' '+str(ic_pulse_dec)+' '+str(n_sensor_pulse)+' '+str(ic_multiple)+' '+str(cg_multiple)+' '+str(st)+' '+str(ullat)+' '+str(ullon)+' '+str(lrlat_pulse_dec)+' '+str(lrlon_pulse_dec)+'\n')
			f.close()
		x += 1

raios()

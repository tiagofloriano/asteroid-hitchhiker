#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Search objects (asteroids and comets) on Small Body Database/NASA.
Usage:
    Change filters on code and run this file.
Author:
    Tiago Floriano - 2022-07-18
License:
    GNU GPL v3 License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>5.
'''

import time, requests, json, urllib.parse, math, ctypes
import urllib.request as request

from os import system, name

# windows alert
# https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# define our clear function
# https://www.geeksforgeeks.org/clear-screen-python/
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
while True:

    # editar aqui
    
    urldata = "https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name,moid,moid_jup,per,diameter,density,rot_per&limit=500&sort=per&sb-kind=a&sb-cdata="
    
    param = "{ \"AND\" : [ \"moid|LT|0.1\", \"rot_per|DF\", \"diameter|DF\", \"per|LT|730\", \"diameter|GT|0.3\" ] }"
    
    paramencode = urllib.parse.quote(str(param))
    data = 0
    with request.urlopen(urldata+paramencode) as response:
        source = response.read()
        data = json.loads(source)
        numeroderesultados = len(data['data']);
        print("\n######################### \n")
        print("Numero de resultados: {}".format(numeroderesultados))
        Mbox('Numero de resultados', 'Foram encontrados {} asteroides!'.format(numeroderesultados), 1)
        print("\n######################### \n")
        conta = 0
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("| {l_fullname:35} | {l_moid:10} | {l_moidjup:8} | {l_per:9} | {l_diam:8} | {l_dens:8} | {l_rotper:12} | {l_vang:10} | {l_vlin:10} | ".format(l_fullname="FULL NAME", l_moid="MOID", l_moidjup="MOID JUP", l_per="PERIODO", l_diam="DIAMETRO", l_dens="DENSIDADE", l_rotper="ROT. PER.", l_vang="VEL. ANG.", l_vlin="VEL. LIN."))
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        for x in data['data']:
            velang = 2*math.pi/(float(x[6])*3600) # calcula velocidade angular
            vellin = velang*((float(x[4])*1000)/2) # calcula velocidade linear
            # transforma em string para poder limitar caracteres ao exibir
            velang=str(velang) 
            vellin=str(vellin) 
            print("| {fullname:35} | {moid:10} | {moidjup:8} | {per:9} | {diam:8} | {densid:9} | {rotper:12} | {vang:10} | {vlin:10} |".format(fullname=x[0], moid=x[1], moidjup=x[2], per=x[3], diam=x[4], densid=str(x[5]), rotper=x[6], vang=velang[0:8], vlin=vellin[0:8]))
        
    # fim da edição
        
    answer = str(input('Recomeçar? (s/n): '))
    #if answer in ('s', 'n'):
    #    print("Opção inválida")
    #    break
    if answer == 's':
        clear()
        continue
    else:
        print("Adeus! E obrigado pelos peixes!")
        time.sleep(2)
        break
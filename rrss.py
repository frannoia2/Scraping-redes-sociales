from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

def find_rrss(driver, urls, xpath_list, f):
    count = 0
    facebook = 0; twitter = 0; instagram = 0; youtube = 0; blog = 0; tiktok = 0; pinterest = 0; spotify = 0 
    enlaceface = 'No tiene'; enlacetwi = 'No tiene'; enlaceinst = 'No tiene'; enlaceyout = 'No tiene'; enlaceblog = 'No tiene' 
    enlacetik = 'No tiene'; enlacepint = 'No tiene'; enlacespoti = 'No tiene' 
    unique_url = list()     
    for url, xpath in zip(urls, xpath_list):
        try:
                driver.get(url)
                #muestra las paginas que lee del txt y las numera 
                count +=1
                print ("\n{} - {}\n".format(url.strip(), count))
                f.write("\n{} - {}\n".format(url.strip(), count))
                elementos = driver.find_elements(By.XPATH, xpath)
                try:
                    #obtenemos los enlaces a las rrss de las paginas
                    for a in elementos:
                            enlace = a.get_attribute('href')
                            #eliminamos duplicados
                            if enlace not in unique_url:
                                unique_url.append(enlace)
                                #comprobamos las rrss que tiene la pagina y marcamos las que si subiendo count a 1 
                                if enlace.find('facebook')!= -1: facebook+=1; enlaceface = enlace 
                                if enlace.find('twitter')!= -1: twitter+=1; enlacetwi = enlace
                                if enlace.find('instagram')!= -1: instagram+=1; enlaceinst = enlace
                                if enlace.find('youtube')!= -1: youtube+=1; enlaceyout = enlace
                                if enlace.find('blog')!= -1: blog+=1; enlaceblog = enlace
                                if enlace.find('tiktok')!= -1: tiktok+=1; enlacetik = enlace 
                                if enlace.find('pinterest')!= -1: pinterest+=1; enlacepint = enlace
                                if enlace.find('spotify')!= -1: spotify+=1; enlacespoti = enlace
                    rrss = ['Facebook '+ str(facebook)+ ' ' + str(enlaceface), 'Twitter '+ str(twitter) + ' ' + str(enlacetwi), 
                            'Instagram '+ str(instagram) + ' ' + str(enlaceinst), 'Youtube '+ str(youtube) + ' ' + str(enlaceyout),
                            'Blog '+ str(blog) + ' ' + str(enlaceblog), 'Tiktok '+ str(tiktok) + ' ' + str(enlacetik), 
                            'Pinterest '+ str(pinterest) + ' ' + str(enlacepint), 'Spotify '+ str(spotify) + ' ' + str(enlacespoti)]
                    print ("\n".join(rrss))
                    f.write("\n".join(rrss)+"\n\n")
                    facebook = 0; twitter = 0; instagram = 0; youtube = 0; blog = 0; tiktok = 0; pinterest = 0; spotify = 0
                    enlaceface = 'No tiene'; enlacetwi = 'No tiene'; enlaceinst = 'No tiene'; enlaceyout = 'No tiene'; enlaceblog = 'No tiene' 
                    enlacetik = 'No tiene'; enlacepint = 'No tiene'; enlacespoti = 'No tiene' 
                    unique_url.clear()
                except NoSuchElementException:
                    print("El elemento especificado en el XPATH es incorrecto o no existe, vuelva a especificarlo en la configuración")
                    pass
                
        except TimeoutException as e:
            print("Timeout")

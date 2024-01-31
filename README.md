# Scraping-redes-sociales

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

**Scraper en selenium para obtener las redes sociales de una lista de sitios web.**

## Modo de empleo:

Para ejecutar el proceso completo deberemos lanzar el main.py el cuál llama primero a config.py, script que nos sirve para crear un .json de configuración a partir de unos parametros que meteremos por terminal, como son el tipo de navegador que se usará, el .txt con la lista de urls, los XPATH de los elementos a buscar en cada url.

```
python main.py
```
El siguiente proceso es desglosar ese .json de configuración y utilizar los parametros para que nuestro scraper rrss.py nos busque los elementos deseados y nos los devuelva en un archivo de texto junto con sus enlaces a las redes sociales, en caso de tenerlas.

```
https://mundo-r.com - 1

Facebook 1 https://www.facebook.com/osdeR.oficial/
Twitter 1 https://twitter.com/os_de_R
Instagram 1 https://www.instagram.com/os_de_r/?hl=es
Youtube 1 https://www.youtube.com/c/os_de_R
Blog 1 https://blog.mundo-r.com/
Tiktok 0 No tiene
Pinterest 0 No tiene
Spotify 0 No tiene

https://www.zara.com/es/ - 2

Facebook 1 https://www.facebook.com/Zara
Twitter 1 https://twitter.com/zaraes
Instagram 1 https://www.instagram.com/zara/
Youtube 1 http://www.youtube.com/user/zara
Blog 0 No tiene
Tiktok 1 https://www.tiktok.com/@zara
Pinterest 1 https://es.pinterest.com/zaraofficial
Spotify 1 https://open.spotify.com/user/r6ivwuv0ebk346hhxo446pbfv

```
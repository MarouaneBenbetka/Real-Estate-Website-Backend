from bs4 import BeautifulSoup 
import requests
import json 


URL = "https://www.beytic.com/annonces-immobilieres/"






def getAnnouncesLinks(pageURL):
    """@param pageURL: -all announces- page url
       @return: an array of links that take the -announce details- page
    """
    html_text = requests.get(pageURL).text
    soup= BeautifulSoup(html_text,"lxml")


    announces_cards = soup.find_all("div",class_=["properties","properties--management"])

    links = [announce_card.find("a",class_="item-photo")["href"] for announce_card in announces_cards]
    return links


def getPageLink(url,page_number):
    
    return f"{url}?_page={page_number}"


def scrap_page(page_url):
    res=[]
    for announce_page_url in getAnnouncesLinks(page_url):
        try:
            response = requests.get(announce_page_url)
            soup = BeautifulSoup(response.text,"lxml").find("div",class_="property")
            
            images= [ "https://www.beytic.com/"+img["src"] for img in soup.select("div.slider__img > img")]
            # print("Images :" , *images , sep="\n")
            
            price = soup.find("strong",class_="property__price-value").text.strip()
            # print("Price :",price,sep="\n")

            description = soup.find("div",class_="property__description").select_one("p").text
            # print("Description",description,sep="\n")

            typeAnnonce = soup.find("div",class_="property__ribon").text.strip()
            # print("type :",typeAnnonce,sep="\n")

            surface = soup.find("dd",class_="property__plan-value").text.replace("M²","").strip()
            # print("surface :",surface)

            property_info_soup = soup.find("div",class_="property__info")

            typeImmoblier = property_info_soup.select_one(".property__info-item:nth-child(1) strong").text
            # print("type immoblier :", typeImmoblier, "\n")

            wilaya,commune = map(str.strip,property_info_soup.select_one(".property__info-item:nth-child(2)").text.split(","))
            # print("wilaya commune",wilaya,commune,sep="\n")

            params_list_soup = soup.find("ul",class_="property__params-list")

            adresse = params_list_soup.select_one("li:nth-child(1) > strong").text
            date_publication = params_list_soup.select_one("li:nth-child(2) > strong").text

            # print("adresse :",adresse,"date_publication:",date_publication,sep="\n")

            
            name = BeautifulSoup(response.text,"lxml").select_one(".worker__name > a").text.strip()
            phone_number = BeautifulSoup(response.text,"lxml").select_one(".tel").text.replace("Tel.","").strip()

            # print("name",name,"phone",phone_number,sep="\n")

            res+=[
            {
                "wilaya":wilaya,
                "commune":commune,
                "address":adresse,
                "surface":surface,
                "date":date_publication,
                "prix":price,
                "typeAnnonce":typeAnnonce,
                "typeImmoblier":typeImmoblier,
                "description":description,
                "images":images,
                "contatcatInfo":{
                    "name":name,
                    "picture":None,
                    "email":None,
                    "phoneNumber":phone_number,
                },
                "coordinates":None
            }]
            print("added succefully")
        except Exception as e: 
            print(e)
    return res
        


def scrap_beytic_website(nb_pages_to_scrap):
    if nb_pages_to_scrap <= 0 or nb_pages_to_scrap>30 :return
    res=[]
    for page_count in range(1,nb_pages_to_scrap+1):
        page = getPageLink(URL,page_count)
        res+= scrap_page(page)
        print(f"page {page_count} finished scrapping")

    print(f"{len(res)} announces has been add succesfully")



    with open('./src/api/beytic_scrap_result.json', 'w+') as fp:
        json.dump(res, fp)
    
        



scrap_beytic_website(1)


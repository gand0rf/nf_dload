import requests
from bs4 import BeautifulSoup as BS
import os

def get_fonts():
    url = "https://www.nerdfonts.com/font-downloads"
    font_list = []
    result = requests.get(url).text
    soup = BS(result, "html.parser")
    a_list = soup.find_all('a', href=True)

    for a in a_list:
        if "github" in str(a):
            zip = a.get("href")
            if ".zip" in str(zip) and str(zip) not in font_list:
                font_list.append(str(zip))

    return font_list

def dload_fonts(home, font_list):

    if not os.path.exists(f'{home}/Downloads/fonts'):
        os.makedirs(f'{home}/Downloads/fonts')
    
    os.chdir(f'{home}/Downloads/fonts')

    for font in range(0,len(font_list)):
        print(f'Getting {font} out of {len(font_list)}..', end='\r')
        os.system(f'wget {font_list[font]} >/dev/null 2>&1')
    
    return 0

def unzip_fonts(home):
    if not os.path.exists(f'{home}/.local/share/fonts'):
        os.makedirs(f'{home}/.local/share/fonts')
    os.system(f"unzip -o '*.zip' -d {home}/.local/share/fonts >/dev/null 2>&1")

def zip_remove(home):
    os.system('rm *.zip')
    os.chdir(f'{home}/Downloads')
    os.rmdir(f'{home}/Downloads/fonts')

if __name__ == "__main__":
    home = os.path.expanduser('~')
    print('Getting font urls...')
    font_list = get_fonts()
    print('Font list made')
    print('Downloading font archives...')
    dload_fonts(home, font_list)
    print('Downloading completed')
    print('Unzipping fonts...')
    unzip_fonts(home)
    print('Unzipping completed')
    remove = input('Remove font zip archives? [y/n] ')
    if remove == 'y':
        zip_remove(home)
    print('Installation of Nerd Fonts complete. Enjoy!!')
            

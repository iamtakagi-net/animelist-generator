from requests import get
import re
from bs4 import BeautifulSoup
from math import ceil
from janome.tokenizer import Tokenizer
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import matplotlib.pyplot as plt
from io import BytesIO
import unicodedata
import numpy as np
import cv2
import zipfile
import urllib.request
import base64
import uuid
urllib.request.urlretrieve('https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml', 'lbpcascade_animeface.xml')

classifier = cv2.CascadeClassifier('lbpcascade_animeface.xml')
t = Tokenizer()
 
template = Image.new('RGB', (158, 332), (71, 71, 71))
 
part = Image.fromarray(np.r_[[[np.linspace(130.5, 84.5, 256)] * 256] *
                             3].T.astype(np.uint8))
 
aimsize = {
    "タイトル": (157, 39),
    "制作元請": (70, 39),
    "スタッフ": (86, 99),
    "キャスト": (70, 112),
    "放送スケジュール": (86, 52),
    "原作": (157, 37),
}
aimpoint = {
    "タイトル": (0, 103),
    "制作元請": (0, 142),
    "スタッフ": (71, 195),
    "キャスト": (0, 182),
    "放送スケジュール": (71, 142),
    "原作": (0, 295),
}
 
 
def get_data(url):
    global Title
    html = get(url).text
    soup = BeautifulSoup(html, 'html.parser')
 
    for i in soup.select("br"):
        i.replace_with("\n")
 
    Title = re.sub("(\d+)(.+)", "\\1\n\\2",
                   soup.title.text.replace("|", "｜").split("｜")[0])
    li = []
    headingh2 = soup.find_all('h2', class_='c-heading-h2')
    if headingh2[0].get("id") != "1":
        headingh2.pop(0)
    for i, j in zip(headingh2, soup.find_all('table')):
        a = [k.text for k in j.select("th")]
        a.append(a[0])
        a[0] = i.text
        aa = []
        for e in i.next_elements:
            if e.name == "img":
                aa.append(e["src"])
                break
        for k in a:
            if k:
                if k[0] == "\n":
                    k = k[1:]
                aa.append(k)
        li.append(aa)
 
    data = {}
    for i in li:
        d = {"img": "", "原作": "", "キャスト": "", "制作元請": "", "放送スケジュール": ""}
        data[i[1]] = d
        d["img"] = i[0]
        d["放送スケジュール"] = i[-1]
        d["キャスト"] = "\n".join(re.findall(".+:(.+)", i[2].replace("：", ":")))
        staff = []
        for j in i[3].splitlines():
            j = j.replace("：", ":")
            if len(j.split(':')) < 2: continue
            if "原作" in j:
                d["原作"] = " ".join(j.split(':')[1:])
            elif "制作" in j:
                d["制作元請"] = j.split(':')[1]
            else:
                staff.append("\n".join(j.split(':')))
        d["スタッフ"] = "\n".join(staff)
        for j in soup.find(text=f"『{i[1]}』最新記事・関連動画一覧").previous_elements:
            if j.name == "a" and "サイト" in j.text:
                data[i[1]]['href'] = j["href"]
                break
 
    return data
 
 
def len_(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count
 
 
def nn(text, w):
    tt = ""
    l = 0
    for j in t.tokenize(text, wakati=True):
        if l + len(j) > w:
            tt += "\n"
            l = 0
        elif j == "\n":
            l = 0
        tt += j
        l += len(j)
 
    return tt.replace("\n\n", "\n")
 
 
def mojiire(text, font_path, tmp, aimsize, aimpoint, case, hopt):
    text = text.replace("\n ", "\n")
    if case == 1:
        tm = Image.new('RGB', (256, 256), (66, 58, 59))
        if text:
            text = nn(text, 14)
    elif case == 2:
        tm = part.copy()
        if text:
            text = nn("\n".join(text.splitlines()[-3:]), 10) + "\n "
    elif case == 3:
        tm = part.copy()
        if text:
            text = nn(text, 20)
            while len_(text) < 20:
                text += " "
    else:
        tm = part.copy()
        if text:
            text = nn("\n".join(text.splitlines()[:8]), 10)
    if text:
        while len(text.splitlines()) < hopt:
            text += "\n "
        font = ImageFont.truetype(font_path, 100)
        draw = ImageDraw.Draw(tm)
        x, y = draw.textsize(text, font=font, spacing=1)
        tm = tm.resize((x + 30, y + 30))
        draw = ImageDraw.Draw(tm)
        draw.text((15, 15), text, font=font, spacing=1)
        tm = tm.resize(aimsize)
        if case == 2:
            draw = ImageDraw.Draw(tm)
            draw.line((0, 39, aimsize[0], 39), fill=(179, 179, 179), width=1)
    else:
        tm = tm.resize(aimsize)
    tmp.paste(tm, aimpoint)
 
 
def area(x, y, href):
    h, w = template.height, template.width
    return f'<area shape="rect" coords="{y * w},{x * h},{(y + 1) * w},{(x + 1) * h}" href="{href}" target="_blank" rel="noopener"/>'
 
def generate(url):
    urllib.request.urlretrieve('http://moji.or.jp/wp-content/ipafont/IPAfont/ipag00303.zip', 'ipag00303.zip')
    with zipfile.ZipFile('ipag00303.zip') as zf:
      zf.extractall()
    font_title = "./ipag00303/ipag.ttf" #作品名部分のフォントのパス
    font_main = "./ipag00303/ipag.ttf" #その他のフォントのパス

    data = get_data(url)
    titles = list(data.keys())
    inList = True
    area_ = f'%%html\n<img src="../img/' + ''.join(Title.splitlines()) + '.png" usemap="#urlmap" />\n<map name="urlmap">'
    for x in range(ceil((len(titles) + 1) / 6)):
        for y in range(6):
            i = x * 6 + y - 1
            tmp = template.copy()
            if i == -1:
                tmp = Image.open('./assets/template.png').convert("RGB")
                font = ImageFont.truetype(font_main, 20)
                draw = ImageDraw.Draw(tmp)
                draw.text((2, 2), Title, (96, 167, 200), font=font, spacing=1)
                tmp = np.array(tmp)
            elif i < len(titles):
                area_ += "\n " + area(x, y, data[titles[i]]["href"])
                for kw in aimsize.keys():
                    if kw == "タイトル":
                        case = 1
                        hopt = 1
                    elif kw == "放送スケジュール":
                        case = 2
                        hopt = 3
                    elif kw == "原作":
                        case = 3
                        hopt = 2
                    else:
                        case = 0
                        if kw == "制作元請":
                            hopt = 2
                        else:
                            hopt = 6
                    mojiire(titles[i] if kw == "タイトル" else data[titles[i]][kw],
                            font_title if kw == "タイトル" else font_main, tmp,
                            aimsize[kw], aimpoint[kw], case, hopt)
                try:
                    img = Image.open(
                        BytesIO(get(
                            data[titles[i]]["img"]).content)).convert("RGB")
                    gray_image = cv2.cvtColor(np.array(img),
                                              cv2.COLOR_BGR2GRAY)
                    faces = classifier.detectMultiScale(gray_image)
                    h, w = img.height, img.width
                    if len(faces):
                        x_, y_ = (
                            np.r_[[faces[:, 3]**2 /
                                   (faces[:, 3]**2).sum()]].T *
                            (faces[:, :2] + faces[:, 2:] * .5)).sum(axis=0,
                                                                    dtype=int)
                    else:
                        x_, y_ = 0.5 * w, 0.45 * h
                    if w > 1.5 * h:
                        cropped_image = img.crop(
                            (max(0, int(x_ - .75 * h)) -
                             max(0,
                                 int(x_ + .75 * h) - w), 0,
                             min(w, int(x_ + .75 * h)) +
                             max(0, -int(x_ - .75 * h)), h))
                    else:
                        cropped_image = img.crop(
                            (0, max(0, int(y_ - (1 / 3) * w)) -
                             max(0,
                                 int(y_ + (1 / 3) * w) - h), w,
                             min(h, int(y_ + (1 / 3) * w)) +
                             max(0, -int(y_ - (1 / 3) * w))))
                    tmp = np.array(tmp)
                    tmp[:103, :-1] = np.array(cropped_image.resize((157, 103)))
                except Exception as e:
                    print(e)
            elif inList:
                foundation = np.array(template)
                foundation[20:, :10] = 0
                foundation[:2] = 0
                tmp = np.array(
                    Image.fromarray(foundation).filter(
                        ImageFilter.GaussianBlur(10.0)))
                inList = False
            else:
                foundation = np.array(template)
                foundation[:2] = 0
                tmp = np.array(
                    Image.fromarray(foundation).filter(
                        ImageFilter.GaussianBlur(10.0)))
            try:
                line = np.r_["1", line, tmp]
            except:
                line = tmp.copy()
        try:
            image = np.r_["0", image, line]
        except:
            image = line.copy()
        del line
    
    result, dst_data = cv2.imencode('.png', image)
    base64str = base64.b64encode(dst_data)
    title = ''.join(Title.splitlines())
    #filename = uuid.uuid4()
    #file_path = f"./img/{filename}.png"
    #plt.imsave(file_path, image)
    print(area_ + "\n</map>")
    return base64str
from flask import Flask, request, render_template,send_file
import requests as r
def download(url,s,e):
    re=r.get(url)
    with open("./static/img/qndxx/"+s+e+".jpg","wb+") as f:
        f.write(re.content)

def get_chinese(s):
    digit = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
    return digit[s]


    

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def fake_pic():
    s = str(request.form['s'])
    e = str(request.form['e'])
    if (not (0<int(s)<20 or 0<int(e)<20)) or s=="" or e=="":
        return  render_template('index.html',message="错误的查询范围。")
    elif int(s)<3:
        return render_template('index.html',message="前两季暂时没有收录。")
    convert=['0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    url=r"http://h5.cyol.com/special/daxuexi/daxuexi"+s+convert[int(e)]+e+r"/images/end.jpg"
    download(url,s,e)
    return render_template('fake_pic.html', pic_src='img/qndxx/'+s+e+'.jpg',s=get_chinese(s),e=e)   

if __name__ == '__main__':
    app.run()
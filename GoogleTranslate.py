import requests,execjs,re

class Py4Js():     
	def __init__(self):  
		self.ctx=execjs.compile(""" 
		function TL(a) {
			var k="";
			var b=406644;
			var b1=3293161072;
			
			var jd=".";
			var $b="+-a^+6";
			var Zb="+-3^+b+-f";
			for (var e=[], f=0, g=0; g < a.length; g++) {
				var m=a.charCodeAt(g);
				128 > m ? e[f++]=m : (2048 > m ? e[f++]=m >> 6 | 192 : (55296==(m & 64512) && g + 1 < a.length && 56320==(a.charCodeAt(g + 1) & 64512) ? (m=65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
				e[f++]=m >> 18 | 240,
				e[f++]=m >> 12 & 63 | 128) : e[f++]=m >> 12 | 224,
				e[f++]=m >> 6 & 63 | 128),
				e[f++]=m & 63 | 128)
			}
			a=b;
			for (f=0; f < e.length; f++) a +=e[f],
			a=RL(a, $b);
			a=RL(a, Zb);
			a ^=b1 || 0;
			0 > a && (a=(a & 2147483647) + 2147483648);
			a %=1E6;
			return a.toString() + jd + (a ^ b)
		};
		function RL(a, b) {
			var t="a";
			var Yb="+";
			for (var c=0; c < b.length - 2; c +=3) {
				var d=b.charAt(c + 2),
				d=d >=t ? d.charCodeAt(0) - 87 : Number(d),
				d=b.charAt(c + 1)==Yb ? a >>> d: a << d;
				a=b.charAt(c)==Yb ? a + d & 4294967295 : a ^ d
			}
			return a
		}
	""")  
		  
	def getTk(self,text):  
		return self.ctx.call("TL",text)  
	 
def translate(content,types=''):
	js=Py4Js()
	tk=js.getTk(content)
	if len(content)>4891:
		print("字符长度超过限制！")
		return
	param={'tk': tk, 'q': content}
	urlDic={'en_ch':"https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2",'ch_en':"https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2"}
	if types:
		try:url=urlDic[types]
		except KeyError:
			print('Error: types can only be ch_en or en_ch')
			sys.exit(0)
	elif not re.search('^[\u4e00-\u9fa5]+$',content):#英译中
		url=urlDic['en_ch']
	elif not re.search('^[a-zA-Z]+$',content):#中译英
		url=urlDic['ch_en']
	else:url=urlDic['en_ch']
	r=requests.get(url,params=param,proxies={'http':'http://127.0.0.1:7890','https':'http://127.0.0.1:7890'})
	result=''
	for i in range(len(r.json()[0])):
		if r.json()[0][i][0]:
			result+=r.json()[0][i][0]
	return result
	  
if __name__=="__main__": 
	content="Beautiful is better than ugly. Explicit is better than implicit.Simple is better than complex. Complex is better than complicated. "     
	print(translate(content))

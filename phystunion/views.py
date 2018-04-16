#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from django.http import HttpResponse,Http404,StreamingHttpResponse
import phystunion.models as mo
from django.template import Context
import os
import codecs

def Begin(request):
	return render(request,'manage.html',{})

def Manage(request,function):
     return render(request,'Result.html',eval(function))

def Init():
	initlist=['Section','News','Activity','Resource']
	namelist=[]
	try:
		for name in initlist:
			for parent,dirnames,filenames in os.walk(os.path.dirname(os.path.abspath(__file__).replace('views.py','../static/'+name+'/'))):
				for filename in  filenames:
					#namelist.append(filename)
					eval('Read'+name+'("'+filename+'")')
		return {'result':'Succeed!','ps':'Finish'}
	except Exception as e:
		return {'result':'Fail!','ps':str(e)}

def ReadNews(news):
	try:
		with codecs.open(os.path.abspath(__file__).replace('views.py','../static/News/'+news+'/'+news+'.txt'),'r','utf-8') as fp:
			ftext=fp.readlines()
			img=[]
			sty=[]
			for image in ftext[3:5]:
				img.append("/static/News/"+news+'/'+image)
				
			aut='<p align=\"center\">作者:'+ftext[1].split('#')[0].replace(' ','&nbsp;')+'</p>'
			if len(ftext[1].split('#'))>1 :
				aut=aut+'<p align=\"center\">编辑:'+ftext[1].split('#')[1].replace(' ','&nbsp;')+'</p>'
			new=mo.News(
					name=news,
					title=ftext[0],
					author=aut,
					timestamp=ftext[2],
					image1=img[0],
					image2=img[1],
					email=ftext[5],
					text='<p>'+'</p><p>'.join(ftext[6:])+'</p>',
					url='../News/'+news
				)
			new.save()
			
			return {'result':'Succeed!','ps':'Finish.'}
	except Exception as e:
		return {'result':'Fail!','ps':str(e)}

def ReadSection():
	sections=(str("keji"),str("wenti"),str("waixuan"),str("shijian"),str("zongban"))
	if(len(mo.Section.objects.all())>0):
		mo.Section.objects.all().delete()
	
	for section in sections:
		#try:
			with codecs.open(os.path.abspath(__file__).replace("views.py","../static/Section/"+section+"/"+section+".txt"),"r",'utf-8') as fp:
                            text=fp.readlines()
                            #return {'result':'1','ps':'2'}
                            sec=mo.Section(
                                Name=text[0],
                                image='/static/Section/'+section+'/'+text[1],
                                host=text[2],
                                sub=text[3].replace('#','  '),
                                email=text[4],
                                introduction='<p></p><p>'.join(text[5:])+'</p>'
                                )
                            sec.save()
		#except Exception as e:
		#	return {'result':'Fail!','ps':str(e)}
	
	return {'result':'Succeed!','ps':'Finish.'}

def ReadActivity(activity):
	try:
		with open(os.path.abspath(__file__).replace('views.py','../static/Activity/'+activity+'/'+activity+'.txt'),'r') as fp:
			text=fp.read().split('\n')
			act=mo.Activity(
				name=activity,
				title=text[0],
				timestamp=text[1],
				image="/static/Activity/"+activity+'/'+text[2],
				email=text[3],
                                introduction='<p></p><p>'.join(text[4:])+'</p>',
				url='Activity/'+activity
				)
			act.save()
			return {'result':'Succeed!','ps':'Finish!'}
	except Exception as e:
		return {'result':'Fail!','ps':str(e)}

def ReadResource():
    vedio=['mp4','mkv','rm','rmvb','3gp','avi','wmv','mp3','wav','wma','ogg','ape','acc','cda','flac','aac']
    picture=['bmp','jpg','gif','jpeg','tiff','psd','png','swf','svg','dxf''eps']
    if(len(mo.Resource.objects.all())>0):
        mo.Resource.objects.all().delete()

    (files,)=os.walk(os.path.dirname(os.path.abspath(__file__).replace('views.py','../static/Resource/')))
    
    for resource in list(files)[2]:
        sty='Defualt'
        try:
            nam=resource
            if resource.split('.')[-1] in vedio:
                ty='vedio'
            elif resource.split('.')[-1] in picture:
                ty='picture'
            else:
                ty='doc'
                sty=resource.split('@')[0]
                nam=resource.split('@')[-1]
                                        
            res=mo.Resource(
                name=nam.split('.')[0].replace('_',' '),
                type=ty,
                style=sty,
                url='../static/Resource/'+resource
                )
            res.save()
        except Exception as e:
            return {'result':'Fail!','ps':str(e)}
    return {'result':'Succeed!','ps':'Finish.'}

def DeleteResource(resource):
	vedio=['mp4','mkv','rm','rmvb','3gp','avi','wmv','mp3','wav','wma','ogg','ape','acc','cda','flac','aac']
	picture=['bmp','jpg','gif','jpeg','tiff','psd','png','swf','svg','dxf''eps']
	try:
		mo.Resource.get(name=resource).delete()
		os.remove(os.path.abspath(__file__).replace('views.py','../static/Resource/'+resource))
		return {'result':'Succeed!','ps':'Finish.'}
	except Exception as e:
		return {'result':'Fail!','ps':str(e)}

def DeleteNews(news):
	try:
		mo.News.objects.get(name=news).delete()
		for parent,dirnames,filenames in os.walk(os.path.dirname(os.path.abspath(__file__).replace('views.py','../static/News/'+news))):
			for filename in  filenames:
				os.remove(os.path.abspath(__file__).replace('views.py','../static/News/'+news+'/'+filename))
		os.rmdir(os.path.abspath(__file__).replace('views.py','../static/News/'+news))
		return {'result':'Succeed!','ps':'Finish.'}
	except Exception as e:
		return {'result':'Fail!','ps':str(e)}

def DeleteActivity(activity):
    try:
        mo.News.objects.get(name=activity).delete()
        for parent,dirnames,filenames in os.walk(os.path.dirname(os.path.abspath(__file__).replace('views.py','../static/Activity/'+activity))):
            for filename in  filenames:
                os.remove(os.path.abspath(__file__).replace('views.py','../static/Activity/'+activity+'/'+filename))
            os.rmdir(os.path.abspath(__file__).replace('views.py','../static/Activity/'+activity))
            return {'result':'Succeed!','ps':'Finish.'}
    except Exception as e:
        return {'result':'Fail!','ps':str(e)}

def NewsList(request):
    return render(request,'Newslist.html',{'ActList':mo.News.objects.all(),'ActList2':mo.News.objects.all()})

def ActivityList(request):
	return render(request,'Activitylist.html',{'ActivityList':mo.Activity.objects.all()})
	
def ResourceList(request):
	return render(request,'Resourcelist.html',{'VedioList':mo.Resource.objects.filter(type='vedio'),'PictureList':mo.Resource.objects.filter(type='picture'),'DocList':mo.Resource.objects.filter(type='doc')})
	
def Home(request):
	return render(request,'Home.html',{})
	
def News(request,news):
	return render(request,'News.html',{'news':mo.News.objects.get(name=news),})
	
def Activity(request,activity):
	return render(request,'Activity.html',{'activity':mo.Activity.objects.get(name=activity)})
	
def Section(request,section):
#    return render(request,'Result.html',{'result':section,'ps':'1'})
    return render(request,'Section.html',{'sec':mo.Section.objects.get(Name__icontains=section)})

def DownloadFile(request,filename):
	response=StreamingHttpResponse(ReadFile(os.path.abspath(__file__).replace('views.py','../static/Resource/'+filename)))
	response['Content-Type']='application/octet-stream'
	response['Content-Disposition']='attachment;filename="{0}"'.format(filename)
	return response

def ReadFile(filename,chunk_size=1024):
	with open(filename,'rb') as f:
		while True:
			c=f.read(chunk_size)
			if c:
				yield c
			else:
				break

def Mail(request,subject,name,phone,email,studentid,tomail):
        #qq='3038796649'
        #qqpswd='授权码'

        qq='3185258352'
        qqpswd='jezusuyegdzrdhfb'
        tomail='1367190098@qq.com'
        me=subject+'<'+qq+'@qq.com>'
        if subject=='意见反馈' :
            studentid=studentid.split('@')[0]+'</p><p>Suggestion:'+studentid.split('@')[1]

        context='<p>Name:'+name+'</p><p>Email:'+email+'</p><p>Student ID:'+studentid+'</p><p>Phone:'+phone+'</p>'
	
        msg = MIMEText(context,'html','utf-8')
        msg['Subject'] = Header(subject,'utf-8')
        msg['From'] = me
        msg['To'] = ','+email
        
        try:
            server=smtplib.SMTP_SSL("smtp.qq.com",465)
            server.login(qq+'@qq.com',qqpswd )
            server.sendmail(me,tomail,msg.as_string())
            server.quit()
            return render(request,'Result.html',{'result':'Succeed!','ps':'Thanks!'})
        except Exception as e:
            return render(request,'Result.html',{'result':'Fail!','ps':'Pleause send mail to '+tomail+' by yourself. Thanks.'})


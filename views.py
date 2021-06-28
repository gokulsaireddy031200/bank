from django.shortcuts import render

# Create your views here.
import requests

from django.template import loader 
from django.http import HttpResponse 
from django.http import JsonResponse


from django.views.generic import TemplateView,ListView

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core import serializers

from django.template.loader import render_to_string


def pagExample(request):
	url='https://gokulapi.herokuapp.com/api/branches/?q=Hyderabad&limit=10&offset=0'
	response=requests.get(url)
	res=response.json()

	p=Paginator(res,3)
	page_num=request.GET.get('page',1)
	try:
		page=p.page(page_num)  # desired page number we want 
	except EmptyPage:
		page=p.page(1)
	context={'sets':page}  # can also send whole res


	return render(request,'main3.html',context)

def bookmarks(request):
	return render(request,'testing.html',{})

def get_records(request):
	
	url_parameter = request.GET.get("q",'Delhi')  # default is set to delhi
	print(request,url_parameter)
	ctx={}
	
	if url_parameter and url_parameter!='none':
		
		url='https://gokulapi.herokuapp.com/api/branches/?q='+url_parameter+'&limit=500' +'&offset=0'
		response=requests.get(url)
		
		artists = response.json()

	else:
		artists = {}

	ctx["data"] = artists
	
	if request.is_ajax():
		
		
		
		data_dict = {"data": artists,'q':url_parameter}  #list of jsons/dicts
		
		return JsonResponse(data=data_dict, safe=False)
		
def table_view(request):
	ctx = {}
	url_parameter = request.GET.get("q")
	print(url_parameter,'asd')
	if url_parameter:
		url='https://gokulapi.herokuapp.com/api/branches/?q='+url_parameter+'&limit=10&offset=0'
		response=requests.get(url)
		artists = response.json()

	else:
		artists = {}
	ctx["data"] = artists
	
	flg=request.GET.get('flg',None)
	if request.is_ajax() or flg:
		p=Paginator(artists,3)  # shd be var
		
		page_num=request.GET.get('page',1)
		page_num=int(page_num)

		try:
			page=p.page(page_num)  # desired page number we want 
		except EmptyPage:
			page=p.page(1)
		
		html = render_to_string(
		template_name="result.html", 
		context={"sets": page,'query':url_parameter} )
		

	
		data_dict = {"html_from_view": html,'curr_page':page_num,'maxi':p.num_pages}  #list of jsons/dicts
		
		return JsonResponse(data=data_dict, safe=False)
	
	return render(request, "final.html", context=ctx)




class Testing(ListView):
	
	paginate_by=3
	context_object_name='context'
	template_name='testing.html'

	#queryset=[{1:'sd',2:'asdf'}]   # static data
	
	
	def get_queryset(self):
		key=self.kwargs['key']
		print(key)
		urlkey=key.upper()
		url='https://gokulapi.herokuapp.com/api/branches/?q='+urlkey+'&limit=10&offset=0'
		response=requests.get(url)
		res=response.json()
		return res
	
	# app/<model we specify here>_list.html


def ajaxHtml(request):
	urlkey=request.GET.get('search_element',None)
	if(urlkey):
		url='https://gokulapi.herokuapp.com/api/branches/?q='+urlkey+'&limit=10&offset=0'
		response=requests.get(url)
		res=response.json()
		res={ 'result':res} 
	else:
		res={}
	return JsonResponse(res)


def testing(request):
	temp=loader.get_template('main2.html')
	return HttpResponse( temp.render() )




def cacheReq(request,key):
	# key is got from request

	urlkey=key.upper()
	url='https://gokulapi.herokuapp.com/api/branches/?q='+urlkey+'&limit=10&offset=0'
	response=requests.get(url)
	res=response.json()
	

	if( not response  or response.status_code==404):
		return HttpResponse('Not Found')
	return HttpResponse(response)


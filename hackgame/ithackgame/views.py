from django.shortcuts import get_object_or_404, render, redirect
from .models import Board, Comment, Notice
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import YourModelForm
def index(request):
    # https://yeko90.tistory.com/entry/django-%EA%B8%B0%EC%B4%88-%ED%8E%98%EC%9D%B4%EC%A7%95-%EC%B2%98%EB%A6%ACpagination-%EB%A7%88%EC%8A%A4%ED%84%B0-%ED%95%98%EA%B8%B0
    post_list = Board.objects.all().order_by('-id')
    page = request.GET.get('page')
    a = "전체게시판"
    paginator = Paginator(post_list, 16)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    print(page_obj)
    for i in  page_obj:
        print(i)
    return render(request,'naver_clone/index.html',{'post_list':post_list, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range,"a":  a })



    #board_model = Board.objects.filter(id=number)

def Boardindex(request, number):
    # 'get_object_or_404' 함수를 사용하여 특정 'id' 값을 가진 레코드를 조회
    #board_model = get_object_or_404(Board, id=number)
    if request.user.is_authenticated:
        username = request.user.username
        print(1)
    else:
        return render(request, 'naver_clone/login.html')
    board = get_object_or_404(Board, id=number)
    comment = Comment.objects.filter(lecture = board, parent_comment=None)

    if request.method == "POST" :
        parent_comment_id = request.POST.get('parent_comment_id')
        print(parent_comment_id)
        if parent_comment_id is not None:
            relcm = request.POST['relcm']
            parent_comment = get_object_or_404(Comment, id=parent_comment_id)
            Comment.objects.create(lecture=board, comment=relcm, user=username, parent_comment=parent_comment)
        else:
            cm = request.POST['cm']
            Comment.objects.create(lecture=board, comment=cm, user=username)
    return render(request, 'naver_clone/lookup.html', {'board': board, 'comment':comment ,'username':username})

def ItisNotice(request):
    # 'get_object_or_404' 함수를 사용하여 특정 'id' 값을 가진 레코드를 조회
    #board_model = get_object_or_404(Board, id=number)
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return render(request, 'naver_clone/login.html')
    board = get_object_or_404(Notice, id=1)
    
    return render(request, 'naver_clone/Notice.html', {'board': board,'username':username})

def login(request):
    if request.method == "POST":
        id = request.POST['id']
        pwd = request.POST['pwd']
        
        user = auth.authenticate(request, username=id, password = pwd)
        if user is None:
            print("틀림")
            return redirect("/login")
        else :
            auth.login(request, user)
            return redirect("/")
    return render(request,'naver_clone/login.html')

def sign(request):
    if request.method == "POST":
        id = request.POST['id']
        pwd = request.POST['pwd']
        email = request.POST['email']
        print(id)
        try:
            User.objects.create_user(username=id, password=pwd, email=email)
        except:
            return render(request,'naver_clone/sign.html')
        return redirect("/")

    return render(request,'naver_clone/sign.html')

def logout(request):
    auth.logout(request)
    return redirect("/")


def comment_remove(request,pk):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return render(request, 'naver_clone/index.html')
    commentfordelete = Comment.objects.get(pk=pk)
    if commentfordelete.user == username or request.user.is_staff :
        commentfordelete.comment ="has been deleted"
        commentfordelete.save()
    return redirect("/")

def docterlist(request, name):
    post_list = Board.objects.filter(name = name).all()
    page = request.GET.get('page')
    paginator = Paginator(post_list, 16)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    print(page_obj)
    for i in  page_obj:
        print(i)
    return render(request,'naver_clone/index.html',{'post_list':post_list, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range, "a":name})

#!!!!!!!!!!!!!!!!!!!!!!!!!!

def write(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            post = form.save()
            post.name = request.user.username
            post.save()
            return redirect('/')  # 적절한 URL로 리다이렉트
        if  request.user.is_authenticated is False:
            return redirect('/')
    else:
        form = YourModelForm()

    return render(request, 'naver_clone/a.html', {'form': form})


def free(request):
    post_list = Board.objects.filter(category="free")
    page = request.GET.get('page')
    a = "자유게시판"
    paginator = Paginator(post_list, 16)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    print(page_obj)
    for i in  page_obj:
        print(i)
    return render(request,'naver_clone/index.html',{'post_list':post_list, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range, 'a':a})
def pc(request):
    post_list = Board.objects.filter(category="pc")
    page = request.GET.get('page')
    a = "pc게임"
    paginator = Paginator(post_list, 16)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    print(page_obj)
    for i in  page_obj:
        print(i)
    return render(request,'naver_clone/index.html',{'post_list':post_list, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range, 'a':a})
def moblie(request):
    post_list = Board.objects.filter(category="moblie")
    page = request.GET.get('page')
    a = "모바일게임"
    paginator = Paginator(post_list, 16)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    print(page_obj)
    for i in  page_obj:
        print(i)
    return render(request,'naver_clone/index.html',{'post_list':post_list, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range, 'a':a})
def embed(request):
    post_list = Board.objects.filter(category="embed")
    page = request.GET.get('page')
    a = "임베디드게임"
    paginator = Paginator(post_list, 16)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    print(page_obj)
    for i in  page_obj:
        print(i)
    return render(request,'naver_clone/index.html',{'post_list':post_list, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range, 'a':a})
def anti(request):
    post_list = Board.objects.filter(category="anti")
    page = request.GET.get('page')
    a = "안티포렌식"    
    paginator = Paginator(post_list, 16)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    custom_range = range(leftIndex, rightIndex+1)
    print(page_obj)
    for i in  page_obj:
        print(i)
    return render(request,'naver_clone/index.html',{'post_list':post_list, 'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range, 'a':a})
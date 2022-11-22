from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse 
from .models import Post
#کتابخونه رندر و گت آپ 404 رو ایمپورت میکنه ک در توابع فراخونی بشه
# کتاب خونه اچ تی ام ال رو ایمپورت میکنه تا در توابع فراخونی بشه
# از قسمت مدل ها کلاس پست رو ایمپورت میکنه تا در تابع پایین فراخوانی شود

# def index (request):
    #(درخواستی)تعریف تابع ایندس
    # return render (request, 'blog/index.html')
    #بطور بازگشتی فراخوانی میشه به اچ تی ام ال ایندس
def index (request):
    post = Post.objects.filter(status="p").order_by("-publish")
    context = {'post':post}
    return render (request , 'blog/index.html' , context)
    #(درخواستی)تعریف تابع پست 
    #تابع پست رو با پست هایی که استاتوسشون پی هست برابر قرار میدهد
    #یک دیکشنری به اسم پست تعریف میکنیم که هرجا از اسم پست استفاده کنیم پست هامون رو نمایش بده
    #بطور بازگشتی فراخوانی میشه به اچ تی ام ال پست
def post(request , slug):
    detail = get_object_or_404(Post , slug=slug , status="p")
    context ={
        'detail':detail
    }
    return render(request , 'blog/post.html' , context)
def about (request) :
    return render (request,"blog/about.html" )
    #(درخواستی)تعریف تابع ابوت 
    #بطور بازگشتی فراخوانی میشه به اچ تی ام ال ابوت
def contact (request):
    return render(request,"blog/contact.html")  
    #(درخواستی)تعریف تابع کانتکت 
    #بطور بازگشتی فراخوانی میشه به اچ تی ام ال کانتکت  
   
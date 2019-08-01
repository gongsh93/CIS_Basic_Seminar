import sqlite3
from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, 'form.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    conn = sqlite3.connect("users")   
    cur = conn.cursor()

    sql = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "';"
    print(sql)
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()

    if result:
        logined = result[0]
        return render(request, "result.html", {'logined': logined})
    else:
        return render(request, "result.html")


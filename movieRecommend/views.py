from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from django.middleware.csrf import get_token
from . import models
import csv
from pymysql import connect

# Create your views here.



def get_csrf_token(request):
    csrf_token = get_token(request)  # 获取csrf_token的值
    return JsonResponse({'token': csrf_token})



class LoginView(View):
    def post(self, request):
        user = models.User
        username = request.POST.get('username')
        password = request.POST.get('password')
        results = user.objects.filter(username=username)
        #结果为0
        if len(results) == 0:
            content = {'state':0, 'message':'用户不存在'}
        else:
            for i in results:
                if i.username == username and i.password == password:
                    content = {'state':1, 'message': '登录成功'}
                else:
                    content = {'state':2, 'message': '密码错误'}

        return JsonResponse(content)


    def get(self, request):
        return JsonResponse({'name': '166666', 'age': 1})


class RegisterView(View):
    def post(self, request):
        user = models.User
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #查询是否已经存在该用户
        results = user.objects.filter(username=username)
        #结果为0
        userNum = user.objects.last().id
        if len(results) != 0:
            content = {'state':0, 'message':'用户已经存在'}
        else:
            if password1 != password2:
                content = {'state': 0, 'message': '用户二次密码输入不同'}
            else:
                user.objects.create(id=userNum+1,username=username, password=password1)
                content = {'state': 1, 'message': '用户创建成功'}
        return JsonResponse(content)


def test(request):
    #  建立链接
    conn = connect(host='localhost', port=3306, db='movierec', user='root', password='123456', charset='utf8')
    # 获取游标
    cur = conn.cursor()
    title = '我是新测试人员'
    # movie = models.movie
    # movie.objects.create(movieid=1, moviename='野狼 Hombre', rating=8, poster='https://img3.doubanio.com/lpic/s2555801.jpg',\
    #                      languages='英语', year=1967, summary='约翰·罗塞尔自幼是老罗塞尔先生从战俘中带回来并抚养他长大的，但是他生性豪放不羁，又回到土著人的中间，在茫茫山野间生活。直到老人去世时，留给他自己的一处房子，那里现在是一家旅馆，由能乾的杰茜经营。老人希望他回到白人中间，用英语思考问题。他却将房子变卖，杰茜只好回家。他们一行人从旅馆出发，一同乘坐马车的还有医生夫妇以及强行霸占别人位置的弗兰克。他们担心路上不安全，改走一条废弃的山路，却遭到一伙人的袭击，原来弗兰克是劫匪中的成员，目的是医生携带的不义之财。这伙人打破了他们的水袋，劫走了医生的妻子做人质。匆忙间，劫匪们遗失了钱袋，他们要用医生妻子换钱袋。胆小的医生不敢前去，一任妻子在炎炎烈日下呻吟。带领大家对付劫匪的罗塞尔冒死前往，在腹背受敌的不利情况下，只身对敌，为了营救他人与匪徒同归于尽。', \
    #                      duration='111', rating_people=145, percentage5=24, percentage4=53,percentage3=19,\
    #                      percentage2=2, percentage1=0)
    # results = movie.objects.filter(moviename='千钧一发 Nick of Time')
    # for i in results:
    #     print(i.languages)
    # with open('./data/刘澎的movie2.csv', 'r', encoding='utf-8') as f:
    #     rete = csv.reader(f)
    #     print(rete)
    #     for x in rete:
    #         print(x)
    #         # sql语句
    #         sql = "insert into movierecommend_movie values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #         print(sql)
    #         # 参数化方式传参
    #         row_count = cur.execute(sql, [int(x[0]), x[2], x[12], x[4], x[7], x[8], x[9]
    #             , x[10], x[11], x[13], x[14], x[15], x[16], x[17]])
    #         # 显示操作结果
    #         print("SQL语句影响的行数为%d" % row_count)
    # 打开文件，读取所有文件存成列表
    # with open('./data/导演.csv', 'r', encoding='utf-8') as f:
    #     rete = csv.reader(f)
    #     for i, x in enumerate(rete):
    #         print(x)
    #         # sql语句
    #         sql = "insert into movierecommend_directors values (%s,%s,%s)"
    #         print(i+1)
    #         print(sql)
    #         # 参数化方式传参
    #         row_count = cur.execute(sql, [int(i+1), x[1], int(x[0])])
    #         # 显示操作结果
    #         print("SQL语句影响的行数为%d" % row_count)

    # # 打开文件，读取所有文件存成列表
    # with open('./data/类别.csv', 'r', encoding='gb18030') as f:
    #     rete = csv.reader(f)
    #     for i, x in enumerate(rete):
    #         # sql语句
    #         sql = "insert into movierecommend_genre values (%s, %s,%s)"
    #         print(sql)
    #         # 参数化方式传参
    #         row_count = cur.execute(sql, [int(i+1), x[1], int(x[0])])
    #         # 显示操作结果
    #         print("SQL语句影响的行数为%d" % row_count)

    # # 打开文件，读取所有文件存成列表
    # with open('./data/评论.csv', 'r', encoding='utf-8') as f:
    #     rete = csv.reader(f)
    #     head = next(rete)
    #     for i, x in enumerate(rete):
    #         # sql语句
    #         sql = "insert into movierecommend_comments values (%s,%s,%s,%s,%s)"
    #         print(sql)
    #         # 参数化方式传参
    #         row_count = cur.execute(sql, [int(i+1), x[2], x[3], x[5],int(x[0])])
    #         # 显示操作结果
    #         print("SQL语句影响的行数为%d" % row_count)

    # # 打开文件，读取所有文件存成列表
    # with open('./data/演员.csv', 'r', encoding='utf-8') as f:
    #     rete = csv.reader(f)
    #     for i,x in enumerate(rete):
    #         # sql语句
    #         sql = "insert into movierecommend_casts values (%s, %s, %s)"
    #         print(sql)
    #         # 参数化方式传参
    #         row_count = cur.execute(sql, [int(i+1), x[1], int(x[0])] )
    #         # 显示操作结果
    #         print("SQL语句影响的行数为%d" % row_count)


    # # 打开文件，读取所有文件存成列表
    # with open('./data/国家.csv', 'r', encoding='utf-8') as f:
    #     rete = csv.reader(f)
    #     for i,x in enumerate(rete):
    #         # sql语句
    #         sql = "insert into movierecommend_nation values (%s, %s, %s)"
    #         print(sql)
    #         # 参数化方式传参
    #         row_count = cur.execute(sql, [int(i+1), x[1], int(x[0])] )
    #         # 显示操作结果
    #         print("SQL语句影响的行数为%d" % row_count)



    # # 统一提交
    # conn.commit()
    # # 关闭游标　
    # cur.close()
    # # 关闭连接
    # conn.close()
    #
    return HttpResponse('“{}”，数据添加成功'.format(title))

def search(request):
    # def post(self, request):
    #  建立链接
    conn = connect(host='localhost', port=3306, db='movierec', user='root', password='123456', charset='utf8')
    # 获取游标
    cur = conn.cursor()
    title = '我是新测试人员'
    # type = request.POST.get('type')
    # region = request.POST.get('region')
    # year = request.POST.get('year')
    sql = "select m.movieid from movierecommend_genre as g join movierecommend_nation as n on \
     g.movieid_id = n.movieid_id join movierecommend_movie as m \
     on g.movieid_id = m.movieid where g.genres ='{}' and n.nation = '{}' and m.year = '{}';".format('剧情', '美国','1967')
    print(sql)
    cur.execute(sql)

    results = cur.fetchall()
    print(results)
    for result in results:
        print(result[0])

    return HttpResponse('“{}”，数据添加成功'.format(title))
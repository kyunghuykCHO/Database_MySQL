# Main 
# Searching menu
# Search by title, actor, director, genre, year and country
# set ordering
# get movie info 1~4

import pymysql
import os
import time
import unicodedata

def Print(input_s="", max_size=20, fill_char=" "):
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)
def Print_line(input_s="", max_size=15, fill_char=" "):
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)


genre_list = ["드라마","판타지","서부","공포","모험","멜로/로맨스","스릴러","느와르","컬트","다큐멘터리","코미디","가족",
              "미스터리","전쟁","애니메이션","범죄","뮤지컬","SF","액션","무협","에로","서스펜스","서사","블랙코미디",
              "실험","공연실황"]

def open_db(): # Connection Open
    conn = pymysql.connect(host='localhost', user='root',
                           password='whrudgur', db='movie', unix_socket='/tmp/mysql.sock')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    return conn,cur
def close_db(conn,cur): # Connection Close
    cur.close()
    conn.close()

def show_menu(): # Showing Starting menu
    print("*****************")
    print("*  1) 영화검색  *")
    print("*  2) 종료하기  *")
    print("*****************")
def show_searching_menu(): # Showing Searching Option
    print("**********************")
    print("*  1) 영화제목 검색  *")
    print("*  2) 배우이름 검색  *")
    print("*  3) 감독이름 검색  *")
    print("*  4) 장르 검색      *")
    print("*  5) 제작년도 검색  *")
    print("*  6) 제작국가 검색  *")
    print("*  7) 프로그램 종료  *")
    print("**********************")
def show_genre_list(): # Showing genre List
    print("******************************************")
    print("*        영화 장르 리스트 입니다.        *")
    print("*   __________검색가능 장르____________  *")
    print("*  ┃드라마  판타지  서부  공포  모험   ┃ *")
    print("*  ┃멜로/로맨스  스릴러  느와르  컬트  ┃ *")
    print("*  ┃다큐멘터리  코미디  가족  미스터리 ┃ *")
    print("*  ┃전쟁  애니메이션  범죄  뮤지컬     ┃ *")
    print("*  ┃SF  액션  무협  에로  서스펜스     ┃ *")
    print("*  ┃서사  블랙코미디  실험  공연실황   ┃ *")
    print("*  ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣  *")
    print("******************************************")

def set_ordering(): # Ordering Set 
    while True:
        print("검색 정렬 조건입니다.")
        print("1) 가나다순 2) 년도순 3) 평점순")
        num = int(input("원하시는 조건에 맞는 번호를 입력하세요 : "))
        if num == 1:
            break
        elif num == 2:
            break
        elif num == 3:
            break
        else:
            os.system('clear')
            print("잘못된 입력입니다.")
            print("다시 입력해주세요.")
            time.sleep(1)
            os.system('clear')
    return num

def get_movie_info():
    os.system('clear')
    while True:
        print("**************************")
        print("*  1) 기본 정보          *") 
        print("*  2) 사진,동영상 (URL)  *")
        print("*  3) 평점,리뷰          *")
        print("*  4) 명대사             *")
        print("*  5) 프로그램 종료      *")
        print("**************************")
        num = int(input("원하시는 옵션을 선택하세요 : "))
        if 1<=num<=5:
            break
        else:
            os.system('clear')
            print("잘못된 입력입니다.")
            print("다시 입력해주세요.")
            time.sleep(1)
            os.system('clear')
    return num

def get_movie_info1(conn,cur,movie_title):
    os.system('clear')
    print("***************************************************")
    info_sql = """
        select m.movie_rate, m.date, m.people_rate, m.critic_rate, m.netizen_rate
        from Movie m
        where m.movie_title = "%s";
    """ %(movie_title)
    cur.execute(info_sql)
    print("* "+Print_line(" MOVIE RATE",max_size=5),Print_line(" MOVIE DATE",max_size=5),Print_line(" PEOPLE RATE",max_size=5),Print_line(" CRITIC RATE",max_size=5),Print_line(" NETIZEN RATE",max_size=5)+"  *")
    dics = cur.fetchone()
    row = list(dics.values())
    mv,md,pr,cr,nr = row
    print("* "+Print_line(mv,max_size=5),Print_line(md,max_size=5),Print_line("pr",max_size=5),Print_line(cr,max_size=5),Print_line(nr,max_size=5)+"  *")
    print("***************************************************")
    plot_sql = """
        select m.plot
        from Movie m
        where m.movie_title = "%s";
    """ %(movie_title)
    cur.execute(plot_sql)
    print("***************************************************")
    print("{0:^40}".format("PLOT"))
    dics = cur.fetchone()
    row = list(dics.values())
    print(row)
    print("***************************************************")
    genre_sql ="""
        select g.genre
        from genre g
        where g.movie_code=(select movie_code from movie where movie_title = "%s")
    """ %(movie_title)
    cur.execute(genre_sql)
    print("***************************************************")
    print("{0:^40}".format("GENRE"))
    dics = cur.fetchall()
    for i in dics:
        print(i.values(), end='\n')
    print("***************************************************")
    nation_sql ="""
        select n.nation
        from nation n
        where n.movie_code = (select movie_code from movie where movie_title = "%s");
    """ %(movie_title)
    cur.execute(nation_sql)
    print("{0:^40}".format("NATION"))
    dics = cur.fetchall()
    for i in dics:
        print(i.values(), end='\n')
    print("***************************************************")
    print("***************************************************")
    person_sql = """
        SELECT mp.person_name, mp.movie_role, mp.role
        FROM movie_person mp
        WHERE mp.movie_code=(select movie_code from movie where movie_title = "%s");
    """%(movie_title)
    cur.execute(person_sql)
    print("* "+Print_line(" NAME",max_size=5),Print_line(" ROLE IN MOVIE",max_size=5),Print_line(" ROLE",max_size=5)+"  *")
    dics = cur.fetchall()
    rows = []
    for i in dics:
        tmp = list(i.values())
        rows.append(tmp)
    for row in rows:
        n,rm,r = row
        print("* "+Print_line(n,max_size=5),Print_line(rm,max_size=5),Print_line(r,max_size=5)+"  *")
    print("***************************************************")

    select = int(input("배역 이름의 정보를 보고 싶으시면 1번, 아닐시 다른 숫자를 누르십시오 : "))
    if select == 1:
        actor_name = input("정보를 원하는 배우의 이름을 입력하시오 : ")
        actor_sql = """
            SELECT p.birth_year, p.nationality, p.person_photo
            FROM person p, movie_person mp, movie m 
            WHERE mp.movie_code=(select movie_code from movie where movie_title = "%s") AND mp.person_name = "%s" AND mp.person_code = p.person_code;
        """%(movie_title, actor_name)
        cur.execute(actor_sql)
        print("***************************************************")
        print("* "+Print_line(" BIRTH",max_size=9),Print_line(" NATIONALITY",max_size=5),Print_line(" PHOTO",max_size=5)+"  *")
        dic = cur.fetchone()
        row = []
        row.append(list(dic.values()))
        b,n,p = row
        print("* "+Print_line(b,max_size=9),Print_line(n,max_size=5),Print_line(p,max_size=5)+"  *")
        print("***************************************************")

    time.sleep(1)
def get_movie_info2(conn,cur,movie_title):
    os.system('clear')
    print("1)사진 2)동영상")
    num = int(input("입력하세요 : "))
    if num ==1:
        os.system('clear')
        start,end = 0,10
        while True:
            photo_sql = """
                SELECT p.photo_url
                FROM photo p
                WHERE p.movie_code = (select movie_code from movie where movie_title = "%s")
                LIMIT %d, %d;
            """ %(movie_title, start, end)
            cur.execute(photo_sql)
            print("***************************************************")
            print("{0:^40}".format("PHOTO URL"))
            print()
            dics = cur.fetchall()
            row = []
            for i in dics:
                tmp = list(i.values())
                row.append(tmp)
            for line in row:
                print(line)
            print("***************************************************")
            print("다음장으로 가길 원한다면 Y 혹은 y 를 누르십시오.")
            print("종료를 원하신다면 아무키나 누르십시오.")
            a = input("입력하세요. : ")
            if a=="Y" or a=="y":
                start+=10
            else:
                return
    elif num==2:
        os.system('clear')
        start = 0
        end = 10
        while True:
            video_sql = """
                SELECT v.video_url
                FROM video v
                WHERE v.movie_code = (select movie_code from movie where movie_title = "%s")
                LIMIT %d, %d;
            """ %(movie_title, start, end)
            cur.execute(video_sql)
            print("***************************************************")
            print("{0:^40}".format("VIEDO URL"))
            dics = cur.fetchall()
            row = []
            for i in dics:
                tmp = list(i.values())
                row.append(tmp)
            for line in row:
                print(line)
            print("***************************************************")
            print()
            print("다음장으로 가길 원한다면 Y 혹은 y 를 누르십시오.")
            print("종료를 원하신다면 아무키나 누르십시오.")
            a = input("다음장으로 가길 윈하면 Y 를 누르시오. : ")
            if a=="Y" or a=="y":
                start+=10
            else:
                return
def get_movie_info3(conn,cur,movie_title):
    os.system('clear')
    num = int(input("1) 평점 2) 리뷰"))
    if num == 1:
        start = 0
        while True:
            for i in range(10):
                rating_sql = """
                    SELECT r.user_id, r.star_rate, r.date, r.agree, r.disagree
                    FROM rating r
                    WHERE r.movie_code = (select movie_code from movie where movie_title = "%s")
                    LIMIT %d, 1;
                """ %(movie_title,start)
                print("***************************************************")
                print("* "+Print_line(" USER_ID",max_size=7),Print_line(" STAR_RATE",max_size=4),Print_line(" DATE",max_size=7),Print_line(" AGREE",max_size=4),Print_line(" DISAGREE",max_size=4)+"  *")
                cur.execute(rating_sql)
                rows = cur.fetchone()
                row = list(rows.values())
                user_id = row[0]
                ui, sr, d , a , dis = row
                print("* "+Print_line(ui,max_size=7),Print_line(sr,max_size=4),Print_line(d,max_size=7),Print_line(a,max_size=4),Print_line(dis,max_size=4)+"  *")
                print("***************************************************")
                text_sql = """
                    SELECT r.text
                    FROM rating r
                    WHERE r.movie_code = (select movie_code from movie where movie_title = "%s") AND r.user_id = "%s"
                    LIMIT %d,1;
                """ %(movie_title, user_id, start)
                print("{0:^40}".format("TEXT"))
                cur.execute(text_sql)
                rows = cur.fetchone()
                row = list(rows.values())
                print(row)
                start+=1
            print("다음장으로 가길 원한다면 Y 혹은 y 를 누르십시오.")
            print("종료를 원하신다면 아무키나 누르십시오.")
            a = input("다음장으로 가길 윈하면 Y 를 누르시오. : ")
            if a=="Y" or a=="y":
                continue
            else:
                return
    if num == 2:
        start = 0
        while True:
            for i in range(10):
                review_sql = """
                    SELECT r.user_id, r.star_rate, r.date, r.views, r.agree
                    FROM review r
                    WHERE r.movie_code = (select movie_code from movie where movie_title = "%s") 
                    LIMIT %d, 1;
                """ %(movie_title,start)
                print("***************************************************")
                print("USER ID, STAR_RATE, DATE, VIEWS, AGREE")
                print("* "+Print_line(" USER_ID",max_size=7),Print_line(" STAR_RATE",max_size=4),Print_line(" DATE",max_size=7),Print_line(" VIEWS",max_size=4),Print_line(" AGREE",max_size=4)+"  *")
                cur.execute(review_sql)
                dics = cur.fetchall()
                rows = []
                for i in dics:
                    tmp = list(i.values())
                    rows.append(tmp)
                for row in rows:
                    ui, sr, d , v, a = row
                    print("* "+Print_line(ui,max_size=7),Print_line(sr,max_size=4),Print_line(d,max_size=7),Print_line(v,max_size=4),Print_line(a,max_size=4)+"  *")
                print("* ---------------------------------------------------- *")
                    
                review2_sql = """
                    SELECT r.text
                    FROM review r
                    WHERE r.movie_code = (select movie_code from movie where movie_title = "%s") 
                    LIMIT %d, 1;
                """
                cur.execute(review2_sql)
                dics = cur.fetchall()
                row = []
                for i in dics:
                    tmp = list(i.values())
                    row.append(tmp)
                for line in row:
                    print(line)
                print("***************************************************")
                start+=1
            while True:
                print("1) 답글확인 2) 다음장 3) 종료")
                next = int(input("입력하세요 : "))
                if next == 1:
                    id = input("원하시는 유저ID를 입력하세요 : ")
                    s,e = 0,10
                    while True:
                        reply_sql = """
                            SELECT rp.text
                            FROM reveiw r, review_reply rp
                            WHERE r.review_code = rp.review_code AND r.user_id = "%s"
                            LIMIT %d,%d;
                        """ %(id, s, e)
                        print("***************************************************")
                        print("{}님의 글의 답글".format(id))
                        cur.execute(reply_sql)
                        dics = cur.fetchall()
                        row = []
                        for i in dics:
                            tmp = list(i.values())
                            row.append(tmp)
                        for line in row:
                            print(line)
                        print("***************************************************")
                        n = int(input("더 보시겠습니까? 1)예 2)아니오"))
                        if n == 1:
                            s+=10
                        else:
                            break
                    
                elif next == 2:
                    break
                else:
                    os.system('clear')
                    print("잘못된 입력입니다.")
                    print("다시 입력해주세요.")
                    time.sleep(1)
            if next ==1:
                break
            elif next ==2:
                continue
            else:
                return
def get_movie_info4(conn,cur,movie_title):
    os.system('clear')
    start,end = 0,10
    while True:
        quote_sql = """
            SELECT q.movie_role, q.user_id, q.date, q.agree, q.text
            FROM quote q
            WHERE q.movie_code = (select movie_code from movie where movie_title = "%s")
            LIMIT %d,%d; 
        """ %(movie_title,start,end)
        print("***************************************************")
        print("* "+Print_line(" MOVIEINROLE",max_size=7),Print_line(" USERID",max_size=7),Print_line(" DATE",max_size=7),Print_line(" AGREE",max_size=7),Print_line(" TEXT",max_size=17)+"  *")
        cur.execute(quote_sql)
        dics = cur.fetchall()
        rows = []
        for i in dics:
            tmp = list(i.values())
            rows.append(tmp)
        for row in rows:
            mv,ui,d,a,t = row
            print("* "+Print_line(mv,max_size=7),Print_line(ui,max_size=7),Print_line(d,max_size=7),Print_line(a,max_size=7),Print_line(t,max_size=17)+"  *")
        print("***************************************************")
        a = input("다음장으로 가길 윈하면 Y 를 누르시오. : ")
        if a=="Y" or a=="y":
            start+=10
        else:
            return
    
def search_by_title(movie_title, ordering_option): # 제목 검색 . 정렬순
    if ordering_option == 1:
        ordering = "movie_title"
    elif ordering_option == 2:
        ordering = "year"
    else :
        ordering = "movie_rate"
    os.system('clear')
    conn, cur = open_db()
    start, end = 0,10
    while True:
        title_sql = """
                SELECT m.movie_title, m.movie_code, m.%s
                FROM movie m
                WHERE m.movie_title LIKE '%s%%'
                ORDER BY %s
                LIMIT %d,%d;
            """ %(ordering, movie_title,ordering, start,end)
        cur.execute(title_sql)
        if ordering == "movie_title": o = " TITLE"
        elif ordering == "year": o = " YEAR"
        elif ordering == "netizen_rate": o = " RATE"
        print("***************************************************")
        print("* "+Print_line(" TITLE",max_size=20),Print_line(" CODE",max_size=7),Print_line(o,max_size=17)+"  *")
        dics = cur.fetchall()
        rows = []
        for i in dics:
            rows.append(list(i.values()))
        for row in rows:
            title, code, order = row    
            print("*  "+Print(title, max_size=20),Print(str(code), max_size=7),Print(" "+str(order),max_size=17)+" *")
        print("***************************************************")

        while True:
            print("1) 영화 정보 검색 2) 다음장")
            next = int(input("입력하세요 : "))
            if next == 1:
                code = input("정보를 원하는 영화의 번호를 입력하세요 : ")
                for i in range(len(rows)):
                    if rows[i][1] == code:
                        movie_title = rows[i][0]
                        break
                break
            elif next ==2:
                break
            else:
                os.system('clear')
                print("잘못된 입력입니다.")
                print("다시 입력해주세요.")
                time.sleep(1)
                os.system('clear')
        if next ==1:
            break
        elif next ==2:
            start+=10
    os.system('clear')
    print("{} 영화에 대해 검색합니다.".format(movie_title))
    time.sleep(1.5)
    os.system('clear')
    info_number = get_movie_info()
    
    if info_number == 1:
        get_movie_info1(conn,cur,movie_title)
    elif info_number == 2:
        get_movie_info2(conn,cur,movie_title)
    elif info_number == 3:
        get_movie_info3(conn,cur,movie_title)
    elif info_number == 4:
        get_movie_info4(conn,cur,movie_title)
    else:
        os.system('clear')
        print("검색 프로그램을 종료합니다.")
        exit()
    
    conn.commit()
    close_db(conn,cur)
    return
def search_by_actor(actor_name, ordering_option): # 배우 검색 , 정렬순
    if ordering_option == 1:
        ordering = "movie_title"
    elif ordering_option == 2:
        ordering = "year"
    else :
        ordering = "movie_rate"

    os.system('clear')
    conn, cur = open_db()
    start,end = 0,10
    while True:
        sql = """
            SELECT m.movie_title, m.movie_code, m.%s
            FROM Movie m, movie_person mp, person p
            WHERE p.person_name = "%s%%" AND m.movie_code = mp.movie_code AND mp.person_code = p.person_code 
            ORDER BY %s
            LIMIT %d,%d;
        """ %(ordering, actor_name,ordering, start,end)
        cur.execute(sql)
        rows = cur.fetchall()
        if ordering == "movie_title": o = " TITLE"
        elif ordering == "year": o = " YEAR"
        elif ordering == "netizen_rate": o = " RATE"
        print("***************************************************")
        print("* "+Print_line(" TITLE",max_size=20),Print_line(" CODE",max_size=7),Print_line(o,max_size=17)+"  *")
        dics = cur.fetchall()
        rows = []
        for i in dics:
            rows.append(list(i.values()))
        for row in rows:
            title, code, order = row    
            print("*  "+Print(title, max_size=20),Print(str(code), max_size=7),Print(" "+str(order),max_size=17)+" *")
        print("***************************************************")
        while True:
            print("1) 영화 정보 검색 2) 다음장")
            next = int(input("입력하세요 : "))
            if next == 1:
                code = input("정보를 원하는 영화의 번호를 입력하세요 : ")
                for i in range(len(row)):
                    if row[i][1] == code:
                        movie_title = row[i][0]
                        break
            elif next ==2:
                break
            else:
                os.system('clear')
                print("잘못된 입력입니다.")
                print("다시 입력해주세요.")
                time.sleep(1)
                os.system('clear')
        if next ==1:
            break
        elif next ==2:
            start+=10
    
    os.system('clear')
    print("{} 영화에 대해 검색합니다.".format(movie_title))
    time.sleep(1)
    os.system('clear')
    info_number = get_movie_info()
    if info_number == 1:
        get_movie_info1(conn,cur,movie_title)
    elif info_number == 2:
        get_movie_info2(conn,cur,movie_title)
    elif info_number == 3:
        get_movie_info3(conn,cur,movie_title)
    elif info_number == 4:
        get_movie_info4(conn,cur,movie_title)
    else:
        os.system('clear')
        print("검색 프로그램을 종료합니다.")
        exit()
    conn.commit()
    close_db(conn,cur)
    return
def search_by_director(director_name, ordering_option): # 감독 검색 , 정렬순
    if ordering_option == 1:
        ordering = "movie_title"
    elif ordering_option == 2:
        ordering = "year"
    else :
        ordering = "movie_rate"
    os.system('clear')
    conn, cur = open_db()
    start,end = 0,10
    while True:
        sql = """
            SELECT m.movie_title, m.movie_code, m.%s
            FROM Movie m, movie_person mp, person p
            WHERE p.person_name = "%s%%" AND m.movie_code = mp.movie_code AND mp.person_code = p.person_code
            ORDER BY %s 
            LIMIT %d,%d;
        """ %(ordering,director_name, ordering, start,end)
        cur.execute(sql)
        if ordering == "movie_title": o = " TITLE"
        elif ordering == "year": o = " YEAR"
        elif ordering == "netizen_rate": o = " RATE"
        print("***************************************************")
        print("* "+Print_line(" TITLE",max_size=20),Print_line(" CODE",max_size=7),Print_line(o,max_size=17)+"  *")
        dics = cur.fetchall()
        rows = []
        for i in dics:
            rows.append(list(i.values()))
        for row in rows:
            title, code, order = row    
            print("*  "+Print(title, max_size=20),Print(str(code), max_size=7),Print(" "+str(order),max_size=17)+" *")
        print("***************************************************")
        while True:
            print("1) 영화 정보 검색 2) 다음장")
            next = int(input("입력하세요 : "))
            if next == 1:
                code = input("정보를 원하는 영화의 번호를 입력하세요 : ")
                for i in range(len(row)):
                    if row[i][1] == code:
                        movie_title = row[i][0]
                        break
            elif next ==2:
                break
            else:
                os.system('clear')
                print("잘못된 입력입니다.")
                print("다시 입력해주세요.")
                time.sleep(1)
                os.system('clear')
        if next ==1:
            break
        elif next ==2:
            start+=10
                
    os.system('clear')
    print("{} 영화에 대해 검색합니다.".format(movie_title))
    time.sleep(1)
    os.system('clear')
    info_number = get_movie_info()
    
    if info_number == 1:
        get_movie_info1(conn,cur,movie_title)
    elif info_number == 2:
        get_movie_info2(conn,cur,movie_title)
    elif info_number == 3:
        get_movie_info3(conn,cur,movie_title)
    elif info_number == 4:
        get_movie_info4(conn,cur,movie_title)
    else:
        
        os.system('clear')
        print("검색 프로그램을 종료합니다.")
        exit()
    conn.commit()
    close_db(conn,cur)
    return
def search_by_genre(genre, ordering_option): # 감독 검색 , 정렬순
    if ordering_option == 1:
        ordering = "movie_title"
    elif ordering_option == 2:
        ordering = "year"
    else :
        ordering = "movie_rate"
    os.system('clear')
    conn, cur = open_db()
    start,end = 0,10
    while True:
        sql = """
            SELECT m.movie_title, m.movie_code, m.%s
            FROM Movie m, genre g
            WHERE m.movie_code = g.movie_code AND g.genre = "%s%%"
            ORDER BY %s
            LIMIT %d,%d;
        """ %(ordering, genre, ordering, start,end)
        cur.execute(sql)
        if ordering == "movie_title": o = " TITLE"
        elif ordering == "year": o = " YEAR"
        elif ordering == "netizen_rate": o = " RATE"
        print("***************************************************")
        print("* "+Print_line(" TITLE",max_size=20),Print_line(" CODE",max_size=7),Print_line(o,max_size=17)+"  *")
        dics = cur.fetchall()
        rows = []
        for i in dics:
            rows.append(list(i.values()))
        for row in rows:
            title, code, order = row    
            print("*  "+Print(title, max_size=20),Print(str(code), max_size=7),Print(" "+str(order),max_size=17)+" *")
        print("***************************************************")
        while True:
            print("1) 영화 정보 검색 2) 다음장")
            next = int(input("입력하세요 : "))
            if next == 1:
                code = input("정보를 원하는 영화의 번호를 입력하세요 : ")
                for i in range(len(row)):
                    if row[i][1] == code:
                        movie_title = row[i][0]
                        break
            elif next ==2:
                break
            else:
                os.system('clear')
                print("잘못된 입력입니다.")
                print("다시 입력해주세요.")
                time.sleep(1)
                os.system('clear')
        if next ==1:
            break
        elif next ==2:
            start+=10

    os.system('clear')
    print("{} 영화에 대해 검색합니다.")
    time.sleep(1)
    os.system('clear')
    info_number = get_movie_info()
    
    if info_number == 1:
        get_movie_info1(conn,cur,movie_title)
    elif info_number == 2:
        get_movie_info2(conn,cur,movie_title)
    elif info_number == 3:
        get_movie_info3(conn,cur,movie_title)
    elif info_number == 4:
        get_movie_info4(conn,cur,movie_title)
    else:
        
        os.system('clear')
        print("검색 프로그램을 종료합니다.")
        exit()
    
    conn.commit()
    close_db(conn,cur)
    return
def search_by_year(year, ordering_option): # 감독 검색 , 정렬순
    if ordering_option == 1:
        ordering = "movie_title"
    elif ordering_option == 2:
        ordering = "year"
    else :
        ordering = "movie_rate"
    os.system('clear')
    conn, cur = open_db()
    start,end = 0,10
    while True:
        sql = """
            SELECT m.movie_title, m.movie_code , m.%s
            FROM Movie m
            WHERE m.year = "%s%%"
            ORDER BY %s
            LIMIT %d,%d;
        """ %(ordering, year, ordering, start, end)
        cur.execute(sql)
        if ordering == "movie_title": o = " TITLE"
        elif ordering == "year": o = " YEAR"
        elif ordering == "netizen_rate": o = " RATE"
        print("***************************************************")
        print("* "+Print_line(" TITLE",max_size=20),Print_line(" CODE",max_size=7),Print_line(o,max_size=17)+"  *")
        dics = cur.fetchall()
        rows = []
        for i in dics:
            rows.append(list(i.values()))
        for row in rows:
            title, code, order = row    
            print("*  "+Print(title, max_size=20),Print(str(code), max_size=7),Print(" "+str(order),max_size=17)+" *")
        print("***************************************************")
        while True:
            print("1) 영화 정보 검색 2) 다음장")
            next = int(input("입력하세요 : "))
            if next == 1:
                code = input("정보를 원하는 영화의 번호를 입력하세요 : ")
                for i in range(len(row)):
                    if row[i][1] == code:
                        movie_title = row[i][0]
                        break
            elif next ==2:
                break
            else:
                os.system('clear')
                print("잘못된 입력입니다.")
                print("다시 입력해주세요.")
                time.sleep(1)
            os.system('clear')
        if next ==1:
            break
        elif next ==2:
            start+=10
            
    os.system('clear')
    print("{} 영화에 대해 검색합니다.")
    time.sleep(1)
    os.system('clear')
    info_number = get_movie_info()
    
    if info_number == 1:
        get_movie_info1(conn,cur,movie_title)
    elif info_number == 2:
        get_movie_info2(conn,cur,movie_title)
    elif info_number == 3:
        get_movie_info3(conn,cur,movie_title)
    elif info_number == 4:
        get_movie_info4(conn,cur,movie_title)
    else:
        
        os.system('clear')
        print("검색 프로그램을 종료합니다.")
        exit()
    
    conn.commit()
    close_db(conn,cur)
    return
def search_by_country(country, ordering_option): # 감독 검색 , 정렬순
    if ordering_option == 1:
        ordering = "movie_title"
    elif ordering_option == 2:
        ordering = "year"
    else :
        ordering = "movie_rate"
    os.system('clear')
    conn, cur = open_db()
    start,end = 0,10
    while True:
        sql = """
            SELECT m.movie_title, m.movie_code, m.ordering
            FROM Movie m, nation n
            WHERE m.movie_code = n.movie_code AND n.nation = "%s%%"
            ORDER BY %s
            LIMIT %d,%d;
        """ %(ordering, country, ordering, start,end)
        cur.execute(sql)
        if ordering == "movie_title": o = "TITLE"
        elif ordering == "year": o = "YEAR"
        elif ordering == "netizen_rate": o = "RATE"
        print("***************************************************")
        print("* "+Print_line(" TITLE",max_size=20),Print_line(" CODE",max_size=7),Print_line(o,max_size=17)+"  *")
        dics = cur.fetchall()
        rows = []
        for i in dics:
            rows.append(list(i.values()))
        for row in rows:
            title, code, order = row    
            print("*  "+Print(title, max_size=20),Print(str(code), max_size=7),Print(" "+str(order),max_size=17)+" *")
        print("***************************************************")
        while True:
            print("1) 영화 정보 검색 2) 다음장")
            next = int(input("입력하세요 : "))
            if next == 1:
                code = input("정보를 원하는 영화의 번호를 입력하세요 : ")
                for i in range(len(row)):
                    if row[i][1] == code:
                        movie_title = row[i][0]
                        break
            elif next ==2:
                break
            else:
                os.system('clear')
                print("잘못된 입력입니다.")
                print("다시 입력해주세요.")
                time.sleep(1)
            os.system('clear')
        if next ==1:
            break
        elif next ==2:
            start+=10
            
    os.system('clear')
    print("{} 영화에 대해 검색합니다.")
    time.sleep(1)
    os.system('clear')
    info_number = get_movie_info()
    
    if info_number == 1:
        get_movie_info1(conn,cur,movie_title)
    elif info_number == 2:
        get_movie_info2(conn,cur,movie_title)
    elif info_number == 3:
        get_movie_info3(conn,cur,movie_title)
    elif info_number == 4:
        get_movie_info4(conn,cur,movie_title)
    else:
        
        os.system('clear')
        print("검색 프로그램을 종료합니다.")
        exit()
    
    conn.commit()
    close_db(conn,cur)
    return

def searching_menu(): # Searching Menu
    os.system('clear')
    while True:
        show_searching_menu()
        searching_option = int(input("원하시는 옵션을 선택해주세요 : "))
        if searching_option == 1:
            os.system('clear')
            movie_title = input("영화 제목을 입력하세요 : ")
            ordering_option = set_ordering()
            search_by_title(movie_title, ordering_option)
            break
        elif searching_option == 2:
            os.system('clear')
            actor_name = input("배우 이름을 입력하세요 : ")
            ordering_option = set_ordering()
            search_by_actor(actor_name, ordering_option)
            break
        elif searching_option == 3:
            os.system('clear')
            director_name = input("감독 이름을 입력하세요 : ")
            ordering_option = set_ordering()
            search_by_director(director_name, ordering_option)
            break
        elif searching_option == 4:
            os.system('clear')
            show_genre_list()
            flag = 0
            while flag==0:
                genre = input("영화 장르를 입력하세요 : ")
                for gen in genre_list:
                    if genre == gen:
                        flag+=1
                        break;
                if flag == 0: print("입력이 잘못되었습니다. 다시 입력해주세요.")
            ordering_option = set_ordering()
            search_by_genre(genre, ordering_option)
            break
        elif searching_option == 5:
            os.system('clear')
            year = int(input("제작 년도를 입력하세요 : "))
            ordering_option = set_ordering()
            search_by_year(year, ordering_option)
            break
        elif searching_option == 6:
            os.system('clear')
            country = input("제작 국가를 입력하세요 : ")
            ordering_option = set_ordering()
            search_by_country(country, ordering_option)
            break
        elif searching_option == 7:
            os.system('clear')
            print("검색 프로그램을 종료합니다.")
            exit()
        else:
            os.system('clear')
            print("입력을 확인해 주세요.")
            print("다시 입력 화면으로 넘어갑니다.")
            time.sleep(1.5)
            os.system('clear')
            
def start_menu(): # Starting Menu
    while True:
        os.system('clear')
        show_menu()
        menu_choice = int(input("원하시는 옵션을 선택해주세요 : "))
        if menu_choice == 1:
            searching_menu()
        else:
            os.system('clear')
            print("검색 프로그램을 종료합니다.")
            exit()

if __name__ == '__main__':
    
    os.system('clear')
    start_menu()
    

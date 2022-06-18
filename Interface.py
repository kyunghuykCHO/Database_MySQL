import pymysql
import os

genre_list = ["드라마","판타지","서부","공포","모험","멜로/로맨스","스릴러","느와르","컬트","다큐멘터리","코미디","가족",
              "미스터리","전쟁","애니메이션","범죄","뮤지컬","SF","액션","무협","에로","서스펜스","서사","블랙코미디",
              "실험","공연실황"]

def open_db():
    conn = pymysql.connect(host='localhost', user='root',
                           password='whrudgur', db='navermovie', unix_socket='/tmp/mysql.sock')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    return conn,cur
def close_db(conn,cur):
    cur.close()
    conn.close()

def show_menu():
    print("*****************")
    print("*  1) 영화검색  *")
    print("*  2) 종료하기  *")
    print("*****************")
def show_searching_menu():
    print("**********************")
    print("*  1) 영화제목 검색  *")
    print("*  2) 배우이름 검색  *")
    print("*  3) 감독이름 검색  *")
    print("*  4) 장르 검색      *")
    print("*  5) 평점 검색      *")
    print("*  6) 프로그램 종료  *")
    print("**********************")
def show_genre_list():
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

def set_ordering():
    print("검색 정렬 조건입니다.")
    print("1) 가나다순 2) 년도순 3) 평점순")
    num = input("원하시는 조건에 맞는 번호를 입력하세요 : ")
    return num
def set_rating():
    print("입력받은 평점을 넘은 영화작품을 검색합니다.")
    rate = float(input("평점을 입력하세요 (0.00~10.00) : "))
    return rate

# 영화제목 movie_title 배우이름 actor_name 감독이름 director_name 장르 genre 평점 rate 
# 검색옵션 ordering_option 1->가나다 2->년도순 3->평점순
# 각 def 마다 conn, cur = open_db() , close_db(conn,cur) 설정 해야함
def search_by_title(movie_title, ordering_option): # 제목 검색 . 정렬순
    print(" test ")
def search_by_actor(actor_name, ordering_option): # 배우 검색 , 정렬순
    print(" test ")
def search_by_director(director_name, ordering_option): # 감독 검색 , 정렬순
    print(" test ")
def search_by_genre(genre, ordering_option): # 장르 검색 , 정렬순
    print(" test ")
def search_by_rate(rate, ordering_option): # 평점 검색 , 정렬순 
    print(" test ")

def searching_menu():
    os.system('clear')
    show_searching_menu()
    searching_option = int(input("원하시는 옵션을 선택해주세요 : "))
    if searching_option == 1:
        os.system('clear')
        movie_title = input("영화 제목을 입력하세요 : ")
        ordering_option = set_ordering()
        search_by_title(movie_title, ordering_option)
    elif searching_option == 2:
        os.system('clear')
        actor_name = input("배우 이름을 입력하세요 : ")
        ordering_option = set_ordering()
        search_by_title(actor_name, ordering_option)
    elif searching_option == 3:
        os.system('clear')
        director_name = input("감독 이름을 입력하세요 : ")
        ordering_option = set_ordering()
        search_by_title(director_name, ordering_option)
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
        search_by_title(genre, ordering_option)
    elif searching_option == 5:
        os.system('clear')
        rate = set_rating()
        ordering_option = set_ordering()
        search_by_title(movie_title, ordering_option)
    else:
        os.system('clear')
        print("검색 프로그램을 종료합니다.")
        exit()
def start_menu():
    while True:
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

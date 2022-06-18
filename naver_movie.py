"""import pymysql"""
import requests 
from bs4 import BeautifulSoup
import re



def main_crawling():
    total_movie_cnt = 0
    for i in range (1, 50):
        temp = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220617&page=" + str(i)
        data = requests.get(temp)
        soup = BeautifulSoup(data.text, 'html.parser')
        # error = soup.select_one('#container > script').text
        movie_list = soup.select('#old_content > table > tbody > tr')
        for movie in movie_list:
            movie_address = movie.select_one('td.title > div')
            if(movie_address is not None):
                total_movie_cnt += 1
                print ("영화 수 : " + str(total_movie_cnt))
                # print (movie_address.find("a")["href"])
                # print (movie_list)
                temp1 = "https://movie.naver.com" + movie_address.find("a")["href"]
                data1 = requests.get(temp1)
                soup = BeautifulSoup(data1.text, 'html.parser')
                error = soup.select_one('#container > script').text
                
                
                if "alert" in error:
                    i = i + 1
                    print("영화 없음")
                else:
                    # print(i)
                    #제목
                    title = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)')
                    if title is not None:
                        title = title.text
                        print("제목: " + title)
                    else:
                        print("제목 없음")

                #관람객 평점

                people_rate = soup.select_one('#actualPointPersentBasic > div')
                people_ratecheck = soup.select_one('#actualPointPersentBasic > div > span')
                if people_rate is not None:
                    if '없음' not in people_rate.text:        
                        people_rate = people_rate.text
                        people_ratecheck = people_ratecheck.text
                        
                        people_rate = people_rate.replace(people_ratecheck, '')        
                        people_rate = people_rate.replace('\t', '')
                        people_rate = people_rate.replace('\n', '')
                        people_rate = people_rate.replace('\r', '')
                        print("관람객 평점: " + people_rate)
    
                netizen_rate = soup.select_one('div.main_score > div:nth-child(2) > div > a > div')

                if netizen_rate is not None:
                    netizen_rate = netizen_rate.text
                    netizen_rate = netizen_rate.replace('\t', '')
                    netizen_rate = netizen_rate.replace('\n', '')
                    netizen_rate = netizen_rate.replace('\r', '')
                    netizen_rate = netizen_rate.replace(' ', '')
                    print("네티즌 평점: " + netizen_rate)
    
    
                critic_rate = soup.select_one('#pointNetizenPersentBasic')
                if critic_rate is not None:
                    critic_rate = critic_rate.text
                    if float(critic_rate) > 0:
                        print("전문가 평점: " + critic_rate)
    
                spans = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span')
                
                temp_gen = "드라마 판타지 서부 공포 멜로/로맨스 모험 스릴러 느와르 컬트 다큐멘터리 코미디 가족 미스터리 전쟁 애니메이션 범죄 뮤지컬 SF 액션 무협 에로 서스펜스 서사 블랙코미디 실험 공연실황"
                temp_style = "TV시리즈 TV영화 단편영화 뮤직비디오 비디오영화 옴니버스영화 웹드라마 웹무비"
                temp_run = "분"
                temp_date = "개봉"    
                                
                if len(spans) == 4:            
                    #국가, 러닝타임, 개봉일자, 감독, 출연, 관람 등급
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        
                        genarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                        
                        if genarr[0].text in temp_gen:
                            for genre in genarr:
                                genre = genre.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
                            
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
            
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
                                
                if len(spans) == 3:            
                    #국가, 러닝타임, 개봉일자, 감독, 출연, 관람 등급
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        
                        genarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                        
                        if genarr[0].text in temp_gen:
                            for genre in genarr:
                                genre = genre.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
                            
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
                                
                if len(spans) == 2:            
                    #국가, 러닝타임, 개봉일자, 감독, 출연, 관람 등급
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        
                        genarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                        
                        if genarr[0].text in temp_gen:
                            for genre in genarr:
                                genre = genre.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
                            
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
    
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
                # 줄거리
                slot = soup.select('div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p.con_tx')
                if slot is not None:
                    for i in slot:
                        temp = i.text
                        temp = temp.replace('\r', '')
                        temp = temp.replace('\xa0', '\n')
                        print(temp)
                people_rating_crawling(temp1)
                total_movie_cnt = rel_movie_crawling(temp1, total_movie_cnt)
                        
                    

def rel_movie_crawling(temp1, total_movie_cnt):
     # 관련 영화 크롤링
     rel_movie_cnt = 0
     data1 = requests.get(temp1)
     soup = BeautifulSoup(data1.text, 'html.parser')
     rel_movie_list = soup.select('#content > div.article > div:nth-child(7) > div:nth-child(2) > div > ul > li')
     
     for rel_movie in rel_movie_list: 
         rel_movie_address = rel_movie.find('a')['href']
         print(rel_movie_address)
         if(rel_movie_address is not None):
                total_movie_cnt += 1
                print ("영화 수 : " + str(total_movie_cnt))
                # print (movie_address.find("a")["href"])
                # print (movie_list)
                temp2 = "https://movie.naver.com" + rel_movie_address
                data1 = requests.get(temp2)
                soup = BeautifulSoup(data1.text, 'html.parser')
                error = soup.select_one('#container > script').text
                
                
                if "alert" in error:
                    # i = i + 1
                    print("영화 없음")
                else:
                    # print(i)
                    #제목
                    title = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)')
                    if title is not None:
                        title = title.text
                        print("제목: " + title)
                    else:
                        print("제목 없음")

                #관람객 평점
                people_rate = soup.select_one('#actualPointPersentBasic > div')
                people_ratecheck = soup.select_one('#actualPointPersentBasic > div > span')
                if people_rate is not None:
                    if '없음' not in people_rate.text:        
                        people_rate = people_rate.text
                        people_ratecheck = people_ratecheck.text
                        
                        people_rate = people_rate.replace(people_ratecheck, '')        
                        people_rate = people_rate.replace('\t', '')
                        people_rate = people_rate.replace('\n', '')
                        people_rate = people_rate.replace('\r', '')
                        print("관람객 평점: " + people_rate)
    
                netizen_rate = soup.select_one('div.main_score > div:nth-child(2) > div > a > div')
                if netizen_rate is not None:
                    netizen_rate = netizen_rate.text
                    netizen_rate = netizen_rate.replace('\t', '')
                    netizen_rate = netizen_rate.replace('\n', '')
                    netizen_rate = netizen_rate.replace('\r', '')
                    netizen_rate = netizen_rate.replace(' ', '')
                    print("네티즌 평점: " + netizen_rate)
    
    
                critic_rate = soup.select_one('#pointNetizenPersentBasic')
                if critic_rate is not None:
                    critic_rate = critic_rate.text
                    if float(critic_rate) > 0:
                        print("전문가 평점: " + critic_rate)
    
                spans = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span')
                
                temp_gen = "드라마 판타지 서부 공포 멜로/로맨스 모험 스릴러 느와르 컬트 다큐멘터리 코미디 가족 미스터리 전쟁 애니메이션 범죄 뮤지컬 SF 액션 무협 에로 서스펜스 서사 블랙코미디 실험 공연실황"
                temp_style = "TV시리즈 TV영화 단편영화 뮤직비디오 비디오영화 옴니버스영화 웹드라마 웹무비"
                temp_run = "분"
                temp_date = "개봉"    
                                
                if len(spans) == 4:            
                    #국가, 러닝타임, 개봉일자, 감독, 출연, 관람 등급
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        
                        genarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                        
                        if genarr[0].text in temp_gen:
                            for genre in genarr:
                                genre = genre.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
                            
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
            
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
                                
                if len(spans) == 3:            
                    #국가, 러닝타임, 개봉일자, 감독, 출연, 관람 등급
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        
                        genarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                        
                        if genarr[0].text in temp_gen:
                            for genre in genarr:
                                genre = genre.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
                            
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
                                
                if len(spans) == 2:            
                    #국가, 러닝타임, 개봉일자, 감독, 출연, 관람 등급
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
                        
                        genarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                        
                        if genarr[0].text in temp_gen:
                            for genre in genarr:
                                genre = genre.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
                            
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
    
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
    
                    arr = soup.select('div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2)')
                    if arr is not None:
                        aaaaa = arr[0].text
                        aaaaa = aaaaa.replace('\n', '')
                        aaaaa = aaaaa.replace('\r', '')
                        aaaaa = aaaaa.replace('\t', '')
    
                        if temp_gen in aaaaa:
                            for a in arr:
                                genre = a.text
                                print("장르: " + genre)
    
                        elif temp_run in aaaaa:
                            running_time = aaaaa
                            running_time = running_time.replace(' ', '')
                            running_time = running_time.replace('분', '')                
                            print("러닝타임: " + running_time)
    
                        elif temp_date in aaaaa:
                            date = aaaaa
                            date = date.replace(' 개봉', '')
                            date = date.replace('\t', '')
                            date = date.replace('\n', '')
                            date = date.replace('\r', '')
                            date = date.replace(' ', '')
                            print("개봉일: " + date)
    
                        elif aaaaa in temp_style:
                            print("스타일: " + aaaaa)
                            
                        else:
                            natarr = soup.select('div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a')
                            for nat in natarr:
                                nation = nat.text
                                nation = nation.replace('\n', '')
                                nation = nation.replace('\r', '')
                                nation = nation.replace('\t', '')
                                print("국가: " + nation)
                # 줄거리
                slot = soup.select('div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p.con_tx')
                if slot is not None:
                    for i in slot:
                        temp = i.text
                        temp = temp.replace('\r', '')
                        temp = temp.replace('\xa0', '\n')
                        print(temp)
     
     return total_movie_cnt   
 
    
def people_rating_crawling(temp):
     data = requests.get(temp)
     soup = BeautifulSoup(data.text, 'html.parser')
     people_rating = soup.select_one('#movieEndTabMenu > li:nth-child(5)')
     print(people_rating)
     
     people_rating_address=  people_rating.find('a')['href']
     
    
     
     temp2 = "https://movie.naver.com" + people_rating_address
     data1 = requests.get(temp2)
     soup = BeautifulSoup(data1.text, 'html.parser')
     
     total = soup.select_one("body > div > div > div.score_total > strong")
     print(total)

    
    
    

def quote_crawling():
    for i in range (19990, 20100):
        print(i)
        temp = "https://movie.naver.com/movie/bi/mi/script.naver?code=" + str(i) + "&order=best&nid=&page="
        data = requests.get(temp)
        soup = BeautifulSoup(data.text, 'html.parser')
        error = soup.select_one('#iframeDiv > div.top_behavior.no_border > span > em').text
        if '0' in error:
            i = i + 1    
            print("명대사 없음")
        else:

            # 명대사
            arr = soup.select_one('#iframeDiv > div.paging > div').text.replace('다음', '').replace('\n', '').replace('10','').strip()
            pages = list(arr)     

            for i in range(len(pages)):

                page = pages[i]

                lis = soup.select('#iframeDiv > ul > li')

                for li in lis:

                    quote = li.select_one('div > p.one_line').text
                    print(quote)

                    author = li.select_one('div > p.char_part > span')
                    if author is not None:
                        author = author.text
                        print(author)

                    nickname = li.select_one('div > p.etc_lines > span:nth-child(1) > a').text
                    print(nickname)

                    date = li.select_one('div > em').text
                    print(date)

if __name__ == '__main__':
    main_crawling()
    #quote_crawling()

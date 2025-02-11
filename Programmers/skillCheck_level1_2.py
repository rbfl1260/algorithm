#유효기간 지났을 시 폐기

def solution(today,terms,privacies):
    res=[]
    Tyear,Tmonth,Tday=map(int,today.split())
    #공백으로 구분해서 년도, 달, 날짜 구분.
    term_dict={term:int(month) for term,month in (x.split() for x in terms)}
    #terms를 공백으로 구분해서 term:month 딕셔너리로 만듦

    for index,privacy in enumerate(privacies):
        start,term=privacy.split()
        Syears,Smonth,Sday=map(int,start.split())
        
        Smonth+=term_dict[term]
        if Smonth>12:
            Syears+=Smonth//12
            Smonth%=12
            if Smonth==0:
                Syears-=1
                Smonth=12
        if (Syears<Tyear) or (Syears==Tyear and Smonth<Tmonth) or (Syears==Tyear and Smonth==Tmonth and Sday<=Tday):
            res.append(index+1)
    return res
#베스트 앨범
def solution(genres, plays):
    answer = []
    hash_map={}
    for i in range(len(genres)):
        hash_map[genres[i]]=hash_map.get(genres[i],0)+plays[i]
    #sorted_hash_False=sorted(hash_map.items(),reverse=True)
    #정렬하면 리스트로 바뀜, 딕셔너리가 아님
    #reverse=True로 하면 튜플 첫번째 요소(장르 이름) 기준으로 내림차순 정렬됨.
    #총 재생 수 기준 내림차순이 필요하므로 아래와 같이 작성해야 함
    sorted_hash=sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
    
    
    genres_songs={}
    for i in range(len(genres)):
        genres_songs.setdefault(genres[i],[]).append((plays[i],i)) #튜플로 배열안에 넣음
    
    for g, _ in sorted_hash:
        songs=genres_songs[g] #songs는 리스트 형태임
        songs.sort(key=lambda x: (-x[0],x[1])) #첫번째 기준은 재생 수 내림차순, 두번쨰 기준은 인덱스 오름차순
        #sort는 원본 리스트를 바꿈.
        #x는 리스트의 각 원소 -> 재생수와 인덱스 튜플
        #-x[0]: 재생수를 내림차순으로 정렬하기 위해 음수
        #x[1]: 인덱스는 오름차순으로 정렬
        top_two=songs[:2]
        for s in top_two:
            answer.append(s[1])

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
solution(genres,plays)
def solution(genres, plays):
    answer = []

    # 장르 순위를 선정을 위한 딕셔너리 -> {장르 : 재생횟수 총합}
    genre_rank = dict.fromkeys(genres, 0)
    song_data = {}  # 장르별 곡 정보를 위한 딕셔너리 -> {장르 : [(곡인덱스, 재생횟수),...,...]}

    for genre in genre_rank.keys():  # song_data 를 위한 초기화 과정
        songlist = []
        song_data[genre] = songlist

    for i in range(len(genres)):
        genre_rank[genres[i]] += plays[i]  # 장르별 총 재생횟수 합계
        # (곡인덱스, 재생횟수) 의 형태로 곡 정보 입력
        song_data[genres[i]].append((i, plays[i]))
        # 재생횟수(큰수 우선) -> 곡 인덱스 순서(작은수 우선)로 정렬
        song_data[genres[i]].sort(key=lambda x: (-x[1], x[0]))

    # 총 재생횟수 기준 정렬 후, 장르순서만 리스트 변환
    genre_rank = sorted(genre_rank.items(), key=lambda item: -item[1])

    for genre in genre_rank:
        # 우탁씨의 아이디어 이용(슬라이싱은 범위의 값이 존재 안해도 통과)
        nominated = song_data[genre[0]][:2]
        for song in nominated:
            answer.append(song[0])  # 선택된 곡의 인덱스만 추가

    return answer

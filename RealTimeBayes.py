from bayes import BayesianFilter
bf = BayesianFilter()

#텍스트 학습 (긍정, 부정 데이터를 받아들여 어떤 값이 들어갈때 긍정인지 부정인지 알 수 있다.)
bf.fit("오영주가 먼저 부산가겠다 하고 임현주가 남은 속초 간거잖아요;; 현주 여우란 말은 왜나오는거임","부정")
bf.fit("첨부터 현우는 현주적으면 안되는거였어그게잘못이지내가영주여도 실망할듯","부정")
bf.fit("카메라맨 일일이 다 따라다니면서 클로즈업하는데 데이트라니? 연예인들이면 몰라도 일반인 데이트에 카메라맨까지 추가된 상황이면 진심이 못 오가지 결론은 100% 대본","부정")
bf.fit("현우가 샐러드 영주주려고 만든거 현주가 말해줘서 영주도 알구요 지난주에도 현우가 쿠키 만든거 주면서 너인거 알겠지? 이렇게 직접적으로 말했어요 현우가 답답한부분도 있지만 영주가 심하게 의심하는것도 맞아요","부정")
bf.fit("지난번 방송에서 꼬리곰탕 먹으러 가자고 도균이 현주한테 얘기함 현주가 학교간다고 시간 없어서 못 감. 그걸 가지고 부산 가고 싶어했다는 억지 좀 그만","부정")
bf.fit("이프로가 현우 영주를 위한 프로냐~둘좀 그만 밀어라 ㅋ지겨움","부정")
bf.fit("현우가 마지막에 지호때리고 다은이를 강제로 뺐는데요 인간쓰레기.","부정")
bf.fit("솔직히오늘대로되면 하트시그널2존나헤피엔딩인데 영주랑현우는 너무생각하는게다르냐왜","부정")
bf.fit("기본적으로 요리학원도 안다니고 책으로만 보고 음식 장사 하겠다 생각부터 틀려 먹었네요ㅎㅎ","부정")
bf.fit("허상을 이야기하는데 사람들은 뭔내용이냐고 투덜댄다..ㅋㅋㅋ","긍정")
bf.fit("뭔재미로 보는건지 원...","부정")
bf.fit("각 장면에 숨겨진 뜻과 메타포를 읽어내느라 정신없었지만 그만큼 재미있었고 여운이 길게 남는 영화, 마지막이 강렬했던 영화","긍정")
bf.fit("중간에 피는 못 속인다는 흘러가는 대사와 아버지가 창고에 숨겨 보관한 칼을 발견하는 종수...16년 만에 만나 500만원을 찾는 엄마 앞에서도 덤덤했던 종수였지만 결국 종수 자신 안에 꾹꾹 눌러담아 감추어 두었던 화를 폭발시키는 마지막의 종수...좋다.","긍정")
bf.fit("남자들은 못생긴 여자에게 아름다움을 강요하지 않는다 그냥 예쁜 여자를 찾아서 만나는 거지 근데 남들 옷 사입고 화장품 살 돈 지들은 치킨과 족발 피자로 다 사용하며 당해본 적도 없는 사회적 불평등을 토로하며 반대 의견은 공공의 적으로 만드는 쿵쾅이들","긍정")
bf.fit("종수가 태운 욕망의 잿더미 혜미.","긍정")

#예측1
pre,scorelist=bf.predict("오영주 존나 인간쓰레기")
print("결과 =",pre)
print(scorelist)

#예측2
pre,scorelist=bf.predict("이 영화 지겨움 뭔재미냐;;")
print("결과 =",pre)
print(scorelist)

#예측3
pre,scorelist=bf.predict("재미있었고 감동적인 소설이었다.")
print("결과 =",pre)
print(scorelist)

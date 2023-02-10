# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/dataproject1/NanumGothic.otf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


# 21년도 고속국도 교통사고 데이터 불러오기. 출처: 사이버경찰청, 교통사고 상세통계, 교통사고분석시스템(TAAS) (http://taas.koroad.or.kr/)
강원21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EA%B0%95%EC%9B%90.csv', encoding='CP949')
경기21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EA%B2%BD%EA%B8%B0.csv', encoding='CP949')
경남21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EA%B2%BD%EB%82%A8.csv', encoding='CP949')
경북21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EA%B2%BD%EB%B6%81.csv', encoding='CP949')
광주21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EA%B4%91%EC%A3%BC.csv', encoding='CP949')
대구21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EB%8C%80%EA%B5%AC.csv', encoding='CP949')
대전21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EB%8C%80%EC%A0%84.csv', encoding='CP949')
부산21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EB%B6%80%EC%82%B0.csv', encoding='CP949')
서울21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%84%9C%EC%9A%B8.csv', encoding='CP949')
세종21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%84%B8%EC%A2%85.csv', encoding='CP949')
울산21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%9A%B8%EC%82%B0.csv', encoding='CP949')
인천21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%9D%B8%EC%B2%9C.csv', encoding='CP949')
전남21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%A0%84%EB%82%A8.csv', encoding='CP949')
전북21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%A0%84%EB%B6%81.csv', encoding='CP949')
충남21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%B6%A9%EB%82%A8.csv', encoding='CP949')
충북21 = pd.read_csv('https://github.com/amrasanor/dataproject1_4/raw/master/(%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C)_2021%EB%85%84_%EC%B6%A9%EB%B6%81.csv', encoding='CP949')

# 조사를 위해, 21년도 고속국도 교통사고 데이터의 기상상태 열만 데이터프레임화
강원 = pd.DataFrame(강원21.기상상태)
경기 = pd.DataFrame(경기21.기상상태)
경남 = pd.DataFrame(경남21.기상상태)
경북 = pd.DataFrame(경북21.기상상태)
광주 = pd.DataFrame(광주21.기상상태)
대구 = pd.DataFrame(대구21.기상상태)
대전 = pd.DataFrame(대전21.기상상태)
부산 = pd.DataFrame(부산21.기상상태)
서울 = pd.DataFrame(서울21.기상상태)
세종 = pd.DataFrame(세종21.기상상태)
울산 = pd.DataFrame(울산21.기상상태)
인천 = pd.DataFrame(인천21.기상상태)
전남 = pd.DataFrame(전남21.기상상태)
전북 = pd.DataFrame(전북21.기상상태)
충남 = pd.DataFrame(충남21.기상상태)
충북 = pd.DataFrame(충북21.기상상태)


# 용이한 작업을 위해, 추출한 기상상태 열을 합치기
res = pd.concat([강원, 경기, 경남, 경북, 광주, 대구, 대전, 부산, 서울, 세종, 울산, 인천, 전남, 전북, 충남, 충북])

# 기상상태 열의 종류 확인하기
# res.value_counts()

# 전체 기상상태 통계 그래프
plt.pie(res['기상상태'].value_counts(),
        labels=['맑음', '비', '흐림', '눈', '안개', '기타'],
        explode=(0, .5, 0, .5, 0, .5),
        counterclock=False,
        startangle=90,
        autopct='%1.2f%%',
        shadow=True,
        radius=2,
        textprops={'size': 14})

plt.legend(loc=(1.4, 1.2))

plt.show()

# 맑음은 일상 사고여서 기후와 사고의 상관관계가 약하며
# 맑음 때문에 파이 그래프가 제대로 나오지 않음
# 따라서 삭제하고 비, 흐림, 눈, 안개, 기타만 출력하도록 함

# 맑음 삭제하여 별도의 테이블로 만들기
res_drop = res[res['기상상태'] == '맑음'].index
res2 = res.drop(res_drop)  # 추후 다시 res를 참조할 수 있으므로 res2로 설정함

# drop 결과 확인
# res2.value_counts()

# 국내 기후별 교통사고율 파이그래프(맑음 제거 ver.)
plt.pie(res2['기상상태'].value_counts(),
        labels=['비', '흐림', '눈', '안개', '기타'],
        explode=(0, 0, .5, 0, .5),
        counterclock=False,
        startangle=90,
        autopct='%1.2f%%',
        shadow=True,
        radius=2,
        textprops={'size': 14})

plt.legend(loc=(1.4, 1.2))

plt.show()

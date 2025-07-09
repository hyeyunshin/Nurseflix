# nurseflix_advanced_app.py
import streamlit as st
from datetime import datetime, timedelta

# 페이지 기본 설정
st.set_page_config(page_title="Nurseflix 고급 서비스", page_icon="🩺")
st.title("🩺 Nurseflix - 개인 맞춤 간호 구독 서비스")

# 1. 사용자 정보 입력
st.header("1️⃣ 개인정보 입력")
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", 0, 120, step=1)
target = st.selectbox("대상 분류", ["청소년", "직장인", "임산부", "노인", "만성질환자"])
region = st.selectbox("거주 지역", ["서울", "부산", "대구", "인천", "광주", "기타"])

# 2. 건강 정보 입력
st.header("2️⃣ 건강 상태 입력")
height = st.number_input("키 (cm)", 100, 250)
weight = st.number_input("몸무게 (kg)", 20, 200)
sleep = st.slider("하루 수면 시간", 0, 12, 6)
meals = st.radio("오늘 식사하셨나요?", ["예", "아니오"])
mood = st.selectbox("현재 기분은?", ["좋음", "보통", "나쁨"])

# 3. 간호 추천 결과
if st.button("간호 추천 받기"):
    st.subheader(f"✅ {name}님의 간호 서비스 요약")

    st.markdown("### 🧑‍⚕️ 대상 맞춤 간호 서비스")
    if target == "임산부":
        st.write("- 산후 회복 및 우울증 예방 프로그램")
    elif target == "노인":
        st.write("- 낙상 예방, 복약 지도, 외로움 완화 간호")
    elif target == "청소년":
        st.write("- 스트레스 관리 및 수면 교육")
    elif target == "직장인":
        st.write("- 피로 관리, 스트레스 해소 코칭")
    elif target == "만성질환자":
        st.write("- 자가 건강관리 피드백, 복약 코칭")

    st.markdown("### ⚖️ 비만도(BMI) 분석 및 운동 추천")
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 1)
    st.write(f"BMI: **{bmi}**")

    if bmi < 18.5:
        st.warning("저체중입니다. 영양 보충 필요")
        st.markdown("[🍽️ 영양식 영상 보기](https://youtu.be/lLxX_mLO09o)")
    elif 18.5 <= bmi < 23:
        st.success("정상 체중입니다. 유지하세요!")
        st.markdown("[🏃 스트레칭 영상 보기](https://youtu.be/I_izvAbhExY)")
    elif 23 <= bmi < 25:
        st.info("과체중입니다. 생활습관 개선이 필요합니다")
        st.markdown("[💪 유산소 운동 영상 보기](https://youtu.be/ml6cT4AZdqI)")
    else:
        st.error("비만입니다. 적극적인 관리가 필요합니다")
        st.markdown("[🔥 전신 다이어트 운동 보기](https://youtu.be/UBMk30rjy0o)")

    st.markdown("### 🎧 정서 케어 콘텐츠")
    if mood == "나쁨" or sleep < 6:
        st.write("- 😴 수면 부족 또는 기분 저하 감지됨")
        st.markdown("[🛌 수면 유도 오디오](https://youtu.be/MtGQ6LEeBlo)")
        st.markdown("[🧘 명상 영상](https://youtu.be/inpok4MKVLM)")
    elif mood == "보통":
        st.markdown("[🎵 기분 전환 음악](https://youtu.be/kXYiU_JCYtU)")
    else:
        st.write("정서 상태 양호. 유지하세요! 😊")

    st.success("Nurseflix는 건강한 삶을 위해 함께합니다")

# 4. 지역 연계 서비스 + 1:1 간호사 매칭
st.header("3️⃣ 지역 연계 간호사 매칭")
if name:
    st.write(f"📍 [{region}] 지역 간호사 매칭 중...")
    # 임의 매칭 예시
    if region in ["서울", "인천"]:
        nurse_name = "김지현 간호사"
    elif region in ["부산", "대구"]:
        nurse_name = "이수연 간호사"
    else:
        nurse_name = "박민정 간호사"

    st.write(f"🩺 담당 간호사: **{nurse_name}**")

    st.markdown("### 📅 간호 상담 예약")
    date = st.date_input("상담 희망 날짜", value=datetime.today())
    time = st.time_input("상담 시간 선택", value=datetime.now().time())

    if st.button("상담 예약 확정"):
        st.success(f"✅ {date} {time}에 {nurse_name}님과 상담 예약이 완료되었습니다!")
        st.balloons()

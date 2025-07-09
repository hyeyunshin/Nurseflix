# nurseflix_enhanced.py
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Nurseflix 고급형", page_icon="🩺")

# 앱 제목
st.title("🩺 Nurseflix - 맞춤형 간호 구독 서비스")

# 입력: 기본 정보
st.header("1️⃣ 개인정보 입력")
name = st.text_input("이름")
age = st.number_input("나이", min_value=0, max_value=120)
target = st.selectbox("대상 분류", ["청소년", "직장인", "임산부", "노인", "만성질환자"])

# 입력: 건강 정보
st.header("2️⃣ 건강 상태 입력")
height = st.number_input("키 (cm)", min_value=100, max_value=250)
weight = st.number_input("몸무게 (kg)", min_value=20, max_value=200)
sleep = st.slider("하루 수면 시간", 0, 12, 6)
meals = st.radio("오늘 식사하셨나요?", ["예", "아니오"])
mood = st.selectbox("현재 기분은?", ["좋음", "보통", "나쁨"])

# 간호 추천 버튼
if st.button("간호 추천 받기"):
    st.subheader(f"✅ {name}님의 간호 서비스 요약")

    # 1. 대상 맞춤 서비스
    st.markdown("### 🧑‍⚕️ 대상 맞춤 서비스")
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

    # 2. 비만도 분석
    st.markdown("### ⚖️ 비만도(BMI) 분석")
    if height > 0:
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 1)
        st.write(f"BMI: **{bmi}**")
        if bmi < 18.5:
            st.warning("저체중입니다. 영양 상담 권장")
        elif 18.5 <= bmi < 23:
            st.success("정상 체중입니다. 유지하세요!")
        elif 23 <= bmi < 25:
            st.info("과체중입니다. 운동을 고려해보세요.")
        else:
            st.error("비만입니다. 전문가 상담이 필요합니다.")
    else:
        st.write("키를 입력해주세요.")

    # 3. 정서 상태 & 콘텐츠 추천
    st.markdown("### 🎧 정서 케어 콘텐츠 추천")
    if mood == "나쁨" or sleep < 6:
        st.write("- 😴 수면 부족 또는 기분 저하 감지됨")
        st.markdown("[🛌 수면 유도 오디오 듣기 (YouTube)](https://youtu.be/MtGQ6LEeBlo)")
        st.markdown("[🧘 명상 영상 보기 (YouTube)](https://youtu.be/inpok4MKVLM)")
    elif mood == "보통":
        st.markdown("[🎵 기분 전환 음악 추천](https://youtu.be/kXYiU_JCYtU)")
    else:
        st.write("정서 상태 양호. 유지하세요! 😊")

    st.success("Nurseflix 서비스를 기반으로 주기적인 간호 피드백을 받으실 수 있습니다.")


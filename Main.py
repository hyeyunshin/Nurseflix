# nurseflix_app.py
import streamlit as st

# 앱 기본 설정
st.set_page_config(page_title="Nurseflix - 간호 구독 추천", page_icon="🩺")

# 제목
st.title("🩺 Nurseflix - 개인 맞춤 간호 추천")

# 입력 받기
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120, step=1)
condition = st.selectbox("건강 상태", ["일반", "임산부", "노인"])
sleep = st.slider("하루 수면 시간 (시간)", 0, 12, 6)
meals = st.radio("오늘 식사하셨나요?", ["예", "아니오"])
mood = st.selectbox("오늘 기분은 어떤가요?", ["좋음", "보통", "나쁨"])

# 추천 버튼
if st.button("간호 추천 보기"):
    st.subheader(f"✅ {name}님의 간호 추천 결과")

    # 상태 기반 추천
    if condition == "임산부":
        st.write("- 🧘 산후 회복, 정서 관리 서비스 추천")
    elif condition == "노인" or age >= 70:
        st.write("- 🚶 낙상 예방, 정서 돌봄 추천")
    else:
        st.write("- 🩹 일반 건강 상담 및 생활습관 케어")

    # 수면 부족
    if sleep < 6:
        st.write("- 😴 수면 부족 감지 → 수면 유도 오디오 추천")

    # 식사 상태
    if meals == "아니오":
        st.write("- 🍽️ 식사 미흡 → 맞춤 식단 제공 필요")

    # 기분
    st.write(f"- 오늘의 기분: {mood}")

    # 요약
    st.success("Nurseflix의 맞춤 간호 서비스를 기반으로 정기 건강 관리가 가능합니다 🩺")



import streamlit as st

# Streamlit 주요 UI 요소 예시
st.title("Streamlit 주요 요소 데모")  # 페이지 제목

st.header("헤더 예시")  # 큰 제목
st.subheader("서브헤더 예시")  # 작은 제목

st.text("일반 텍스트 예시")  # 일반 텍스트
st.markdown("**마크다운 텍스트** _예시_ ")  # 마크다운 지원 텍스트

st.write("write 함수는 다양한 타입의 데이터를 출력할 수 있습니다.")  # write 함수 예시

st.code("print('코드 블록 예시')", language="python")  # 코드 블록

st.latex(r"E = mc^2")  # LaTeX 수식

# 입력 위젯들
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이 입력", min_value=0, max_value=120)  # 숫자 입력
bio = st.text_area("자기소개를 입력하세요")  # 여러 줄 텍스트 입력

agree = st.checkbox("동의합니다")  # 체크박스
gender = st.radio("성별 선택", ["남성", "여성", "기타"])  # 라디오 버튼
color = st.selectbox("좋아하는 색상", ["빨강", "파랑", "초록"])  # 셀렉트박스
colors = st.multiselect("좋아하는 색상 여러 개 선택", ["빨강", "파랑", "초록"])  # 멀티셀렉트

date = st.date_input("날짜 선택")  # 날짜 입력
time = st.time_input("시간 선택")  # 시간 입력

uploaded_file = st.file_uploader("파일 업로드")  # 파일 업로더

st.slider("슬라이더", min_value=0, max_value=100, value=50)  # 슬라이더

# 버튼
if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")  # 버튼 클릭 시 동작

# 데이터 표시
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)  # 데이터프레임 표시
st.table(df)  # 테이블 표시

# 차트 표시
st.line_chart(df)  # 라인 차트
st.bar_chart(df)  # 바 차트
st.area_chart(df)  # 영역 차트

# 이미지 표시
from PIL import Image
import numpy as np
img = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
st.image(img, caption="랜덤 이미지")  # 이미지 표시

# 알림 및 상태 표시
st.success("성공 메시지 예시")  # 성공 메시지
st.info("정보 메시지 예시")  # 정보 메시지
st.warning("경고 메시지 예시")  # 경고 메시지
st.error("에러 메시지 예시")  # 에러 메시지

st.progress(70)  # 진행률 표시

# 스피너
import time
with st.spinner("잠시만 기다려주세요..."):
    time.sleep(1)
st.write("스피너 종료!")

# 사이드바
st.sidebar.title("사이드바 제목")  # 사이드바 제목
st.sidebar.button("사이드바 버튼")  # 사이드바 버튼

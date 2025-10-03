
import streamlit as st

# Streamlit 주요 UI 요소 예시
st.title("고정 지출 확인 리스트")  # 페이지 제목

st.header("")  # 큰 제목
st.subheader("고정 지출을 확인하고 필요없는 지출을 줄이자!")  # 작은 제목


st.markdown("**월별 고정 지출 금액을 입력하고, 사치를 줄이자 (단위: 원)**")  # 마크다운 지원 텍스트



st.latex(r"")  # LaTeX 수식

# 입력 위젯들

name = st.text_input("고정 지출")  # 텍스트 입력
age = st.number_input("고정 수입", min_value=1000000, max_value=100000000)  # 숫자 입력







# 체크박스 리스트 위에 텍스트 추가
st.markdown("\n\n")  # 체크박스 리스트 앞에 공백 추가
st.markdown("###### 고정지출 체크 리스트")

# 여러 체크박스를 가로로 3개씩 나열
check_labels = ["월세 및 관리비", "교통비", "핸드폰 요금", "인터넷 요금", "보험료", "구독 서비스"]
cols = st.columns(3)
checked = []
for i, label in enumerate(check_labels):
	col = cols[i % 3]
	checked.append(col.checkbox(label, key=f"chk_{i}"))


# 직접 입력할 수 있는 기타란 추가
etc = st.text_input("기타 고정지출 항목을 직접 입력하세요")

# 수입에 따른 고정지출 비율 선택란 추가
st.markdown("### 수입에 따른 고정지출 비율")
ratio_options = [f"{i*10}~{(i+1)*10}%" for i in range(10)]
selected_ratio = st.radio("고정지출 비율을 선택하세요", ratio_options)




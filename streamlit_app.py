import streamlit as st

# 1. 앱 제목 및 설정
st.set_page_config(page_title="배송비 계산기", page_icon="📦")
st.title("📦 배송비 안내 프로그램")
st.write("회원 상태와 주문 금액에 따라 총 결제 금액을 계산합니다.")

st.divider()

# 2. 사용자 입력 (입력창과 라디오 버튼 활용)
col1, col2 = st.columns(2)

with col1:
    member = st.radio(
        "정기 회원 여부",
        ("예 (y)", "아니오 (n)"),
        index=1,
        help="정기 회원은 배송비가 면제됩니다."
    )

with col2:
    total = st.number_input(
        "주문 금액 (원)", 
        min_value=0, 
        step=1000, 
        value=0
    )

# 3. 배송비 계산 로직
shipping_fee = 0
if member == "예 (y)":
    st.info("✅ 정기회원으로 배송비가 면제됩니다.")
    shipping_fee = 0
else:
    st.warning("ℹ️ 배송비 3,000원이 부과됩니다.")
    shipping_fee = 3000

final_price = total + shipping_fee

# 4. 결과 출력
st.divider()
if total > 0:
    st.subheader(f"💰 최종 결제 금액: {final_price:,}원")
    st.write(f"(주문 금액 {total:,}원 + 배송비 {shipping_fee:,}원)")
else:
    st.info("금액을 입력해 주세요.")
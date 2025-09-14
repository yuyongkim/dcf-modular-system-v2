# 🏭 석유화학 DCF 가치평가 시스템

석유화학 산업의 투자 프로젝트에 대한 DCF(Discounted Cash Flow) 분석을 수행하는 웹 애플리케이션입니다.

## 📋 주요 기능

- **WACC 계산**: 자기자본비용, 타인자본비용, 세율을 고려한 가중평균자본비용 계산
- **원료/생산품 관리**: 다중 원료 및 생산품 입력 및 실시간 비용/매출 계산
- **인플레이션 반영**: 연간 인플레이션율을 적용한 현금흐름 예측
- **DCF 분석**: NPV, IRR, 회수기간 등 핵심 투자 지표 계산
- **시각화**: 비용 구조 파이차트, 현금흐름 시계열 그래프 제공

## 🚀 실행 방법

### 1. 환경 설정
```bash
pip install -r requirements.txt
```

### 2. Streamlit 앱 실행 (권장)
```bash
streamlit run streamlit_dcf_app.py
```
- 브라우저에서 `http://localhost:8501` 접속

### 3. Flask 앱 실행
```bash
python flask_dcf_app.py
```
- 브라우저에서 `http://localhost:5000` 접속

## 📁 파일 구조

```
final_project/
├── streamlit_dcf_app.py      # Streamlit 메인 애플리케이션
├── flask_dcf_app.py          # Flask 웹 애플리케이션
├── excel_multi_tab_handler.py # Excel 처리 유틸리티
├── price_data_processed.csv  # 석유화학 가격 데이터베이스
├── requirements.txt          # Python 패키지 의존성
├── templates/                # Flask HTML 템플릿
│   ├── index.html
│   ├── price_db_manager.html
│   ├── excel_dashboard.html
│   └── summary_result.html
└── README.md                 # 프로젝트 설명서
```

## 💡 사용법

### Streamlit 앱 (권장)
1. **WACC 설정**: 자기자본비율, 자본비용, 세율 입력
2. **프로젝트 정보**: 초기투자액, 운영기간, 인플레이션율 설정
3. **원료 입력**: 최대 3개 원료의 카테고리, 제품, 수량 입력
4. **생산품 입력**: 최대 3개 생산품의 카테고리, 제품, 수량 입력
5. **비용 구조**: 고정비, 변동비, 유틸리티, 정비비 설정
6. **DCF 계산**: 모든 입력 완료 후 계산 버튼 클릭

### 주요 지표
- **NPV (Net Present Value)**: 순현재가치
- **IRR (Internal Rate of Return)**: 내부수익률
- **회수기간**: 투자금 회수 기간
- **연간 FCF**: 연간 자유현금흐름

## 📊 데이터베이스

`price_data_processed.csv`에는 다음과 같은 석유화학 제품들의 가격 정보가 포함되어 있습니다:
- 원유 및 석유제품
- 천연가스 및 LPG
- 석유화학 기초원료
- 합성수지 및 플라스틱
- 합성고분자 및 섬유

## 🔧 기술 스택

- **Backend**: Python 3.8+
- **Web Framework**: Streamlit, Flask
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Financial Analysis**: SciPy

## 📝 라이선스

이 프로젝트는 교육 및 연구 목적으로 개발되었습니다.

## 🤝 기여

프로젝트 개선을 위한 제안이나 버그 리포트는 언제든 환영합니다.


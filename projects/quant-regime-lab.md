# Quant Regime Lab

**Quantitative Research · Financial Time Series**

- **활동 유형:** 개인 연구 프로젝트 (진행 중)
- **목적:** SPY 수익률과 변동성을 기반으로 시장 국면의 특성 탐색
- **기술:** Python, pandas, NumPy, yfinance, Matplotlib, Jupyter
- **현재 구현:** 데이터 수집·결측 확인, 단순 및 로그수익률, 20거래일 이동 변동성과 연율화 변동성, 가격·변동성 시각화 코드
- **후속 연구:** HMM 시장 국면 추정, 거래비용을 반영한 전략 백테스트, 위험조정 성과 평가 (미완료)

## Selected Code

- [SPY 기초 분석 노트북](quant-regime-lab/notebooks/01_data_eda.ipynb): 데이터 수집, 결측 확인, 수익률 및 이동 변동성 계산, 시각화.
- [의존성](quant-regime-lab/requirements.txt)

기존 개인 연구 노트북의 코드 셀을 유지하고 출력과 개인 실행 환경 메타데이터는 제거했습니다. 의존성을 설치하고 Jupyter에서 실행할 수 있습니다. 시세 데이터 이용 조건을 준수해야 하며, 시장 국면 추정 및 투자전략은 포함하지 않습니다.

[← Portfolio](../README.md)

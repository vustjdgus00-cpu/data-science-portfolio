# QUANT ADAPTIVE | Quant Regime Lab

**Quantitative Research · Financial Time Series · Research in Progress (2026.11)**

SPY 단일 자산 탐색에서 9개 ETF를 활용하는 멀티에셋 시장 국면 분석 및 동적 자산배분 연구로 확장하고 있습니다.

## 현재 진행 상황 (2026-11-26)

| 단계 | 상태 |
|---|---|
| ETF 수정주가 수집 (SPY, QQQ, IWM, EFA, EEM, TLT, IEF, GLD, BIL) | 구현 기록 |
| 단순·로그수익률 계산, VIX 및 무위험금리 통합 | 구현 기록 |
| 결측·중복 날짜·무한대·비정상 가격 점검, CSV 저장 및 재로딩 | 구현 기록 |
| 모멘텀·변동성 등 특성변수 생성 | 착수 |
| 시장 국면 추정·동적 자산배분·백테스트 | 예정 |
| 거래비용·벤치마크·CAGR·Sharpe Ratio·MDD 평가 | 예정 |

위 멀티에셋 진행 상황은 현재 로컬 개발 기록 기준입니다. 신규 노트북 및 실행 결과는 공개 저장소에 아직 동기화되지 않았으며 투자 성과는 아직 산출하지 않았습니다.

## 공개 코드 — SPY 초기 연구

- [SPY 기초 분석 노트북](quant-regime-lab/notebooks/01_data_eda.ipynb): 데이터 수집, 결측 확인, 수익률 및 이동 변동성 계산, 시각화.
- [의존성](quant-regime-lab/requirements.txt)

기존 개인 연구 노트북의 코드 셀을 유지하고 출력과 개인 실행 환경 메타데이터는 제거했습니다. 의존성을 설치하고 Jupyter에서 실행할 수 있습니다. 시세 데이터 이용 조건을 준수해야 하며, 시장 국면 추정 및 투자전략은 포함하지 않습니다.

[← Portfolio](../README.md)

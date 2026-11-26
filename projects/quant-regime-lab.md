# QUANT ADAPTIVE | Quant Regime Lab

**Quantitative Research · Financial Time Series · Research in Progress (2026.11)**

SPY 단일 자산 탐색에서 9개 ETF를 활용하는 멀티에셋 시장 국면 분석 및 동적 자산배분 연구로 확장하고 있습니다.

## 현재 진행 상황 (2026-11-26)

| 단계 | 상태 |
|---|---|
| ETF 수정주가 수집 (SPY, QQQ, IWM, EFA, EEM, TLT, IEF, GLD, BIL) | 구현 기록 |
| 단순·로그수익률 계산, VIX 및 무위험금리 통합 | 구현 기록 |
| 결측·중복 날짜·무한대·비정상 가격 점검, CSV 저장 및 재로딩 | 구현 기록 |
| 탐색적 데이터 분석 (EDA) | CSV 로딩 코드 작성 |
| 모멘텀·변동성 등 특성변수 생성 | 예정 |
| 시장 국면 추정·동적 자산배분·백테스트 | 예정 |
| 거래비용·벤치마크·CAGR·Sharpe Ratio·MDD 평가 | 예정 |

## 데이터 수집 노트북의 기존 실행 기록

- 관측 기간: 2010-01-04 ~ 2026-11-24 (다운로드 종료일 2026-11-25 미포함)
- 수정주가: 4,250 거래일 × 9 ETF, 통합 데이터: 4,250행 × 12열
- 중복 날짜 및 무한대: 각각 0개
- ETF 및 VIX 결측: 0개, 시차 처리된 금리 및 일별 금리: 각각 1개
- 출처: 원본 02번 노트북의 저장된 실행 출력. 공개 사본에서 새로 실행하여 재검증한 결과는 아님.
- 금리의 1거래일 시차는 미래정보 사용 위험을 줄이기 위한 초기 처리이며 실제 발표 시점 및 빈티지 검증은 후속 과제. 일별 무위험수익률은 연 금리/252 근사.

## 공개 코드 — SPY 초기 연구 및 QUANT ADAPTIVE

- [SPY 기초 분석 노트북](quant-regime-lab/notebooks/01_data_eda.ipynb): 데이터 수집, 결측 확인, 수익률 및 이동 변동성 계산, 시각화.
- [멀티에셋 데이터 수집 및 품질검증](quant-regime-lab/notebooks/02_data_collection.ipynb): 원본 코드 사본, 실행 출력 및 로컬 메타데이터 제거.
- [EDA 데이터 로딩](quant-regime-lab/notebooks/03_exploratory_analysis.ipynb): 현재 공유한 코드 사본, 분석 계산은 예정.
- [의존성](quant-regime-lab/requirements.txt)

기존 개인 연구 노트북의 코드 셀을 유지하고 출력과 개인 실행 환경 메타데이터는 제거했습니다. 의존성을 설치하고 notebooks 폴더에서 02번, 03번 순서로 실행합니다. 원시 시세 CSV는 공개하지 않으며 02번에서 로컬 생성합니다. 공개 사본의 전체 재실행은 아직 수행하지 않았습니다. 시세 데이터 이용 조건을 준수해야 하며, 시장 국면 추정 및 투자전략은 포함하지 않습니다.

[← Portfolio](../README.md)

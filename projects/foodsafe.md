# FOODSAFE

**Data Analytics · Data Engineering**

- **활동 유형:** 데이터 분석 프로젝트
- **목적:** 분산된 HACCP 인증·검사·회수·행정처분 기록 통합 분석
- **기술:** Python, Streamlit, 데이터 전처리, 공식 식별키 결합, 자동 테스트
- **결과:** 2026-09-28 QA 기록 기준 인증 52,793개, 검사–회수 직접 연결 고유 사건 40개, 분석 메뉴 14개, 자동 테스트 17개 통과
- **검증 범위:** 전체 검사 모집단이 없어 부적합률이나 미래 위험 예측을 제공하지 않습니다. 기존 QA 기록을 인용한 것이며 이번에 재실행하지 않았습니다.

## Selected Code

- [기초 데이터 정제 함수](foodsafe/examples/data_cleaning.py): 문자열 정규화, 빈 문자열·중복 처리, 날짜 변환.
- [의존성](foodsafe/requirements.txt)

기존 전처리 파일에서 일반적인 함수 두 개만 발췌했습니다. 임의의 예제 DataFrame으로 검토할 수 있으며, 실제 원자료와 식별키 결합·서비스 구현은 포함하지 않습니다.

[← Portfolio](../README.md)

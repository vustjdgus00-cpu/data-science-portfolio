# R.HOPE

**NLP · AI Service Research**

- **활동 유형:** AI 연구·개발 프로젝트
- **목적:** 사용자 발화의 근거를 확인하고 사전상담 준비를 지원
- **기술:** Python, Streamlit, scikit-learn, TF-IDF 및 분류기
- **산출물:** 연구용 소스와 별도 LLM 시연 기록
- **검증 범위:** 연구용 버전과 시연 버전은 구분하며 실제 분석에는 허가된 모델 연결이 필요합니다. 임상적 정확도나 치료 효과를 입증하지 않습니다. 개인 상담 데이터는 공개하지 않습니다.

## Selected Code

- [학습·검증 분리 및 평가](rhope-ai/examples/model_validation.py): 대상자 ID 중복 확인, Precision·Recall·F1 계산.
- [의존성](rhope-ai/requirements.txt)

분리 확인 함수는 기존 학습 코드에서 발췌했으며, 평가 함수는 기존 평가 계산을 일반화한 공개용 예제입니다. 실제 상담 기록·분류기·학습 설정·추론 로직은 포함하지 않습니다. 합성 입력으로 검토할 수 있으며 임상적 성능을 의미하지 않습니다.

[← Portfolio](../README.md)

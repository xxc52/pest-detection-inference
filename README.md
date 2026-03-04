# 병해충 탐지 모델 추론 테스트

YOLOv8n 기반 병해충 탐지 모델(`best.pt`)을 사용해 이미지를 추론하는 스크립트입니다.

## 환경

- Python 3.9+
- Apple Silicon(M1~M5): MPS 가속 사용
- NVIDIA GPU 환경: `device="mps"` → `device="0"` 으로 변경

## 설치

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 파일 구성

```
test_inference/
├── best.pt            ← YOLOv8n 학습 모델 (mAP50 0.88)
├── run_inference.py   ← 추론 스크립트
├── requirements.txt   ← 의존성 패키지
├── dataset_info.md    ← 데이터셋 코드 체계 및 JSON 스키마
└── README.md
```

## 실행

```bash
cd test_inference
source venv/bin/activate
python run_inference.py
```

결과 이미지는 `results/` 폴더에 저장됩니다.

## 이미지 폴더 구성

`run_inference.py`의 `FOLDERS` 리스트에 추론할 폴더명을 입력합니다.
각 폴더에서 2장을 랜덤 샘플링하여 추론합니다.

폴더명 규칙: `VS_{작물코드}_{부위코드}_{병해충코드}`

| 예시 폴더명 | 의미 |
|---|---|
| `VS_010_무화과_01_잎_020_점무늬병` | 무화과 잎 점무늬병 |
| `VS_010_무화과_02_과실_999_정상` | 무화과 과실 정상 |

코드 체계 상세는 [dataset_info.md](dataset_info.md) 참고

## 주요 파라미터

| 파라미터 | 기본값 | 설명 |
|---|---|---|
| `conf` | 0.4 | 탐지 신뢰도 임계값 (낮출수록 더 많이 탐지) |
| `device` | `"mps"` | Apple Silicon GPU. NVIDIA는 `"0"`, CPU는 `"cpu"` |

## 모델 클래스

학습된 18개 클래스 (3차 경로 코드 기준):

| 클래스 | 병해충명 |
|---|---|
| 999 | 정상 |
| 2 | 거세미나방 |
| 3 | 검은점무늬병 |
| 6 | 과실썩음병 |
| 7 | 그을음병 |
| 8 | 노린재 |
| 9 | 바나나곰팡이병 |
| 10 | 반엽병 |
| 12 | 잎말이나방 |
| 13 | 줄기썩음병 |
| 15 | 총채벌레 |
| 16 | 탄저병 |
| 17 | 흰가루병 |
| 18 | 귤굴나방 |
| 19 | 차먼지응애 |
| 20 | 점무늬병 |
| 21 | 바구미 |
| 22 | 궤양병 |

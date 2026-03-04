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
pest-detection-inference/
├── best.pt            ← YOLOv8n 학습 모델 (mAP50 0.88)
├── run_inference.py   ← 추론 스크립트
├── requirements.txt   ← 의존성 패키지
├── dataset_info.md    ← 데이터셋 코드 체계 및 JSON 스키마
├── README.md
└── sample_images/     ← 별도 제공 (sample_images.zip 압축 해제)
    ├── VS_010_무화과_01_잎_017_흰가루병/   (3장)
    ├── VS_010_무화과_01_잎_020_점무늬병/   (3장)
    ├── VS_010_무화과_01_잎_999_정상/       (3장)
    ├── VS_010_무화과_02_과실_017_흰가루병/ (3장)
    ├── VS_010_무화과_02_과실_021_바구미/   (3장)
    └── VS_010_무화과_02_과실_999_정상/     (3장)
```

## 샘플 이미지 준비

`sample_images.zip`을 별도로 받아 레포 루트에 압축 해제합니다.

```bash
unzip sample_images.zip
```

## 실행

```bash
git clone https://github.com/xxc52/pest-detection-inference
cd pest-detection-inference
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
unzip sample_images.zip
python run_inference.py
```

각 카테고리 폴더에서 랜덤 1장을 추론하고, 결과 이미지는 `results/` 폴더에 저장됩니다.

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

from ultralytics import YOLO
from pathlib import Path
import json
import random

MODEL_PATH = "best.pt"
IMAGE_ROOT = Path("sample_images")
OUTPUT_DIR = Path("results")
OUTPUT_DIR.mkdir(exist_ok=True)

FOLDERS = [
    "VS_010_무화과_01_잎_017_흰가루병",
    "VS_010_무화과_01_잎_020_점무늬병",
    "VS_010_무화과_01_잎_999_정상",
    "VS_010_무화과_02_과실_017_흰가루병",
    "VS_010_무화과_02_과실_021_바구미",
    "VS_010_무화과_02_과실_999_정상",
]

model = YOLO(MODEL_PATH)
print(f"모델 로드 완료: {MODEL_PATH}\n")
print(f"클래스 목록: {model.names}\n")
print("=" * 60)

for folder_name in FOLDERS:
    folder_path = IMAGE_ROOT / folder_name
    all_images = list(folder_path.glob("*.JPG"))
    images = random.sample(all_images, min(1, len(all_images)))

    print(f"\n[{folder_name}]")
    for img_path in images:
        results = model(str(img_path), device="mps", conf=0.4, verbose=False)
        result = results[0]

        detections = []
        for box in result.boxes:
            detections.append({
                "class_id": int(box.cls),
                "class_name": model.names[int(box.cls)],
                "confidence": round(float(box.conf), 3),
                "bbox_xywhn": [round(float(v), 4) for v in box.xywhn[0]],
            })

        # 결과 이미지 저장
        out_img = OUTPUT_DIR / f"{img_path.stem}_result.jpg"
        result.save(str(out_img))

        # 결과 출력
        if detections:
            for d in detections:
                print(f"  {img_path.name} → {d['class_name']} (conf: {d['confidence']})")
        else:
            print(f"  {img_path.name} → 탐지 없음")

print("\n" + "=" * 60)
print(f"결과 이미지 저장 위치: {OUTPUT_DIR.resolve()}")

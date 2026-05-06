# 🦺 Construction Site Helmet Compliance Detection

> Real-time PPE safety monitoring powered by **YOLOv8** — detects helmet compliance and classifies scenes as **SAFE 🟢** or **UNSAFE 🔴** instantly.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8n-Ultralytics-purple?style=flat-square)
![mAP@50](https://img.shields.io/badge/mAP@50-98%25-2e7d32?style=flat-square)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

---

## 🚀 Demo

Upload an image or video → detect workers → get instant safety classification.

> 📹 `videos/demo.mp4`

---

## 📌 Problem Statement

Construction sites are high-risk environments where helmets are mandatory. Manual monitoring is:

- ❌ Inefficient
- ❌ Error-prone
- ❌ Not scalable

This system automates compliance checks using computer vision for real-time, reliable safety enforcement.

---

## ⚡ Safety Logic

```python
if any(d.label == "no_helmet" for d in detections):
    scene_status = "UNSAFE 🔴"
else:
    scene_status = "SAFE 🟢"
```

| Scenario | Output |
|---|---|
| All workers wearing helmets | 🟢 SAFE |
| At least one worker without helmet | 🔴 UNSAFE |
| No workers detected | 🟢 SAFE |

---

## 🗂️ Dataset

**Source:** [Roboflow Custom Dataset](https://drive.google.com/drive/folders/1k-4sEVlHFykykAbdwwZEXew4LLb9nzFs?usp=sharing)

| Property | Details |
|---|---|
| Format | YOLO annotation format |
| Classes | `helmet`, `no_helmet` |
| Split | Train / Validation / Test |

**Challenges addressed:**
- Class imbalance (`helmet` >> `no_helmet`)
- Occlusion and small objects
- Varied lighting conditions
- Crowded scenes

---

## 🧠 Model

| Component | Value |
|---|---|
| Model | YOLOv8n |
| Framework | Ultralytics |
| Input Size | 640 × 640 px |
| Epochs | 50 |
| Task | Object Detection |

---

## 📊 Results

### Per-Class Metrics

| Class | Precision | Recall | mAP@50 | mAP@50-95 |
|---|---|---|---|---|
| `helmet` | 96% | 94% | **98%** | 67.5% |
| `no_helmet` | 92% | 88% | **91%** | 64.0% |

> ⚠️ `no_helmet` is the critical safety class — 92% precision and 88% recall means the model catches most violations with minimal false alarms.

### Confusion Matrix

| Actual \ Predicted | helmet | no_helmet |
|---|---|---|
| **helmet** | 3763 ✅ | 15 |
| **no_helmet** | 10 | 1276 ✅ |

---

---

## ✨ Features

- 📤 Image & video upload interface
- 🎯 Real-time YOLOv8 detection
- 🧠 Automatic safety classification
- 📦 Bounding boxes with confidence scores
- 🚨 Instant helmet violation alerts
- 🎥 Video tracking via ByteTrack

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core development |
| YOLOv8 | Object detection |
| OpenCV | Video processing |
| NumPy | Data handling |
| Streamlit | Web UI |

---

## 🚀 Installation

```bash
git clone https://github.com/username/helmet-detection.git
cd helmet-detection
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 Inference Example

```python
from ultralytics import YOLO

model = YOLO("best.pt")
results = model("test.jpg", conf=0.5)
results.show()
```

---

## 🎥 Video Tracking

```python
results = model.track(
    source="video.mp4",
    tracker="bytetrack.yaml",
    save=True
)
```

---

## 📈 Future Improvements

- [ ] Real-time CCTV integration
- [ ] Dashboard analytics for violations
- [ ] Alert system (SMS / Email)
- [ ] Upgrade to YOLOv8s/m for higher accuracy
- [ ] Cloud deployment

---

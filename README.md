# 🦺 Construction Site Helmet Compliance Detection

> Real-time PPE safety monitoring powered by **YOLOv8** — automatically classifies construction scenes as **SAFE ✅** or **UNSAFE ❌** based on helmet detection.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8n-Ultralytics-purple?style=flat-square)
![mAP@50](https://img.shields.io/badge/mAP@50-98%25-2e7d32?style=flat-square)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

---

## 📌 Problem Statement

Construction sites are high-risk environments where PPE (Personal Protective Equipment) compliance — especially helmets — is critical. Manual monitoring is inefficient and inconsistent.

This system automates safety checks using computer vision, delivering instant and reliable assessments from images or live camera feeds.

---

## ⚡ Safety Logic

A single strict rule governs scene-level decisions:

```python
if any(detection.label == "no_helmet" for detection in detections):
    scene_status = "UNSAFE ❌"
else:
    scene_status = "SAFE ✅"
\```

| Scenario | Decision |
|---|---|
| All workers wearing helmets | **SAFE ✅** |
| At least one worker without a helmet | **UNSAFE ❌** |
| No workers detected | **SAFE ✅** *(no violation found)* |

---

## 🗂️ Dataset

**Source:** [Roboflow Custom Dataset](https://drive.google.com/drive/folders/1k-4sEVlHFykykAbdwwZEXew4LLb9nzFs?usp=sharing)

| Property | Details |
|---|---|
| Format | YOLO (`.txt` labels) |
| Classes | `helmet`, `no_helmet` |
| Split | Train / Validation / Test |

**Challenges addressed:**
- Class imbalance — helmet instances significantly outnumber `no_helmet`
- Occlusion and partial visibility of workers
- Varied camera angles and lighting conditions
- Similar visual features between classes at distance

---

## 🧠 Model

| Property | Details |
|---|---|
| Architecture | YOLOv8n (Ultralytics) |
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

> **Note:** `no_helmet` is the critical class for safety enforcement. At 92% precision and 88% recall, the model reliably catches most violations while keeping false alarms low.

### Confusion Matrix

| | Predicted: helmet | Predicted: no_helmet | Missed (background) |
|---|---|---|---|
| **Actual: helmet** | 3763 ✅ | 15 | 241 |
| **Actual: no_helmet** | 10 | 1276 ✅ | 159 |
| **Background FP** | 140 | 149 | — |

---

## 🔁 Inference Pipeline

```
Input Image / Frame
        │
        ▼
  YOLOv8n Inference
  (imgsz=640, conf threshold)
        │
        ▼
  Bounding Box Extraction
  [class: helmet | no_helmet | confidence]
        │
        ▼
  Safety Logic Layer
  (any no_helmet? → UNSAFE ❌)
        │
        ▼
  Color-coded Scene Verdict
  🟢 SAFE  /  🔴 UNSAFE
\```

---

## ✨ Features

- 📤 Image upload interface
- ⚡ Real-time YOLOv8 inference with bounding box overlay
- 🎨 Color-coded scene verdict: 🟢 **SAFE** / 🔴 **UNSAFE**
- 📈 Confidence scores displayed per detection

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Ultralytics YOLOv8 | Object detection model |
| OpenCV | Image processing |
| NumPy | Array operations |
| Streamlit | Web UI deployment |

---

## 🚀 Getting Started

```bash
git clone https://github.com/Ahmed-KKhaled/computer-vision-safety-detection.git
cd computer-vision-safety-detection
pip install -r requirements.txt
streamlit run app.py
\```

---


---

## 📄 License

This project is licensed under the MIT License.

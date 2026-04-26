# Construction Site Helmet Compliance Detection

A real-time safety monitoring system built with **YOLOv8** that detects whether construction workers are wearing helmets and classifies each scene as **Safe** or **Unsafe**.

---

## Problem Statement

Construction sites are high-risk environments where PPE (Personal Protective Equipment) compliance — especially helmets — is critical. Manual monitoring is inefficient and inconsistent. This system automates that process using computer vision, providing instant and reliable safety assessments from images or live camera feeds.

---

## Safety Logic

The scene-level decision follows a single strict rule:

```python
if any(detection.class == "no_helmet" for detection in detections):
    scene_status = "UNSAFE ❌"
else:
    scene_status = "SAFE ✅"
```

| Scenario | Decision |
|---|---|
| All workers wearing helmets | **SAFE ✅** |
| At least one worker without helmet | **UNSAFE ❌** |
| No workers detected | **SAFE ✅** (no violation found) |

---

## Dataset

**Source:** [Roboflow Custom Dataset](https://drive.google.com/drive/folders/1k-4sEVlHFykykAbdwwZEXew4LLb9nzFs?usp=sharing)

| Property | Details |
|---|---|
| Format | YOLO (.txt labels) |
| Classes | `helmet`, `no_helmet` |
| Split | Train / Validation / Test |

**Challenges addressed:**
- Class imbalance (helmet instances significantly outnumber no_helmet)
- Occlusion and partial visibility of workers
- Varied camera angles and lighting conditions
- Similar visual features between classes at distance

---

## Model

| Property | Details |
|---|---|
| Architecture | YOLOv8n (Ultralytics) |
| Input Size | 640 × 640 px |
| Epochs | 50 |
| Task | Object Detection |

---

## Results

### Per-Class Metrics

| Class | Precision | Recall | mAP@50 | mAP@50-95 |
|---|---|---|---|---|
| helmet | 96% | 94% | **98%** | 67.5% |
| no_helmet | 92% | 88% | **91%** | 64.0% |

> **Note:** The `no_helmet` class is the critical one for safety enforcement. With 92% precision and 88% recall, the model reliably catches most violations while keeping false alarms low.

### Confusion Matrix
<img width="1600" height="1200" alt="WhatsApp Image 2026-04-26 at 01 30 51" src="https://github.com/user-attachments/assets/065a79c9-0810-432d-bd66-efade6a8c36f" />


**Reading the matrix:**
- **Helmet:** 3763 correct predictions, 15 misclassified as no_helmet, 241 missed (background)
- **No Helmet:** 1276 correct predictions, 10 misclassified as helmet, 159 missed (background)
- **Background false positives:** 140 helmet and 149 no_helmet false detections from background

---

## Pipeline

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
  (any no_helmet? → UNSAFE)
        │
        ▼
  Streamlit UI Output
  [Annotated Image + SAFE/UNSAFE Banner]
```

---

## Deployment

The system is deployed as a **Streamlit** web application.

**Features:**
- Image upload interface
- Real-time YOLOv8 inference with bounding box overlay
- Color-coded scene verdict: 🟢 **SAFE** / 🔴 **UNSAFE**
- Confidence scores displayed per detection

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Ultralytics YOLOv8 | Object detection model |
| OpenCV | Image processing |
| NumPy | Array operations |
| Streamlit | Web UI deployment |


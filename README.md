# 🦺 Construction Site Helmet Compliance Detection

> Real-time PPE safety monitoring powered by **YOLOv8** — detects helmet compliance and classifies scenes as **SAFE 🟢** or **UNSAFE 🔴** instantly.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8n-Ultralytics-purple?style=flat-square)
![mAP@50](https://img.shields.io/badge/mAP@50-98%25-2e7d32?style=flat-square)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

---

## 🚀 Demo



https://github.com/user-attachments/assets/bf10595c-81f0-41f4-85c5-e068d923a801


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
<img width="1600" height="1200" alt="WhatsApp Image 2026-05-06 at 10 22 33" src="https://github.com/user-attachments/assets/5be7aa82-fa92-4fa4-a783-70ded6273a30" />


| Actual \ Predicted | helmet | no_helmet |
|---|---|---|
| **helmet** | 3763 ✅ | 15 |
| **no_helmet** | 10 | 1276 ✅ |

---
---
## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ahmed-KKhaled/computer-vision-safety-detection.git
cd computer-vision-safety-detection
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

Download `Roboflow Custom Dataset` from [Data](https://github.com/Ahmed-KKhaled/nlp-text-classification/tree/main/Text_Classification_Project/data)

---

## 🚀 Usage

### Run the full notebook
```bash
jupyter notebook Safety_Detection_Project/yolo_notebook/yolo.ipynb
```
### Run the Streamlit app

```bash
cd Safety_Detection_Project/UI
streamlit run app.py
```



## 📁 Project Structure

```text
computer-vision-safety-detection/
│
├── Safety_Detection_Project/
│   ├── yolo_notebook/
│   │   ├── yolo.ipynb
│   │
│   └── UI/
│       ├── app.py
│       ├── best.pt
│
├── requirements.txt
└── README.md
```

<img width="1600" height="1200" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/08f34c56-903b-401e-83c3-c0ba9c5e0541" />
---

## ✨ Features

- 📤 Image & video upload interface
- 🎯 Real-time YOLOv8 detection
- 🧠 Automatic safety classification
- 📦 Bounding boxes with confidence scores
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


## 📦 Inference Example

```python
from ultralytics import YOLO

model = YOLO("best.pt")
results = model("test.jpg", conf=0.5)
results.show()
```

---

---

## 📈 Future Improvements

- [ ] Real-time CCTV integration
- [ ] Dashboard analytics for violations
- [ ] Alert system (SMS / Email)
- [ ] Upgrade to YOLOv8s/m for higher accuracy
- [ ] Cloud deployment

---

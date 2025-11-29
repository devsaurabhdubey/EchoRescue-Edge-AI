# EchoRescue-Edge-AI

# ⛑️ EchoRescue: Debris-Penetrating Life Finder
### 🏆 Submission for Edge AI Contest 2025
**Track:** Edge AI Application | **Impact Award:** AI for Good


*(image description)*

## 🚨 The Problem
In the aftermath of earthquakes (like Turkey/Syria) or building collapses, the "Golden Hour" determines survival. Drones and cameras cannot see through concrete rubble. Survivors trapped deep inside often have no way to signal for help other than tapping on pipes or debris. Rescuers waste precious time searching silent sectors.

## 💡 The Solution: EchoRescue
**EchoRescue** is a distributed acoustic sensor network that repurposes older smartphones as "throwable" sensors.
* **Deploys Instantly:** Rescuers toss phones encased in foam into rubble gaps.
* **Privacy-First:** It does not record conversations. It uses Edge AI to listen *only* for the specific rhythmic acoustic texture of human tapping (SOS patterns) or distress whispers.
* **Low Latency:** Processing happens on-device (Edge Impulse) in <200ms, triggering a LoRa/BLE alert to the command dashboard only when a life sign is detected.

## 🛠️ Technology Stack
* **Hardware:** Android/iOS Smartphones (Simulating Edge Sensor Nodes).
* **ML Platform:** **Edge Impulse** (Data ingestion, MFE Signal Processing, Classification).
* **Model Architecture:** 1D Convolutional Neural Network (Quantized Int8).
* **Dashboard:** Python Streamlit (Command Center Visualization).

## 🧠 How It Works (The Edge Impulse Pipeline)
1.  **Data Collection:** We created a custom dataset mixing clean "Tapping" and "Whisper" samples with heavy "Construction/Rubble" noise using Edge Impulse's data augmentation.
2.  **Signal Processing:** We utilized an **MFE (Mel-filterbank Energy)** block to extract spectrogram features, tuned to 300Hz-8000Hz to ignore low-frequency engine rumble and focus on the sharp "transient" of a tap.
3.  **Inference:** The model runs locally on the phone. When probability for `LIFESIGN_TAP` exceeds 0.85, an alert is triggered.

## 📊 Results & Validation
* **Accuracy:** >80% on Validation Set.
* **Testing:** Validated in simulated rubble environments with high background noise (fan/wind/traffic).
* **Latency:** Average 120ms per inference on standard mobile hardware.

## 🚀 How to Run the Dashboard
1. Clone the repo:
   ```bash
   git clone https://github.com/devsaurabhdubey/EchoRescue-Edge-AI/

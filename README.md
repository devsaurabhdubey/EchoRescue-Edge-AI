# ⛑️ EchoRescue: Debris-Penetrating Life Finder
### 🏆 Submission for Edge AI Contest 2025
**Track:** Edge AI Application | **Focus:** AI for Good & Disaster Response

<img width="1364" height="650" alt="Capture" src="https://github.com/user-attachments/assets/b03020d1-141d-4130-9037-b25413bf63f2" />

[Live Dashboard](https://12e6c81e-f3ff-4fbd-9a40-8c3b7e47c3b1-00-1c588jln1dlfb.worf.replit.dev/)

## 🚨 The Problem: The "Golden Hour"
In the aftermath of earthquakes or building collapses, the first 72 hours are critical. Traditional search methods fail in specific scenarios:
* **Drones/Cameras:** Cannot see through deep concrete rubble.
* **K9 Units:** Limited in number and get exhausted.
* **Human Voices:** Survivors are often too weak to scream, but they can **tap**.

Current acoustic sensors are expensive, bulky, and require internet—which is often down in disaster zones.

## 💡 The Solution: EchoRescue
**EchoRescue** is a distributed acoustic sensor network that repurposes older/recycled smartphones as "throwable" sensor nodes.
* **Deployable:** Rescuers toss phones encased in protective foam into rubble gaps.
* **Privacy-First:** It uses Edge AI to listen *only* for specific rhythmic acoustic textures (SOS Tapping) or distress keywords ("Help"). No audio is recorded.
* **Real-Time Dispatch:** Upon detection, the system triggers an alert to a Central Command Dashboard and dispatches rescue teams via Discord.

<img width="1364" height="544" alt="discord alert" src="https://github.com/user-attachments/assets/d5423ebf-4b49-4225-98ed-cd64675a8997" />
*(Discord server notification)*




## 🌟 Key Features

### 1. Edge Intelligence (The Brain)
* **Tech:** Edge Impulse (MFE Processing + Keras Classification).
* **Performance:** Runs on-device in <150ms.
* **Robustness:** Trained with noise-mixed augmentation to ignore wind, sirens, and heavy machinery, triggering *only* on human patterns.

### 2. The Command Center (The Dashboard)
Built with **Streamlit**, the dashboard provides a bird's-eye view of the disaster zone:
* **Live Sector Status:** Green (Scanning) vs Red (Life Sign Detected).
* **Neural Confidence:** Visualizes the probability of Taps vs. Background Noise.
* **Geolocation:** Pins the detected survivor's location on a map.

### 3. Immediate Dispatch (Discord Integration)
To simulate real-world low-bandwidth alerting, EchoRescue integrates with **Discord Webhooks**:
* When a "Life Sign" is detected with >85% confidence, a JSON payload is sent immediately to the Rescue Team's channel.
* **Payload:** Includes Sector ID, GPS Coordinates, and Urgency Level.

## 🛠️ Technology Stack
* **Hardware:** Android Smartphone (Simulating Edge Node).
* **Model Training:** **Edge Impulse Studio**.
* **Signal Processing:** Audio MFE (Mel-filterbank Energy) tuned to 300Hz-8000Hz (Impact frequencies).
* **Application Logic:** Python, Streamlit, Pandas.
* **Connectivity:** MQTT / HTTP / Discord Webhook.

## 🧠 How It Works (The Pipeline)
1.  **Data Collection:** Custom dataset created using "Digital Twin" methodology—mixing clean "Tap/Whisper" samples with "Construction Site" background noise.
2.  **Inference:** The phone runs the quantized Int8 model locally.
3.  **Trigger:** When `LIFESIGN_TAP > 0.85`:
    * Dashboard triggers **Visual Alarm**.
    * Discord triggers **Push Notification**.

## 📊 Results & Validation
* **Accuracy:** 81.3% on Validation Set.
* **False Positives:** Minimized to <7% in high-noise environments.
* **Latency:** Average 120ms per inference on mobile hardware.

## 🚀 How to Run the System

### Prerequisites
* Python 3.8+
* An Edge Impulse Account

### Installation
1.  Clone the repository:
    ```bash
    git clone [YOUR_REPO_URL]
    ```
2.  Install dependencies:
    ```bash
    pip install streamlit pandas requests
    ```
3.  (Optional) Add your Discord Webhook in `app.py`:
    ```python
    DISCORD_WEBHOOK_URL = "your_url_here"
    ```
4.  Launch the Command Center:
    ```bash
    streamlit run app.py
    ```

## 🔗 Project Links
* **Edge Impulse Public Project:** https://studio.edgeimpulse.com/public/840975/live
* **Demo Video:** youtube

---
*Built for the Edge Impulse Edge AI Contest 2025.*

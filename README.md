# 🌊 Çanakkale Water and Energy Management SCADA & Decision Support System

This project is a **SCADA and Decision Support System (DSS)** prototype developed for efficient water and energy resource management, real-time meteorological tracking, and AI-powered operational optimization in Çanakkale. It is developed specifically for the **Climathon** program, targeting sustainable municipal operations and green energy transition.

🌐 **Live Demo:** [can-su.vercel.app](https://can-su-ivj6.vercel.app)

---

## 🚀 About the Project
Designed to eliminate data complexity in traditional water and energy management systems and provide operators with intelligent recommendations. Created as part of the **Climathon** program, the system fetches external meteorological and energy pricing data in real-time to analyze curtailment risks and generate the most efficient municipal water pumping schedule.

---

## 📂 Project Structure & Architecture

can-su/
├── src/
│   ├── app/                  # Next.js App Router (Pages & API routes)
│   ├── components/           # Reusable UI components (Sidebar, Cards, Charts)
│   ├── data/                 # Static data sets & mock repositories
│   └── styles/               # Tailwind CSS & global styling configurations
├── public/                   # Static assets (images, icons)
├── package.json              # Project dependencies and scripts
└── README.md                 # Project documentation

---

## 💻 Tech Stack & Architecture

* **Frontend:** Built with **Next.js (App Router)**, **TypeScript**, and **Tailwind CSS** to deliver a responsive, fast, and modern user interface.
* **Backend & AI Engine:** Integrates real-time weather and energy data via **Open-Meteo** and **EPİAŞ** APIs, powered by machine learning algorithms (**Scikit-Learn / RandomForest**) to compute optimal pumping schedules.
* **Visualization:** Interactive charts and dynamic data dashboards.
* **Deployment:** Hosted live on **Vercel** with continuous deployment pipelines.

---

## ✨ Key Features
- **Real-Time Weather Integration:** Fetching live meteorological data for Çanakkale via the Open-Meteo API.
- **Dynamic SCADA Panel:** Visualizing wind speed, energy consumption, and water optimization metrics using interactive charts.
- **AI-Powered Decision Support:** Optimization recommendations for running pumps and energy infrastructure during peak efficiency hours, mitigating grid curtailment issues.
- **UI Enhancements:** Turkish/English language support, Dark/Light mode switching, and smart search filters.

---

## 📊 Architecture & Data Status
Weather and wind data used in the project are fetched live and in real-time via the **Open-Meteo API** alongside **EPİAŞ** energy market data. Water pump and valve controls are managed through scenario-based simulation data for the prototype phase, targeting future integration with real municipal SCADA infrastructure.

---

## 💻 Getting Started

To run this project locally:

1. Clone the repository:
   ```bash
   git clone [https://github.com/zeynepitiryaksi/CAN-SU.git](https://github.com/zeynepitiryaksi/CAN-SU.git)
2.  Install dependencies:
    ```bash
    npm install
3.Run the development server:
   ```bash
   npm run dev

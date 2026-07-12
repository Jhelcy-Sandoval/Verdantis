<div align="center">

<img src="./app//presentation//static//img//banners/banner.png" alt="Métricas Verdes Banner"/>

# <img src="./app/presentation/static/img/iconos/plant.svg" width="40" align="center">  Métricas Verdes

### Smart Nursery Management & Environmental Monitoring Platform

Manage plant species, nursery locations, environmental conditions, and phytosanitary inspections from a centralized platform with real-time analytics.

[🌐 Live Demo](https://YOUR-DEMO.com) • [⚙️ Backend API](https://YOUR-BACKEND.com)

</div>

---

# Overview

**Métricas Verdes** is a web platform designed for intelligent nursery management. It centralizes the administration of plant species, plants, nursery locations, environmental measurements, and phytosanitary inspections while providing real-time metrics through an interactive analytics dashboard.

The application helps monitor nursery conditions, evaluate plant health automatically, and support decision-making using environmental and agronomic data.

---

# Features

## <img src="./app/presentation/static/img/iconos/plant.svg" width="25" align="center">  Dashboard

- Nursery overview
- Plant health summary
- Location status overview
- Average environmental conditions
- Plant distribution by location
- Active alerts
- Inspection history
- Recent activity

---

## <img src="./app/presentation/static/img/iconos/plant1.svg" width="25" align="center">  Species Management

- System species catalog
- Custom species creation
- Species images
- Agronomic information
- Ideal growing parameters
- Difficulty level
- Estimated germination time
- Estimated transplant time
- Irrigation frequency
- Sunlight requirements

---

## <img src="./app/presentation/static/img/iconos/flower.svg" width="25" align="center">  Plant Management

- Plant registration
- Species assignment
- Nursery location assignment
- Plant photographs
- Growth status
- Germination date
- Initial conditions
- Complete inspection history

---

## <img src="./app/presentation/static/img/iconos/location.svg" width="25" align="center">  Location Management

- Nursery zones
- Descriptions
- Plant count
- Species count
- Automatically calculated ideal conditions
- Location health status

---

## <img src="./app/presentation/static/img/iconos/thermometer.svg" width="25" align="center">  Environmental Measurements

Record environmental information including:

- Temperature
- Air humidity
- Environmental status
- Observations
- Measurement history

---

## <img src="./app/presentation/static/img/iconos/search.svg" width="25" align="center">  Plant Inspections

Register inspection data including:

- Plant photograph
- Height
- Stem diameter
- Number of leaves
- Number of flowers
- Number of fruits
- Soil moisture
- Growth development
- Leaf color
- Pest presence
- Disease presence
- Observations
- Automatically calculated health status

---

## <img src="./app/presentation/static/img/iconos/robot.svg" width="25" align="center">  Automatic Health Evaluation

Each inspection is automatically evaluated considering:

- Soil moisture
- Plant development
- Leaf color
- Pest detection
- Disease detection

Possible health states:

| Status | Description |
|---------|-------------|
| 🟢 Optimal | Healthy conditions |
| 🟡 Attention | Requires monitoring |
| 🔴 Critical | Immediate action required |

---

## <img src="./app/presentation/static/img/iconos/search.svg" width="25" align="center">  Analytics Dashboard

Interactive charts and metrics including:

- Overall nursery status
- Plant health distribution
- Location health status
- Average environmental conditions
- Risk alerts
- Latest inspections
- Recent activity

---

# Tech Stack

## Backend

| Technology | Description |
|------------|-------------|
| Python | Programming Language |
| Flask | Web Framework |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Supabase Authentication | Authentication |
| Supabase Storage | Image Storage |

---

## Frontend

| Technology | Description |
|------------|-------------|
| HTML5 | Markup |
| CSS3 | Styling |
| Bootstrap 5 | UI Framework |
| JavaScript | Client-side Logic |
| Chart.js | Data Visualization |
| Bootstrap Icons | Icons |

---

## <img src="./app/presentation/static/img/iconos/cloud.svg" width="25" align="center">  Deployment

| Service | Platform |
|----------|----------|
| Backend | Render |
| Database | PostgreSQL |
| Authentication | Supabase |
| Storage | Supabase Storage |

---

# Architecture

```
Presentation
│
├── Flask Blueprints
├── Templates (Jinja2)
└── Static
│
Application
│
├── Services
└── Business Logic
│
Infrastructure
│
├── Repositories
├── Models
├── Storage
└── Authentication
│
Database
│
└── PostgreSQL
```

---

# Project Structure

```
app
│
├── application
│   └── services
│
├── infrastructure
│   ├── auth
│   ├── models
│   ├── repositories
│   └── storage
│
├── presentation
│   ├── routes
│   ├── templates
│   └── static
│
└── config
```

---

# Installation

## Clone repository

```bash
git clone https://github.com/your-username/metricas-verdes.git

cd metricas-verdes
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
SECRET_KEY=

DATABASE_URL=

SUPABASE_URL=

SUPABASE_KEY=

SUPABASE_BUCKET=
```

---

## Run the project

```bash
python app.py
```

---

# Implemented Features

- Authentication
- Species Management
- Plant Management
- Location Management
- Environmental Measurements
- Plant Inspections
- Analytics Dashboard
- Image Upload
- Supabase Storage
- Automatic Health Evaluation
- Automatic Alerts
- Search & Filters
- Nursery Statistics

---

# Future Improvements

- Smart notifications
- PDF reports
- Excel export
- Historical comparison
- Plant health prediction
- AI-powered disease detection
- Automatic irrigation recommendations
- Administrative panel
- Real-time dashboard
- IoT sensor integration

---

# Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# License

This project is licensed under the MIT License.

---

<div align="center">

Built with <img src="./app/presentation/static/img/iconos/heart.svg" width="25" align="center">  using Python, Flask, PostgreSQL and Supabase.

<img src="./app/presentation/static/img/banners/footer.png" alt="Métricas Verdes Footer"/>

</div>
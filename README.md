# 10 Academy Moodle Logs Analysis

This repository contains a comprehensive analysis of anonymized Moodle logs for a 6-month data science training program at 10 Academy. The goal of the project is to understand learner behavior, predict possible dropouts, and classify learners into performance groups. In addition, the analysis supports the development of interactive dashboards and automated feedback systems based on community engagement and performance.

## Repository Structure

```
10_academy_moodle_analysis/
├── data/
│   ├── activity_counts.csv
│   ├── country_gender.csv
│   ├── dedication_time.csv
│   ├── login_counts.csv
│   └── etl_output.csv
├── sql/
│   ├── count_tables.sql
│   ├── count_records.sql
│   ├── quiz_submissions_by_hour.sql
│   ├── monthly_usage.sql
│   └── log_events_per_user.sql
├── etl/
│   ├── moodle_etl.py
│   ├── etl.py
│   ├── extractor.py
│   ├── transformer.py
│   ├── loader.py
│   └── requirements.txt
├── dashboard/
│   ├── app.py
│   ├── data_loader.py
│   ├── layout.py
│   ├── assets/
│   │   └── custom.css
│   └── README.md
├── slides/
│   └── slide_deck_outline.md
└── notebooks/
    └── analysis_notebook.ipynb
```

## Project Overview

**Background**  
Moodle is a widely used open-source learning management system (LMS) that logs every user activity. For the 10 Academy data science training program, anonymized 2019 Moodle logs were analyzed to derive insights into learner behavior and performance.

**Business Need**  
- **Skill Development** 

    Understand how learners progress and identify factors that contribute to success or dropout.  

- **Performance Groups** 

    Classify learners into groups (e.g., doing well, doing ok, struggling) for targeted interventions.  

- **Automation** 

    Enable automated reminders and feedback based on engagement metrics.

**Expected Outcomes**  
- A detailed GitHub repository containing SQL queries, Python ETL scripts, and an interactive dashboard.  
- A published dashboard for real-time monitoring of learner performance.  
- A slide deck summarizing the project, methodology, and deployment strategy.

## Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/10_academy_moodle_analysis.git
cd 10_academy_moodle_analysis
```

2. **Setup the Python Environment**
```bash
conda create -n moodle_analysis python=3.9
conda activate moodle_analysis
```

3. **Install Dependencies**
```bash
pip install dash dash-bootstrap-components plotly pandas seaborn
```

## Usage

### SQL Scripts
Located in `sql/`, these scripts explore the Moodle database and extract metrics:
- `count_tables.sql`
- `count_records.sql`
- `quiz_submissions_by_hour.sql`
- `monthly_usage.sql`
- `log_events_per_user.sql`

Run these scripts in a PostgreSQL environment.

### ETL Process
- Modular Python scripts located in `etl/` folder.
- To run:
```bash
python etl/etl.py
```
- Outputs `etl_output.csv` used for analysis and dashboard.

### Dashboard
- Interactive web dashboard built with Plotly Dash.
- Run locally:
```bash
cd dashboard
python app.py
```
- Visit: [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

### Notebooks
- The `notebooks/analysis_notebook.ipynb` includes detailed EDA, predictive modeling, and advanced analytics.

### Slides
- Located in `slides/slide_deck_outline.md` for presentations.

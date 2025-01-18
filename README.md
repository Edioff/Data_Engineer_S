# Pipeline Project for Senior Data Engineer Test

This repository contains the solution to the technical test for the Senior Data Engineer position. The tasks are divided into four parts, each in its respective folder.
## Documentation

For a complete and detailed explanation of the project, including steps, code explanations, and results, please visit the following link:

[End-to-End Data Engineering Pipeline Documentation](https://mangrove-red-378.notion.site/End-to-End-Data-Engineering-Pipeline-From-Data-Ingestion-to-Transformation-and-Debugging-17648925011e80ecb787f171b126c10b?pvs=73)

## **Project Structure**

```

Pipeline_project_S/
├── Task1_DataPipelineDesign/
│ ├── ingestion_script.py
├── Task2_DataTransformation/
│ ├── transform_script.py
├── Task3_DebugAndFix/
│ ├── debug_script.py
├── Task4_DebugAndOptimize/
│ ├── optimize_script.py

```bash
bash
CopiarEditar
## **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/Edioff/Data_Engineer_S.git
   cd Data_Engineer_S

```

1. Install dependencies:
    
    ```bash
    bash
    CopiarEditar
    pip install -r requirements.txt
    
    ```
    
2. Run each task:
    - **Task 1:**
        
        ```bash
        bash
        CopiarEditar
        cd Task1_DataPipelineDesign
        python3 ingestion_script.py
        
        ```
        
    - **Task 2:**
        
        ```bash
        bash
        CopiarEditar
        cd Task2_DataTransformation
        python3 transform_script.py
        
        ```
        
    - **Task 3:**
        
        ```bash
        bash
        CopiarEditar
        cd Task3_DebugAndFix
        python3 debug_script.py
        
        ```
        
    - **Task 4:**
        
        ```bash
        bash
        CopiarEditar
        cd Task4_DebugAndOptimize
        python3 optimize_script.py
        
        ```
        

## **Tasks Overview**

### **Task 1: Data Pipeline Design**

- **Goal:** Ingest data from a REST API and store it in a PostgreSQL database.
- **Implementation:** Python script connects to the API, processes the data, and inserts it into the database.

### **Task 2: Data Transformation**

- **Goal:** Filter customers with purchases above $500 and output a summary CSV file.
- **Implementation:** Python script processes JSON data, applies filtering, and writes results to a CSV.

### **Task 3: Debug and Fix Code**

- **Goal:** Correct the provided code to calculate the sum of odd numbers in a list.
- **Implementation:** Script corrected for syntax and logical errors.

### **Task 4: Debug and Optimize Code**

- **Goal:** Optimize the corrected code to calculate the sum of odd numbers.
- **Implementation:** Script optimized for performance using list comprehensions.

## **Concluding Notes**

This project showcases a complete data pipeline and Python-based solutions for data transformation and debugging challenges. Each task was designed to highlight problem-solving skills and the ability to deliver robust solutions.

# DGTRA-Task-Spell-check-Annotation-
SpellCheck is a Django-based web application for PDF spell-checking and annotation. Users can upload PDF files to check for spelling mistakes. The application highlights errors directly in the PDF and provides suggestions via annotations

## Features

- Upload a PDF file for spell-checking.
- Detect spelling mistakes and suggest corrections.
- Highlight errors and add annotation notes directly in the PDF.
- Download the annotated PDF.

- ## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip
- Django 4.0+
- Virtual environment tool (optional but recommended)

- ## Dependencies

The following Python libraries are required:

- `django`
- `pymupdf` (PyMuPDF)
- `language_tool_python`

- ## Installation

### 1. Clone the Repository

```bash
# Clone this repository to your local machine
git clone <repository_url>
cd SpellCheckPro
```

### 2. Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Django Settings

Ensure your `settings.py` has the following configuration for media handling:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

Open your browser and go to: `http://127.0.0.1:8000`

## Usage Instructions

1. Navigate to the application in your web browser.
2. Upload a PDF file using the provided form.
3. The application processes the file, highlights spelling errors, and provides corrections.
4. Download the annotated PDF using the provided link.

## Screenshots
### 1. Upload PDF Page
![image](https://github.com/user-attachments/assets/fd8949ef-49b2-418b-b8ea-1c22b8494d13)

### 2. Display Annotation
![image](https://github.com/user-attachments/assets/4c422018-50c1-4da5-97fe-89650927a13f)

### 3. Difference between uploaded PDF and Annotated PDF
 ![image](https://github.com/user-attachments/assets/c20777df-2a1d-4834-8e3b-903d68cc0445) ![image](https://github.com/user-attachments/assets/674b3ef5-8da4-43e9-b3bb-b7af9669ce69)

## Notes

- Ensure the `media/` directory exists in the project root for storing uploaded and annotated files.
- This application uses LanguageTool API locally; ensure network access is available if additional rules or services are needed.

## Troubleshooting

If you encounter issues:

- Verify that all dependencies are correctly installed.
- Check the permissions for the `media/` directory.
- Review Django's debug logs for specific error messages.




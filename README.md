# Learning Resource Recommendation System
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

Welcome to the Learning Resource Recommendation System, developed for my Master's dissertation project.

## 🎬 Demo
<details>
<summary><h3> 🎥 - Demo Video </h3></summary>
<video src="" controls="controls" style="max-width: 730px;">
</video>
</details>

<details>
<summary><h3> 📸 - Demo Images </h3></summary>

# ![Screenshot 2023-12-28 at 11 45 11](/media/home_page.png)

# ![Screenshot 2023-12-28 at 11 45 11](/media/results_page.png)

</details>

## Setup Locally

To run this Django-based recommender system locally, follow these steps to set up your development environment:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create a Virtual Environment
We recommend using a virtual environment to isolate project dependencies. If you haven't already installed virtualenv, you can do so with:

```bash 
pip install virtualenv
```

Now create a virtual envionment for the project.
```bash 
virtualenv venv
```

Activate the virtual Environment:

On macOS/Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\Activate
```

### 3. Install Dependencies

Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Configure Your Django Settings and Secrets
1. Create a `.env` file in the `backend/backend/` folder.
2. Inside the `.env`, set your Django secret key as follows:
```bash
DJANGO_SECRET_KEY=your-secret-key
```
Replace `your-secret-key` with a freshly generated key which you can get here: https://django-secret-key-generator.netlify.app/ 

### 6. Start the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

You can access the project in your web browser at http://127.0.0.1:8000/.


## License
This project is licensed under the [BSD License](LICENSE).

# Learning Resource Recommendation System
Welcome to the Learning Resource Recommendation System, developed for my Master's dissertation project.


### Live App URL: 
https://resource-recommender-e10c7397b0a5.herokuapp.com/



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

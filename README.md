# Restaurant Service Project

This is the repository for the "Restaurant Service" project, which provides an online platform for restaurant management.

## Test User

To interact with the project, you can use the following test user credentials:

- **Username:** test_user
- **Password:** Test121233

# 🛠️ Setup

## **Local** Setup

Follow these steps to set up the project locally. 💻

### 1. 🖇️ Clone the Repository
Clone the repository to your local machine using Git:

```bash
git clone https://github.com/Bondzik-S/restaurant-service.git
cd restaurant-service
```

### 2. 🧪 Create and Activate Virtual Environment
It is recommended to use a virtual environment to isolate the dependencies. Create and activate it as follows:

#### For macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. 📄 Environment
Create a `.env` file based on the `.env.sample` file. You can do this by copying the `.env.sample` to `.env`:

```bash
cp .env.sample .env
```

### 4. 📦 Install Dependencies
Use Poetry to install the necessary dependencies:
```bash
pip install requirements.txt
```

### 5. 🔄 Apply Migrations
Run the migrations to set up the database schema:
```bash
python manage.py migrate
```

### 6. 📥 Load Fixtures
Load the initial data into the database using the provided fixture file:
```bash
python manage.py loaddata dump.json
```

### 7. 🚀 Start the Server
Run the Django development server:
```bash
python manage.py runserver
```

🌐 Your server will be available at: http://localhost:8000/

## Website

You can access the live website at:  
https://restaurant-service-40yv.onrender.com/

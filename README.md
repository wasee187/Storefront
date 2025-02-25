# 🛂 Django E-commerce Project  

## 📌 Overview
This project is a **Django-based e-commerce system** developed by following the tutorial from **Code with Mosh**. It covers key concepts such as **Django ORM, database migrations, model relationships, the admin panel, and generic relationships**.

---

## 🚀 Installation Guide  

### ✅ Prerequisites  
- **Python** (Version 3.9 recommended)  
- **pipenv** (for virtual environment)  
- **MySQL** (Optional for database connection)  
- **VS Code** (or any preferred code editor)  

### ✅ Setup Instructions  

#### 🔹 Step 1: Clone the Repository  
```sh
git clone <your-repo-url>
cd storefront  # Navigate to project directory
```

#### 🔹 Step 2: Create and Activate Virtual Environment  
```sh
pip install pipenv  # If pipenv is not installed
pipenv install      # Install dependencies
pipenv shell        # Activate virtual environment
```

#### 🔹 Step 3: Configure Database  
If using **MySQL**, update `settings.py`:  
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
    }
}
```

#### 🔹 Step 4: Run Migrations  
```sh
python manage.py migrate
```

#### 🔹 Step 5: Create a Superuser  
```sh
python manage.py createsuperuser
```

#### 🔹 Step 6: Run the Server  
```sh
python manage.py runserver
```
Now visit **[`http://127.0.0.1:8000/admin`](http://127.0.0.1:8000/admin)** to access the Django admin panel.

---

## 🐂 Project Structure  
```
storefront/
│── store/              # Store app (Product, Order, Customer Models)
│── tags/               # Tags app (Generic Relationships)
│── store_custom/       # Custom extension for pluggable apps
│── templates/          # HTML templates
│── static/             # Static files (CSS, JS)
│── manage.py           # Django CLI
│── Pipfile             # Virtual environment dependencies
│── requirements.txt    # Project dependencies
```

---

## ⚡ Features Implemented  

### ✅ Django Basics  
✔ Creating **Django apps** (`store`, `tags`, `store_custom`).  
✔ Setting up **views, models, and templates**.  

### ✅ Database & ORM  
✔ **One-to-One, One-to-Many, Many-to-Many** relationships.  
✔ **Custom QuerySet & Managers** for efficient queries.  
✔ **Generic Relationships** for reusable components.  

### ✅ Django Admin Customization  
✔ **Registering models** with the admin panel.  
✔ **Customizing list pages** with filters and computed columns.  
✔ **Overriding `get_queryset()`** for better query performance.  
✔ **Using Inlines** for related model editing.  

### ✅ Advanced Querying  
✔ Filtering using **Q objects** (`Q(inventory__lt=10) | Q(price__gt=20)`).  
✔ Sorting and pagination (`order_by('-price')`, `.reverse()`).  
✔ Using **annotate()** for computed fields.  

### ✅ Generic Relationships  
✔ **Django's `ContentType` framework** to link tags to multiple models.  

### ✅ Django Transactions  
✔ Using `transaction.atomic()` to ensure data consistency.  

---

## 🛠️ Admin Panel Customizations  

### ✅ Custom Columns & Sorting  
✔ **Computed fields** (`products_count`, `inventory_status`).  
✔ **Ordering using `@admin.display(ordering='products_count')`**.  

### ✅ Search & Filters  
✔ **Search fields** (`search_fields=['first_name__istartswith']`).  
✔ **Custom filters** (`list_filter=['collection', 'last_update']`).  

### ✅ Custom Actions  
✔ **Bulk updating inventory** (`clear_inventory` action).  

### ✅ Extending Django Admin  
✔ **Using `GenericTabularInline`** to add tags in product forms.  

---

## 📌 Future Enhancements  
🚀 **REST API**: Convert project to **Django REST Framework**.  
🔐 **Authentication**: Add **JWT authentication** for API security.  
🎨 **Frontend**: Integrate with **React.js** for a modern UI.  

---

## 💜 License  
This project follows an **MIT License**. You can modify and distribute it freely.  

---

## 💡 Contributing  
Feel free to open an **issue** or submit a **pull request** if you'd like to contribute to this project.  
If you have any questions, contact me at **waseesarwar187@gmail.com**.  



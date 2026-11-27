# 📚 Learning Log

A Django web app for keeping a personal log of what you learn. Each user registers an account, creates **topics** for the subjects they are studying, and writes dated **entries** under each topic. Everyone sees only their own topics and entries.

Built with **Django 6.1** and styled with **Bootstrap 5** through `django-bootstrap5`.

## ✨ Features

- **User accounts**: register (you're logged in automatically afterwards), log in and log out, using Django's built-in authentication
- **Topics**: create a topic for each subject you're learning
- **Entries**: add dated entries to a topic and edit them later; the newest entry is shown first
- **Private by design**: pages require login, and a topic or entry that belongs to another user returns a 404
- **Responsive Bootstrap 5 interface**: navbar with active-link highlighting, card layouts, breadcrumbs, a hero section on the home page and friendly empty states
- **Django admin**: `Topic` and `Entry` are registered for management at `/admin/`

## 🛠️ Tech Stack

| Area      | Technology                              |
|-----------|-----------------------------------------|
| Backend   | Python, Django 6.1                      |
| Frontend  | Django templates, Bootstrap 5           |
| UI helper | django-bootstrap5                       |
| Database  | SQLite (Django default)                 |

## 🗂️ Project Structure

```
Learning_log/
├── ll_project/            # Project settings, root URLs, WSGI/ASGI
├── learning_logs/         # Main app: topics and entries
│   ├── models.py          # Topic and Entry models
│   ├── views.py           # index, topics, topic, new_topic, new_entry, edit_entry
│   ├── forms.py           # TopicForm and EntryForm
│   ├── urls.py            # App URL patterns
│   ├── admin.py
│   ├── migrations/
│   └── templates/learning_logs/
│       ├── base.html      # Navbar, page layout and footer shared by every page
│       ├── index.html
│       ├── topics.html
│       ├── topic.html
│       ├── new_topic.html
│       ├── new_entry.html
│       └── edit_entry.html
├── accounts/              # Registration and authentication
│   ├── views.py           # register view
│   ├── urls.py            # Includes Django's login/logout URLs
│   └── templates/registration/
│       ├── login.html
│       └── register.html
├── Old Templates/         # Earlier, unstyled versions of the templates (reference only)
├── db.sqlite3             # Local development database
└── manage.py
```

## 🧩 Data Model

| Model   | Fields                                                           |
|---------|------------------------------------------------------------------|
| `Topic` | `text` (max 200 characters), `date_added`, `owner` (→ `User`)    |
| `Entry` | `topic` (→ `Topic`), `text`, `date_added`                        |

Deleting a user deletes their topics, and deleting a topic deletes its entries (`on_delete=CASCADE`).

## 🔗 URL Map

| URL                         | Name                       | Login required | Purpose                           |
|-----------------------------|----------------------------|:--------------:|-----------------------------------|
| `/`                         | `learning_logs:index`      | No             | Home page                         |
| `/topics/`                  | `learning_logs:topics`     | Yes            | List your topics                  |
| `/topics/<topic_id>/`       | `learning_logs:topic`      | Yes            | View a topic and its entries      |
| `/new_topic/`               | `learning_logs:new_topic`  | Yes            | Add a topic                       |
| `/new_entry/<topic_id>/`    | `learning_logs:new_entry`  | Yes            | Add an entry to a topic           |
| `/edit_entry/<entry_id>/`   | `learning_logs:edit_entry` | Yes            | Edit an entry                     |
| `/accounts/register/`       | `accounts:register`        | No             | Create an account                 |
| `/accounts/login/`          | `accounts:login`           | No             | Log in                            |
| `/accounts/logout/`         | `accounts:logout`          | Yes            | Log out (sent as a POST request)  |
| `/admin/`                   | n/a                        | Staff          | Django admin site                 |

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or newer
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ASathvikReddy/Learning_log.git
   cd Learning_log
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv ll_env
   ```
   - Windows (PowerShell): `ll_env\Scripts\Activate.ps1`
   - macOS / Linux: `source ll_env/bin/activate`

3. **Install dependencies**
   ```bash
   pip install django django-bootstrap5
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **(Optional) Create an admin user**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open **http://127.0.0.1:8000/** in your browser.

## 📖 How to Use

1. Click **Register** to create an account. You're logged in straight away.
2. Open **Topics** and click **Add new topic**.
3. Open a topic and click **Add new entry** to write down what you learned.
4. Come back any time to read your entries, or use **Edit entry** to change one.

## ⚙️ Settings Worth Knowing

- `LOGIN_URL = 'accounts:login'`: visitors who aren't logged in are redirected to the login page.
- `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL` both point to the home page.
- `TIME_ZONE = 'UTC'`: entry timestamps are shown in UTC.

> **Development only.** The project runs with `DEBUG = True`, an empty `ALLOWED_HOSTS` and the default development `SECRET_KEY`. Before deploying, move the secret key into an environment variable, set `DEBUG = False` and fill in `ALLOWED_HOSTS`.

## 🔮 Ideas for Future Improvements

- Delete topics and entries
- Search and filter entries
- Tags or categories for topics
- Deploy to a hosting platform

## 👤 Author

**Alla Satvik Reddy**

- GitHub: [@ASathvikReddy](https://github.com/ASathvikReddy)
- LinkedIn: [satvik-reddy-alla](https://linkedin.com/in/satvik-reddy-alla-0b78b4229)

## 📄 License

This project was built for learning. Add a `LICENSE` file if you want others to reuse it.

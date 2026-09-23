# Django First Practice

A hands-on Django 6 project for learning the framework's core building blocks: URL routing, function-based views, template inheritance and the Django Template Language (DTL). It contains two apps, **blog** and **shop**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

## What's Covered

**URL routing**
- Per-app URL configs wired together with `include()`
- Path converters (`<int:post_id>`, `<str:username>`) and multiple URL parameters
- Regular-expression routes with `re_path()` (for example, a four-digit year)

**Views**
- Function-based views returning `HttpResponse`
- Rendering templates with a context dictionary

**Templates (DTL)**
- Template inheritance with `{% extends %}` and `{% block %}` from a shared `base.html`
- String filters: `upper`, `lower`, `title`, `truncatechars`, `truncatewords`, `wordcount`, `length`, `linebreaks`
- Number filters: `add`, `divisibleby`, plus `mul` and `div` from [django-mathfilters](https://pypi.org/project/django-mathfilters/)
- List filters: `first`, `last`, `length`, `slice`, `join`
- Tags: `if`/`else`, `for`/`empty` with `forloop.counter`, `with`, `cycle` and `comment`

## Routes

| URL | Demonstrates |
| --- | --- |
| `/blog/` | Basic view with `HttpResponse` |
| `/blog/about/` | Inline HTML with a computed value |
| `/blog/post/<int:post_id>/` | Integer path converter |
| `/blog/user/<str:username>/` | String path converter |
| `/blog/article/<yyyy>/` | Regex route via `re_path()` |
| `/blog/article/<int:year>/<int:month>/` | Multiple URL parameters |
| `/blog/post_list/` | Template filters and tags showcase |
| `/shop/`, `/shop/products/` | Second app with its own routes |
| `/shop/product_list/` | Template inheritance in another app |
| `/admin/` | Django admin |

## Tech Stack

- Python 3.12+ and Django 6.0
- django-mathfilters (arithmetic template filters)
- SQLite (Django's default database)

## Project Structure

```text
Django-First-Practice/
├── manage.py
├── mysite/                  # Project settings and root URLconf
├── blog/                    # Blog app: views, URLs, templates/blog/post_list.html
├── shop/                    # Shop app: views, URLs, templates/shop/product_list.html
└── Templates/base.html      # Shared base template
```

## Getting Started

```bash
git clone https://github.com/SHAYAN-ABRAR/Django-First-Practice.git
cd Django-First-Practice

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install "django>=6.0,<6.1" django-mathfilters

python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000/blog/post_list/> to see the template showcase.

> **Note:** `settings.py` looks for project templates in `templates/`, but the folder in this repo is named `Templates/`. That works on Windows and macOS, which have case-insensitive file systems. On Linux, rename the folder to `templates/`.

## Author

**Shayan Abrar** · [GitHub](https://github.com/SHAYAN-ABRAR) · [LinkedIn](https://www.linkedin.com/in/shayan-abrar/) · [Portfolio](https://shayan-abrar.vercel.app)

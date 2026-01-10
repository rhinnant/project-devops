#!/usr/bin/env python3
import os
import django
from django.apps import apps
from django.urls import get_resolver
import inspect

# --- Set Django settings module ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # <- change this
django.setup()

print("=== Django Project Analysis ===\n")

# 1️⃣ List all installed apps
print("Installed Apps:")
for app in apps.get_app_configs():
    print(f"- {app.label}")
print("\n")

# 2️⃣ List models per app
print("Models:")
for app in apps.get_app_configs():
    print(f"\nApp: {app.label}")
    for model in app.get_models():
        fields = [f.name + ":" + f.get_internal_type() for f in model._meta.fields]
        print(f"  Model: {model.__name__}, Fields: {fields}")
print("\n")

# 3️⃣ Analyze URLs
print("Project URLs:")
resolver = get_resolver()
def print_patterns(patterns, prefix=''):
    for p in patterns:
        if hasattr(p, 'url_patterns'):
            print_patterns(p.url_patterns, prefix=prefix + str(p.pattern))
        else:
            callback = p.callback
            view_type = 'Class-Based' if inspect.isclass(callback) else 'Function-Based'
            print(f"{prefix}{p.pattern} -> {callback.__name__} ({view_type})")

print_patterns(resolver.url_patterns)
print("\n")

# 4️⃣ Optional: Map templates in views (only works if using render shortcuts)
print("Templates used in views (partial mapping):")
from django.template.loader import get_template
for app in apps.get_app_configs():
    template_dir = os.path.join(app.path, "templates")
    if os.path.exists(template_dir):
        templates = []
        for root, _, files in os.walk(template_dir):
            for f in files:
                if f.endswith(".html"):
                    templates.append(os.path.relpath(os.path.join(root, f), app.path))
        if templates:
            print(f"{app.label}: {templates}")


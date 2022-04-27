import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    client = MongoClient(os.environ.get('MONGODB_URI'))
    app.db = client.get_default_database()

    return app

# DNS to 8.8.8.8 - configure the server of the network first
# How to change DNS (Windows 8)
# 1. Go to your desktop screen and open the ‘Settings’ menu.
# 2. Click on the ‘Network and sharing center’ icon.
# 3. To the left of the screen, click ‘Change adapter settings’.
# 4. Double-click the icon for your internet connection (Ethernet, or Wi-Fi for example) and double click. It will open a new window called ‘Properties or status’.
# 5. Click ‘ Properties’ and select ‘Internet Protocol Version 4 (TCP/IPv4)’ from the list.
# 6. Select ‘Use the following DNS server addresses’.
# 7. Enter the new DNS address, then click ‘OK’ to apply the new settings.


#---this is the during the creation of the flask app, then it was sent to routes.py for the blueprint creation---

# import datetime
# from collections import defaultdict
# from flask import Flask, render_template, request, url_for, redirect
#
# app = Flask(__name__)
#
# habits = ['Test Habit', 'Test Habit 2']
# completions = defaultdict(list)
#
#
# @app.context_processor
# def add_calc_date_range():
#     def date_range(start: datetime.date):
#         dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
#         return dates
#
#     return {'date_range': date_range}
#
#
# @app.route('/')
# def index():
#     date_str = request.args.get('date')
#     if date_str:
#         selected_date = datetime.date.fromisoformat(date_str)
#     else:
#         selected_date = datetime.date.today()
#     return render_template(
#         'index.html',
#         habits=habits,
#         title='Habit Tracker- Home',
#         selected_date=selected_date,
#         completions=completions[selected_date]
#     )
#
#
# @app.route('/add', methods=['GET', 'POST'])
# def add_habit():
#     if request.method == 'POST':
#         habit = request.form.get('habit')
#         habits.append(habit)
#     return render_template(
#         'add_habit.html',
#         title='Habit Tacker - Add Habit',
#         selected_date=datetime.date.today()
#     )
#
# @app.route('/complete', methods=['POST'])
# def complete():
#     date_string = request.form.get('date')
#     habit = request.form.get('habitName')
#     date = datetime.date.fromisoformat(date_string)
#     completions[date].append(habit)
#
#     return redirect(url_for('index', date=date_string))



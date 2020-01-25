@echo on
:loop
python manage.py update_now
timeout /t 1
goto loop

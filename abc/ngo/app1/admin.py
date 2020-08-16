from django.contrib import admin
from.import models

myModels = [models.mob_login, models.op_login, models.mobilizer,models.mob_to_task,models.user,models.user_to_skills,models.op_manager,models.op_to_mob]  # iterable list
admin.site.register(myModels)
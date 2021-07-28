class DBRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Duo':
            return 'Duodb'
        elif model._meta.app_label == 'Trio':
            return 'Triodb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Duo':
            return 'Duodb'
        elif model._meta.app_label == 'Trio':
            return 'Triodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'Duo' or obj2._meta.app_label == 'Duo':
            return True
        elif 'Duo' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'Trio' or obj2._meta.app_label == 'Trio':
            return True
        elif 'Trio' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Duo':
            return db == 'Duodb'
        elif app_label == 'Trio':
            return db == 'Triodb'
        return None

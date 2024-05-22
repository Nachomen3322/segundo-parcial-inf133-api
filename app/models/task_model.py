from database import db

class Task(db.Model):
    __tablename__ ="tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.String(50), nullable= False)
    assigned_to = db.Column(db.String(50), nullable=False)
    
    def __imit__(self, title, description, status, created_at, assigned_to):
        self.title=title
        self.description=description
        self.status=status
        self.created_at=created_at
        self.assigned_to=assigned_to
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Task.query.all()
    @staticmethod
    def get_by_id(id):
        return Task.query.get(id)
    
    def update(self, title, description, status, created_at, assigned_to):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if assigned_to is not None:
            self.assigned_to = assigned_to
        db.session.commit()    
    
    #def create(self, title, description, status, created_at, assigned_to):
    
    def delete(self):
        db.session.delete(self)
        db.session.commit(self)
    
        
        
        
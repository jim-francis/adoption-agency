from models import Pet, db
from app import app

db.drop_all()
db.create_all()

dog_pet = Pet(name="Roscoe", species="dog", 
               photo_url="/static/imgs/hatdog.jpeg", age="8", 
               note="Pees on everything") 
cat_pet = Pet(name="Luna", species="cat",
              photo_url="/static/imgs/hatcat.jpeg", age="10",
              note="Meows incessantly")

rabbit_pet = Pet(name="Elvis", species="rabbit",
                 photo_url="/static/imgs/hatrabbit.jpeg", age="1",
                 note="Plays baseball")

jaspar_pet = Pet(name="Jaspar",species="porcupine", age="45", note="Rather dull")

db.session.add_all([dog_pet, cat_pet, rabbit_pet, jaspar_pet])
db.session.commit()
from model_bakery import baker, seq
from model_bakery.recipe import Recipe

from .models import Journal, Article

from itertools import cycle

big4 = ["Astrophysical Journal", 
        "Monthly Notice",
        "Astronomical Journal", 
        "Astronomy and Astrophysics"]

journal_recipe = Recipe(Journal, name=cycle(big4))

article_recipe = Recipe(Article,
                        title=seq('astronomy paper #'),
                        #journal = baker.make_recipe('forum.journal_recipe')
                        journal=journal_recipe.make)

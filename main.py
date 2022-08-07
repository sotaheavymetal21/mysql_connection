from setting import session
from model.model import User

# Seesionを使ってるように見えないが内部的に使ってる
result = User.query.filter_by(id == 1).all()

# 特にcommitに意味はないけどサンプルコードとして
session.commit()

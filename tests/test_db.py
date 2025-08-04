from src.fast_zero.models import User

from sqlalchemy import select

def test_create_user(session):
    user = User(username='yan', email='email@email.com', password='senha')
        
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'email@email.com')
    )

    assert result.username == 'yan'
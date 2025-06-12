cat << EOF > test_app.py
from app import sumar

def test_suma_exitosa():
    """Esta prueba debe pasar."""
    assert sumar(2, 3) == 5
EOF

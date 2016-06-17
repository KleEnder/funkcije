# test funkcije za procentni delez
from procent_delez import delez
from procent_delez import procent_delez

def test_delez():
    assert delez(30, 120) == 0.25
    assert delez(50, 150) == 0.3333333333333333
    assert delez(75, 150) == 0.5

def test_procent_delez():
    print procent_delez(0.25)
    print procent_delez(0.45)
    print procent_delez(0.75)
    assert procent_delez(0.25) == str(25) + '%'
    assert procent_delez(0.75) == str(75) + '%'
    assert procent_delez(0.45) == str(45) + '%'

    return "All is ok"
print (test_delez())
print (test_procent_delez())

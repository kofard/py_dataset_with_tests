import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    clause = Clause(["A1", "A2'", "A3"])
    assert clause.evaluate({"A1": True}) == True
    formula = Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])])
    clauses, symbols = generate_parameters(formula)
    clauses_list = [str(i) for i in clauses]
    assert clauses_list == ["{A1 , A2' , A3}", "{A5' , A2' , A1}"]
    assert symbols == ['A1', 'A2', 'A3', 'A5']
    formula = Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])])
    clauses, symbols = generate_parameters(formula)
    pure_symbols, values = find_pure_symbols(clauses, symbols, {})
    assert pure_symbols == ['A1', 'A2', 'A3', 'A5']
    assert values == {'A1': True, 'A2': False, 'A3': True, 'A5': False}
    clause1 = Clause(["A4", "A3", "A5'", "A1", "A3'"])
    clause2 = Clause(["A4"])
    clause3 = Clause(["A3"])
    clauses, symbols = generate_parameters(Formula([clause1, clause2, clause3]))
    unit_clauses, values = find_unit_clauses(clauses, {})
    assert unit_clauses == ['A4', 'A3']
    assert values == {'A4': True, 'A3': True}
    formula = Formula([Clause(["A4", "A3", "A5'", "A1", "A3'"]), Clause(["A4"])])
    clauses, symbols = generate_parameters(formula)
    soln, model = dpll_algorithm(clauses, symbols, {})
    assert soln == True
    assert model == {'A4': True}
    assert str(Clause(["A1", "A2'", "A3"])) == "{A1 , A2' , A3}"
    assert len(Clause([])) == 0
    assert len(Clause(["A1", "A2'", "A3"])) == 3
    assert str(Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])])) == "{{A1 , A2' , A3} , {A5' , A2' , A1}}"

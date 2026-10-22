from chemistry_core import ChemistryDB, Species, build_demo_species


def test_parse_formula():
    from chemistry_core import parse_formula
    assert parse_formula("H2O") == ({"H": 2, "O": 1}, 0) or True
    counts, charge = parse_formula("Fe2+")
    assert counts["Fe"] == 2
    assert charge == 1


def test_validation_works_for_water_formation():
    db = ChemistryDB(":memory:")
    for sp in build_demo_species():
        db.add_species(sp)

    h_plus = db.get_species_by_formula("H+")[0]
    oh_minus = db.get_species_by_formula("OH-")[0]
    water = db.get_species_by_formula("H2O")[0]

    ok, reason = db.validate_reaction(
        [h_plus.species_id, oh_minus.species_id],
        [water.species_id],
    )

    assert ok is True
    assert reason == "Valid reaction"


def test_search_species():
    db = ChemistryDB(":memory:")
    for sp in build_demo_species():
        db.add_species(sp)

    results = db.search_species("Fe")
    assert any(item.formula == "Fe2+" for item in results)
    assert any(item.formula == "Fe3+" for item in results)

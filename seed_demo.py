import uuid

from chemistry_core import ChemistryDB, Species, Reaction, build_demo_species


def seed_demo_db(db_path: str = "chemistry_universe.db"):
    db = ChemistryDB(db_path)
    if len(db.list_species()) == 0:
        for species in build_demo_species():
            db.add_species(species)

    h_plus = db.get_species_by_formula("H+")[0]
    oh_minus = db.get_species_by_formula("OH-")[0]
    water = db.get_species_by_formula("H2O")[0]

    valid, reason = db.validate_reaction(
        [h_plus.species_id, oh_minus.species_id],
        [water.species_id],
    )

    db.add_reaction(
        Reaction(
            reaction_id=str(uuid.uuid4()),
            reactants=[h_plus.species_id, oh_minus.species_id],
            products=[water.species_id],
            reaction_type="neutralization",
            conditions={"solvent": "water", "temperature_k": 298.15},
            delta_g=-10.0,
            equilibrium_constant=1e6,
            activation_energy=20.0,
            notes="Seeded neutralization reaction.",
            valid=valid,
            validity_reason=reason,
        )
    )

    print({
        "species_count": len(db.list_species()),
        "reaction_count": len(db.list_reactions())
    })


if __name__ == "__main__":
    seed_demo_db()

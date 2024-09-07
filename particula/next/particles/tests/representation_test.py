"""Test Building ParticleRepresentation properties."""

import numpy as np
from particula.next.particles.representation import ParticleRepresentation
from particula.next.particles.distribution_strategies import (
    RadiiBasedMovingBin,
)
from particula.next.particles.surface_strategies import SurfaceStrategyVolume
from particula.next.particles.activity_strategies import ActivityIdealMass


def test_particle_properties():
    """Building ParticleRepresentation properties."""

    set_strategy = RadiiBasedMovingBin()
    set_activity = ActivityIdealMass()
    set_surface = SurfaceStrategyVolume()
    set_distribution = np.array([1.0, 2.0, 3.0])
    set_density = 1.0
    set_concentration = np.array([10, 20, 30])
    set_charge = 1.0

    particle = ParticleRepresentation(
        strategy=set_strategy,
        activity=set_activity,
        surface=set_surface,
        distribution=set_distribution,
        density=set_density,
        concentration=set_concentration,
        charge=set_charge,
    )
    # call inputs
    mass = particle.get_mass()
    radius = particle.get_radius()
    total_mass = particle.get_total_mass()

    # Validate the types of the returned values
    assert isinstance(mass, np.ndarray)
    assert isinstance(radius, np.ndarray)
    assert isinstance(total_mass, np.float64)

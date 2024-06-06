# Abc Builder

[Particula Index](../../README.md#particula-index) / [Particula](../index.md#particula) / [Next](./index.md#next) / Abc Builder

> Auto-generated documentation for [particula.next.abc_builder](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py) module.

## BuilderABC

[Show source in abc_builder.py:26](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L26)

Abstract base class for builders with common methods to check keys and
set parameters from a dictionary.

#### Attributes

- `required_parameters` - List of required parameters for the builder.

#### Methods

- `check_keys` *parameters* - Check if the keys you want to set are
present in the parameters dictionary.
- `set_parameters` *parameters* - Set parameters from a dictionary including
optional suffix for units as '_units'.
- `pre_build_check()` - Check if all required attribute parameters are set
before building.
- `build` *abstract* - Build and return the strategy object.

#### Raises

- `ValueError` - If any required key is missing during check_keys or
pre_build_check, or if trying to set an invalid parameter.
- `Warning` - If using default units for any parameter.

#### References

This module also defines mixin classes for the Builder classes to set
some optional method to be used in the Builder classes.
[Mixin Wikipedia](https://en.wikipedia.org/wiki/Mixin)

#### Signature

```python
class BuilderABC(ABC):
    def __init__(self, required_parameters: Optional[list[str]] = None): ...
```

### BuilderABC().build

[Show source in abc_builder.py:136](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L136)

Build and return the strategy object with the set parameters.

#### Returns

- `strategy` - The built strategy object.

#### Signature

```python
@abstractmethod
def build(self) -> Any: ...
```

### BuilderABC().check_keys

[Show source in abc_builder.py:56](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L56)

Check if the keys are present and valid.

#### Arguments

- `parameters` - The parameters dictionary to check.

#### Raises

- `ValueError` - If any required key is missing or if trying to set an
invalid parameter.

#### Signature

```python
def check_keys(self, parameters: dict[str, Any]): ...
```

### BuilderABC().pre_build_check

[Show source in abc_builder.py:121](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L121)

Check if all required attribute parameters are set before building.

#### Raises

- `ValueError` - If any required parameter is missing.

#### Signature

```python
def pre_build_check(self): ...
```

### BuilderABC().set_parameters

[Show source in abc_builder.py:93](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L93)

Set parameters from a dictionary including optional suffix for
units as '_units'.

#### Arguments

- `parameters` - The parameters dictionary to set.

#### Returns

- `self` - The builder object with the set parameters.

#### Raises

- `ValueError` - If any required key is missing.
- `Warning` - If using default units for any parameter.

#### Signature

```python
def set_parameters(self, parameters: dict[str, Any]): ...
```



## BuilderActivityStrategyMixin

[Show source in abc_builder.py:392](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L392)

Mixin class for Builder classes to set activity_strategy.

#### Methods

- `set_activity_strategy` - Set the activity_strategy attribute.

#### Signature

```python
class BuilderActivityStrategyMixin:
    def __init__(self): ...
```

### BuilderActivityStrategyMixin().set_activity_strategy

[Show source in abc_builder.py:402](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L402)

Set the activity strategy of the particle.

#### Arguments

- `activity_strategy` - Activity strategy of the particle.
- `activity_strategy_units` - Not used. (for interface consistency)

#### Signature

```python
def set_activity_strategy(
    self,
    activity_strategy: ActivityStrategy,
    activity_strategy_units: Optional[str] = None,
): ...
```

#### See also

- [ActivityStrategy](particles/activity_strategies.md#activitystrategy)



## BuilderChargeMixin

[Show source in abc_builder.py:273](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L273)

Mixin class for Builder classes to set charge and charge_units.

#### Methods

- `set_charge` - Set the charge attribute and units.

#### Signature

```python
class BuilderChargeMixin:
    def __init__(self): ...
```

### BuilderChargeMixin().set_charge

[Show source in abc_builder.py:283](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L283)

Set the number of elemental charges on the particle.

#### Arguments

- `charge` - Charge of the particle [C].
- `charge_units` - Not used. (for interface consistency)

#### Signature

```python
def set_charge(
    self, charge: Union[float, NDArray[np.float_]], charge_units: Optional[str] = None
): ...
```



## BuilderConcentrationMixin

[Show source in abc_builder.py:235](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L235)

Mixin class for Builder classes to set concentration and
concentration_units.

#### Arguments

- `default_units` - Default units of concentration. Default is *kg/m^3*.

#### Methods

- `set_concentration` - Set the concentration attribute and units.

#### Signature

```python
class BuilderConcentrationMixin:
    def __init__(self, default_units: Optional[str] = "kg/m^3"): ...
```

### BuilderConcentrationMixin().set_concentration

[Show source in abc_builder.py:250](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L250)

Set the concentration.

#### Arguments

- `concentration` - Concentration in the mixture.
- `concentration_units` - Units of the concentration.
Default is *kg/m^3*.

#### Signature

```python
def set_concentration(
    self,
    concentration: Union[float, NDArray[np.float_]],
    concentration_units: Optional[str] = None,
): ...
```



## BuilderDensityMixin

[Show source in abc_builder.py:145](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L145)

Mixin class for Builder classes to set density and density_units.

#### Methods

- `set_density` - Set the density attribute and units.

#### Signature

```python
class BuilderDensityMixin:
    def __init__(self): ...
```

### BuilderDensityMixin().set_density

[Show source in abc_builder.py:155](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L155)

Set the density of the particle in kg/m^3.

#### Arguments

- `density` - Density of the particle.
- `density_units` - Units of the density. Default is *kg/m^3*

#### Signature

```python
def set_density(
    self,
    density: Union[float, NDArray[np.float_]],
    density_units: Optional[str] = "kg/m^3",
): ...
```



## BuilderDistributionStrategyMixin

[Show source in abc_builder.py:419](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L419)

Mixin class for Builder classes to set distribution_strategy.

#### Methods

- `set_distribution_strategy` - Set the distribution_strategy attribute.

#### Signature

```python
class BuilderDistributionStrategyMixin:
    def __init__(self): ...
```

### BuilderDistributionStrategyMixin().set_distribution_strategy

[Show source in abc_builder.py:429](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L429)

Set the distribution strategy of the particle.

#### Arguments

- `distribution_strategy` - Distribution strategy of the particle.
- `distribution_strategy_units` - Not used. (for interface consistency)

#### Signature

```python
def set_distribution_strategy(
    self,
    distribution_strategy: DistributionStrategy,
    distribution_strategy_units: Optional[str] = None,
): ...
```

#### See also

- [DistributionStrategy](particles/distribution_strategies.md#distributionstrategy)



## BuilderMassMixin

[Show source in abc_builder.py:300](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L300)

Mixin class for Builder classes to set mass and mass_units.

#### Methods

- `set_mass` - Set the mass attribute and units.

#### Signature

```python
class BuilderMassMixin:
    def __init__(self): ...
```

### BuilderMassMixin().set_mass

[Show source in abc_builder.py:310](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L310)

Set the mass of the particle in kg.

#### Arguments

- `mass` - Mass of the particle.
- `mass_units` - Units of the mass. Default is *kg*.

#### Raises

- `ValueError` - If mass is negative

#### Signature

```python
def set_mass(
    self, mass: Union[float, NDArray[np.float_]], mass_units: Optional[str] = "kg"
): ...
```



## BuilderMolarMassMixin

[Show source in abc_builder.py:204](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L204)

Mixin class for Builder classes to set molar_mass and molar_mass_units.

#### Methods

- `set_molar_mass` - Set the molar_mass attribute and units.

#### Signature

```python
class BuilderMolarMassMixin:
    def __init__(self): ...
```

### BuilderMolarMassMixin().set_molar_mass

[Show source in abc_builder.py:214](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L214)

Set the molar mass of the particle in kg/mol.

#### Arguments

-----
- `-` *molar_mass* - Molar mass of the particle.
- `-` *molar_mass_units* - Units of the molar mass. Default is *kg/mol*.

#### Signature

```python
def set_molar_mass(
    self,
    molar_mass: Union[float, NDArray[np.float_]],
    molar_mass_units: Optional[str] = "kg/mol",
): ...
```



## BuilderRadiusMixin

[Show source in abc_builder.py:331](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L331)

Mixin class for Builder classes to set radius and radius_units.

#### Methods

- `set_radius` - Set the radius attribute and units.

#### Signature

```python
class BuilderRadiusMixin:
    def __init__(self): ...
```

### BuilderRadiusMixin().set_radius

[Show source in abc_builder.py:341](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L341)

Set the radius of the particle in meters.

#### Arguments

- `radius` - Radius of the particle.
- `radius_units` - Units of the radius. Default is *m*.

#### Raises

- `ValueError` - If radius is negative

#### Signature

```python
def set_radius(
    self, radius: Union[float, NDArray[np.float_]], radius_units: Optional[str] = "m"
): ...
```



## BuilderSurfaceStrategyMixin

[Show source in abc_builder.py:365](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L365)

Mixin class for Builder classes to set surface_strategy.

#### Methods

- `set_surface_strategy` - Set the surface_strategy attribute.

#### Signature

```python
class BuilderSurfaceStrategyMixin:
    def __init__(self): ...
```

### BuilderSurfaceStrategyMixin().set_surface_strategy

[Show source in abc_builder.py:375](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L375)

Set the surface strategy of the particle.

#### Arguments

- `surface_strategy` - Surface strategy of the particle.
- `surface_strategy_units` - Not used. (for interface consistency)

#### Signature

```python
def set_surface_strategy(
    self, surface_strategy: SurfaceStrategy, surface_strategy_units: Optional[str] = None
): ...
```

#### See also

- [SurfaceStrategy](particles/surface_strategies.md#surfacestrategy)



## BuilderSurfaceTensionMixin

[Show source in abc_builder.py:173](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L173)

Mixin class for Builder classes to set surface_tension.

#### Methods

-------
    - `set_surface_tension` - Set the surface_tension attribute and units.

#### Signature

```python
class BuilderSurfaceTensionMixin:
    def __init__(self): ...
```

### BuilderSurfaceTensionMixin().set_surface_tension

[Show source in abc_builder.py:184](https://github.com/Gorkowski/particula/blob/main/particula/next/abc_builder.py#L184)

Set the surface tension of the particle in N/m.

#### Arguments

- `surface_tension` - Surface tension of the particle.
- `surface_tension_units` - Surface tension units. Default is *N/m*.

#### Signature

```python
def set_surface_tension(
    self,
    surface_tension: Union[float, NDArray[np.float_]],
    surface_tension_units: Optional[str] = "N/m",
): ...
```
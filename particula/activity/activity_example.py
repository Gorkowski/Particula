

org_mole_fraction = np.linspace(0, 1, 100)
molarmass_ratio = 18.016/250
O2C = 0.2
H2C = 0
N2C = 0


O2C, molarmass_ratio = convert_to_OH_eqivelent(
        O2C,
        molarmass_ratio,
        BAT_functional_group=None
    )

# check the limits of possible mole fractions
org_mole_fraction = np.where(org_mole_fraction>1, 1, org_mole_fraction)
org_mole_fraction = np.where(org_mole_fraction<=0, 10**-20, org_mole_fraction)

density = organic_density_estimate(18.016/molarmass_ratio, O2C, H2C, N2C)


#%%

O2C_array = np.linspace(0, 0.6, 100)
weights_matrix = np.zeros((100, 3))

for index, O2C in enumerate(O2C_array):
    weights_matrix[index, :] = bat_blending_weights(molarmass_ratio, O2C)

fig, ax = plt.subplots()
ax.plot(
    O2C_array,
    weights_matrix,
    )

ax.set_xlabel("O:C")
ax.set_ylabel("weights")
# ax.legend()
fig.show


gibbs_mix, dervative_gibbs = gibbs_of_mixing(
    molarmass_ratio,
    org_mole_fraction,
    O2C,
    density,
    FIT_lowO2C
)

organic_molecular_weight = np.linspace(50, 500, 500)

o2c_value = organic_water_single_phase(18.01528 / organic_molecular_weight)

fig, ax = plt.subplots()
ax.plot(
    organic_molecular_weight,
    o2c_value,
    label="initial",
    linestyle='dashed'
    )
ax.set_xlabel("Organic molecular weight (g/mol)")
ax.set_ylabel("O:C ratio")
ax.set_title("Organic Phase separation")
ax.legend()
#     org_mole_fraction, O2C, H2C, molarmass_ratio, BAT_functional_group, special_options, N2C_values_denistyOnly)


# %%
O2C=0.225
molarmass_ratio = 18.016/100
density = organic_density_estimate(18.016/molarmass_ratio, O2C)




#     gibbs_real,
#     label="gibbs",
#     linestyle='dashed'
#     )
ax.plot(
    1-org_mole_fraction,
    activity_water,
    label="water",
    linestyle='dashed'
    )

ax.plot(
    1-org_mole_fraction,
    activity_organic,
    label="organic",
    )
ax.set_ylim((0,1))
ax.set_xlabel("water mole fraction")
ax.set_ylabel("activity")
ax.legend()
fig.show



phase_sep_aw = find_phase_separation(activity_water, activity_organic)
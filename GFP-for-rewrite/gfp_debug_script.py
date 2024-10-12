# %%
import os

from pyglotaran_extras import plot_data_overview

os.chdir("GFP-for-rewrite")

experiment_data = {
    "GFPppH2O": "data/gfph2oa.ascii",
}

plot_data_overview(
    experiment_data["GFPppH2O"],
    linlog=True,
    linthresh=1,
    cmap="seismic",
)


# from glotaran.project.scheme import Scheme
# %%
from glotaran.io import load_parameters, load_scheme

# %%
parameters = load_parameters("models/parameters_sequential2.yml", format_name="yml")


# %%
parameters


# %%
scheme = load_scheme("models/model_sequential_rewrite2.yml", format_name="yml")


# %%
from glotaran.io import load_dataset

scheme.load_data(
    {
        "GFPppH2O": load_dataset("data/gfph2oa.ascii"),
        "GFPpdpH2O": load_dataset("data/gfph2ob.ascii"),
    }
)


# %%
result = scheme.optimize(parameters, maximum_number_function_evaluations=1)


# %%
result.data["renamed"] = result.data["GFPppH2O"].rename(
    {"species_associated_estimation": "species_associated_spectra"}
)


# %%
result


# %%
result.data["renamed"]


# %%
result.parameters_optimized


# %%
# result.data["GFPppH2O"].lifetime_decay
# AttributeError: 'Dataset' object has no attribute 'lifetime_decay'


# %%
result.data["GFPppH2O"].data.plot(x="time", y="spectral", size=2)


# %%
# fig, axes = result.data["GFPppH2O"].data.plot(x="time",y="spectral",size=2)
result.data["GFPppH2O"].data.plot(x="time", y="spectral", size=2)
# axes[0].annotate("A", xy=(-0.1, 1), xycoords="axes fraction",fontsize=16)


import matplotlib.pyplot as plt

# %%
from pyglotaran_extras.plotting.plot_concentrations import plot_concentrations
from pyglotaran_extras.plotting.plot_spectra import plot_sas


def plot_concentration_and_spectra(result_dataset):
    # fig, axes = plt.subplots(1, 2, figsize=(18, 7))
    fig, axes = plt.subplots(1, 2, figsize=(15, 4))
    plot_concentrations(result_dataset, axes[0], center_λ=0, linlog=True)
    plot_sas(result_dataset, axes[1])
    return fig, axes


# %%
fig, axes = plot_concentration_and_spectra(result.data["renamed"])
axes[0].set_xlabel("Time (ps)")
axes[0].set_ylabel("")
axes[0].axhline(0, color="k", linewidth=1)
axes[0].annotate("A", xy=(-0.1, 1), xycoords="axes fraction", fontsize=16)
axes[1].set_xlabel("Wavelength (nm)")
axes[1].set_ylabel("SADS (mOD)")
axes[1].set_title("SADS")
axes[1].axhline(0, color="k", linewidth=1)
axes[1].annotate("B", xy=(-0.1, 1), xycoords="axes fraction", fontsize=16)


# %%
fig, axes = plot_concentration_and_spectra(result.data["GFPppH2O"])
axes[0].set_xlabel("Time (ps)")
axes[0].set_ylabel("")
axes[0].axhline(0, color="k", linewidth=1)
axes[1].set_xlabel("Wavelength (nm)")
axes[1].set_ylabel("SADS (mOD)")
axes[1].set_title("SADS")
axes[1].axhline(0, color="k", linewidth=1)


# %%
from pyglotaran_extras.plotting.plot_traces import (
    plot_fitted_traces,
    select_plot_wavelengths,
)
from pyglotaran_extras.plotting.style import PlotStyle

wavelengths = select_plot_wavelengths(
    result.data["GFPppH2O"], equidistant_wavelengths=False, axes_shape=(4, 3)
)
fig3tr, axes = plot_fitted_traces(
    result,
    wavelengths,
    axes_shape=(4, 3),
    linlog=True,
    linthresh=1,
    cycler=PlotStyle().data_cycler_solid_dashed,
)

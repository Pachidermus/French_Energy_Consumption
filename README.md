# Student challenge

Authors: Oscar Bouvier - Hugues Gallier - Guillaume Hofmann - Romain Ilbert - Christos Katsoulakis

As part of the Data Camp course, within the [Data Science Masters at Institut Polytechnique de Paris](https://www.ip-paris.fr/en/education/masters/applied-mathematics-and-statistics-program/master-year-2-data-science), students were required to build a data challenge addressing some social/science/business problem using data obtained from external sources. This is one example of a student challenge, showcased on the [ramp.studio](https://ramp.studio/) server .

# Forecasting of France's electrical energy consumption

Optimally distributing electrical energy to almost 30 million households is a constant challenge for French power grid engineers. The most obvious constraint comes from the limits of the laws of physics, which make it very difficult to store the energy produced by French power plants. Thus, the power grid must constantly maintain a balance between consumption and production. An excess of production must be obligatorily evacuated and is the cause of financial losses, while a lack of production can lead to power outages.

New difficulties are added with the development of intermittent energies (wind turbines, solar panels) whose production or lack of production must be compensated by the contribution of controllable energy sources (nuclear power plants, hydraulic dams).

This is why a reliable forecast of French electricity consumption is a crucial asset to be able to anticipate needs in order to avoid blackouts and  be able to intelligently distribute production over the various available energy sources.

The challenge is to predict with a minimum of error France's electricity consumption in 2020 using the electricity consumption of the last two years and a few other potentially relevant variables.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```
### Challenge description

The starting kit notebook provides more details on this challenge and exploratory analysis on the data used.

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)

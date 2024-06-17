# Steps to Run pypsa-eur in Tutorial Mode and Manage Results

1. Run PyPSA-Eur in tutorial mode by following the instructions [here](https://pypsa-eur.readthedocs.io/en/latest/tutorial.html).
2. Clone the PyPSA repository:
    ```sh
    git clone https://github.com/PyPSA/PyPSA.git
    ```
3. In the same conda environment (i.e., `pypsa-eur`), navigate to the PyPSA directory and use:
    ```sh
    pip install -e .
    ```
    This will build your modified code to be used in the environment.
4. Follow the [PyPSA code snippet](https://github.com/PyPSA/PyPSA/pull/927) and modify PyPSA to dump the model in the desired directory.
5. Delete only the results folder from PyPSA-Eur directory after a successful tutorial run.
6. Use the same command as the pypsa-eur tutorial to dump the file using our modified PyPSA code:
    ```sh
    snakemake -call results/test-elec/networks/elec_s_6_ec_lcopt_.nc --configfile config/test/config.electricity.yaml
    ```
7. Use Docker to build the Linopy Docker image. Docker commands are in the Dockerfile, play with the image.
8. Copy the dumped model `.nc` file to the input directory of this repo and rename it as `test.nc`.
9. Use Docker volume mount command to run the image and get results.
10. Just like step 4 use [PyPSA code snippet](https://github.com/PyPSA/PyPSA/pull/927) to modify PyPSA to read the resulting model from step 9.
11. Redo step 5 and 6.
12. Check objective values in both cases.
    

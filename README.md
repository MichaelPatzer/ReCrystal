## ReCrystal is published

IUCrJ (2025). 12, 322–333
https://journals.iucr.org/m/issues/2025/03/00/fc5082/index.html

Further details can be found in my dissertation and please cite if used: https://doi.org/10.25926/BUW/0-168

# 🧪 ReCrystal — Quantum Crystallographic Refinement with XD2024
by Michael Patzer

## 🔍 About ReCrystal?
ReCrystal is a python3-based tool for quantum crystallographic refinement based on periodic DFT wave functions. The program combines CRYSTAL17/23 calculations with multipole refinement via XD2024 and enables a realistic description of the electron density in molecular solids.

## ✨New features in the current version (2025)

✅ **Compatibility with XD2024**
ReCrystal is now compatible with xdlsm XD2024.

- Benefit from the new optimizations, features and bug fixes of the current XD version.

✅ **GUI in progress** 
![GUI Goddard 2](https://raw.githubusercontent.com/MichaelPatzer/ReCrystal/main/GUI_goddard2.PNG)

✅ **Extended structural dimension**
The restriction to max. 30 atoms in the asymmetric unit has been lifted.

- Now also suitable for larger molecules and supramolecular systems.

✅ **Optimized refinement cycle**
- Improved iteration process:

- Wave function update with CRYSTAL

- Theoretical form factor calculation

- Multipole refinement with XD2024

- Automated convergence check 

## 🧠 Possible applications
- Investigation of weak interactions (e.g. H-bridges, π-π)

- Quantitative electron density analyses

- Crystal structure analysis of functional molecules and clusters

- Hybrid refinement with experimental and theoretical data

- Improved determination of the positions of the hydrogen atoms compared to the IAM

**the minor issue**
the minor technical problem is that the CRYSTAL calculation is started differently on the respective cluster environment. For this reason, it will be necessary to adapt the code individually so that a routine application is possible.
Write me an e-mail and we can address your project: patzer@mpi-muelheim.mpg.de 

# SOP - Standard Operating Procedure

## A tool for quantum crystallographic refinement
ReCrystal allows you to iteratively refine a crystallographic data set from a single crystal X-ray diffraction pattern with multipolar parameters that have been derived from a CRYSTAL17 calculation under periodic boundary conditions. The programme coordinates the whole process while the underlying computation and refinement is done with already established programmes (CRYSTAL17 and XD2006). ReCrystal automatically generates input data, controls the convergence and writes out the key results.  

## Refinement with CRYSTAL17: ReCrystal
- Software development under **LINUX**
- software language 100 % python3
- it is possible to run CRYSTAL17 on a cluster to speed up refinement as well as on the same computer

## How to run
Enter in the command line:

**python3 ReCrystal.py**

Due to the computational cost of the Crystal calculation, it is possible to use an input.txt file that contains all the necessary information for ReCrystal (see Examples):

**python3 ReCrystal.py < input.txt >& Out.txt &**

Some additional programs are required for ReCrystal.py
1. python3 (https://www.python.org/downloads/)
2. CRYSTAL17 Program Pcrystal and Pproperties (https://www.crystal.unito.it/)
3. ShelxL (https://shelx.uni-goettingen.de/index.php)
4. XD2024 (https://www.chem.gla.ac.uk/~louis/xd-home/download.html)
5. If you run CRYSTAL17 on a HPC, you may need subcry17 and subprop17 (see folder *sub_script*)

## Path where you should store the executable files

()

### The refining process

1. Structure refinement with shelxL:
Before you use ReCrystal, refine your Crystal structure with shelxL and use the **Acta** command to create a CIF.
Vibrations of Hydrogens should be treated isotropic. Each atom should be named in a four-digit code (Example oxygen): O001, O002, O003, etc.

2. Start your refinement with ReCrystal:
For the ReCrystal refinment you only need the CIF from the shelxL refinement. It should contain the HKLF4 and coordinates.
An exmaple how the CIF should look like is given in the Examples-Folder!

Please ensure that all Programms are installed on the Computer (shelxL, Pcrystal, Pproperties, XD2006)

3. Start **ReCrystal.py** as described with python3 ("python3 ReCrystal.py")
The Program will ask you for INPUT data!
- Name of the CIF
- Basis-Set for CRYSTAL calculation
- DFT functional or CRYSTAL calculation
- SHRINK factor
- Maximum number of refinement cycles
- Number of CPU 

4. ReCrystal will perform the Refinement on its own. You do not have to do anything! The hydrogen atoms are now treated anisotropically.

5. After refinement you can analyse all Files! Check if the refinement was succesfull! You can use any tool that can be used to analyse XD charge density refinement results.

Have FUN and GOOD LUCK for your refinement and charge density analysis!





The code will be uploaded soon! If you have any questions, please don't hesitate to ask me!

# ReCrystal: a tool for quantum crystallographic refinement
ReCrystal allows you to iteratively refine a crystallographic data set from a single crystal X-ray diffraction pattern with multipolar parameters that have been derived from a CRYSTAL17 calculation under periodic boundary conditions. The programme coordinates the whole process while the underlying computation and refinement is done with already established programmes (CRYSTAL17 and XD2006). ReCrystal automatically generates input data, controls the convergence and writes out the key results.  

## *Re*finement with *CRYSTAL*17: ReCrystal
- Software development under **LINUX**
- software language 100 % python3
- it is possible to run CRYSTAL17 on a cluster to speed up refinement as well as on the same computer

## SOP - Standard Operating Procedure
Enter in the command line:

"python3 ReCrystal.py"

*You will need some additional Programs for ReCrystal.py*
1. python3 (https://www.python.org/downloads/)
2. CRYSTAL17 Program Pcrystal and Pproperties (https://www.crystal.unito.it/)
3. ShelxL (https://shelx.uni-goettingen.de/index.php)
4. XD2006 (https://www.chem.gla.ac.uk/~louis/xd-home/download.html)
5. If you run CRYSTAL17 on a HPC, you may need subcry17 and subprop17 (if required feel free to send me an e-mail)

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

4. ReCrystal will perform the Refinement on its own. You do not have to do anything! 

5. After refinement you can analyse all Files! Check if the refinement was succesfull! You can use any tool that can be used to analyse XD charge density refinement results.

Have FUN and GOOD LUCK for your refinement and charge density analysis!



# *Re*finement with *CRYSTAL*17: ReCrystal

## What can you do with ReCrystal?
ReCrystal allows you to iteratively refine a crystallographic data set from single crystal x-ray diffraction with multipolar parameters derived from a CRYSTAL17 calculation. 

## How to run ReCrystal.py?
### Basically
Enter in the command line:

"python3 ReCrystal.py"

*You will need some additional Programs for ReCrystal.py*
1. python3 (https://www.python.org/downloads/)
2. CRYSTAL17 Program Pcrystal and Pproperties (https://www.crystal.unito.it/)
3. ShelxL (https://shelx.uni-goettingen.de/index.php)
4. XD2006 (https://www.chem.gla.ac.uk/~louis/xd-home/download.html)
5. If you run CRYSTAL17 on a HPC, you may need subcry17 and subprop17 (Send me an e-mail if you need)

### Example

1. Structure refinement with shelxL
Before you use ReCrystal, refine your Crystal structure with shelxL and use the **Acta** command to create a CIF.
Vibrations of Hydrogens should be treated isotropic. 

2. Start your refinement with ReCrystal
For the ReCrystal refinment you only need the CIF from the shelxL refinement. It should contain the HKLF4 and coordinates.


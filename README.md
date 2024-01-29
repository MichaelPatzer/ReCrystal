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

4. ReCrystal will perform the Refinement on its own. You do not have to do anything! The hydrogen atoms are now treated anisotropically.

5. After refinement you can analyse all Files! Check if the refinement was succesfull! You can use any tool that can be used to analyse XD charge density refinement results.

Have FUN and GOOD LUCK for your refinement and charge density analysis!

# Example Calcium-Tartrat-Tetrahydrate

The refinement of a complete theoretical data set is demonstrated here (no systematic errors). The synthetic dataset was generated using CRYSTAL17.

OPT_FREQ
CRYSTAL
0 0 0
 19 
9.15000000000  9.55000000000  10.49000000000
 27
 20     0.68668     0.68264     0.32358
 8     0.5555     0.4687     0.3298
 8     0.9866     0.2685     -9.70000000000031E-03
 8     0.837200000000001     0.4742     0.2879
 1     0.916     0.455     0.327
 8     0.5359     0.2412     0.2862
 8     0.7261     0.663     8.98999999999997E-02
 1     0.741     0.5744     6.64999999999997E-02
 1     0.6457     0.686     4.68999999999999E-02
 8     1.0496     0.2377     0.1943
 8     0.7271     0.3607     4.64999999999996E-02
 1     0.638     0.323     3.09999999999997E-02
 6     0.7721     0.3395     0.2756
 1     0.8146     0.2767     0.3395
 6     0.6072     0.3511     0.2988
 6     0.7981     0.2786     0.1439
 1     0.7542     0.185     0.1424
 8     0.689800000000001     0.9378     0.3343
 1     0.777200000000001     0.9659     0.347
 1     0.643000000000001     0.9649     0.4004
 6     0.9593     0.2627     0.1075
 8     1.0722     0.5837     7.66999999999997E-02
 1     1.037     0.564     3.99999999999953E-03
 1     0.998     0.606     0.122
 8     1.0726     0.4256     0.4365
 1     1.09     0.459     0.5101
 1     1.12     0.349     0.435
FREQCALC
PREOPTGEOM
FULLOPTG
MAXCYCLE
300
END
INTENS
ADP
0 0
TEMPERAT
2 0 100
END
BASISSET
POB-TZVP
DFT
PBE
END
SHRINK
8 8
TOLDEE
9
MAXCYCLE
200
END

After calculating the dynamic structure factor with CRYSTAL17, an HKLF4 was created with the output of Pproperties. 
The result of the ReCrystal refinement is the following structure model:

<img width="724" alt="ReCrystal_result" src="https://github.com/MichaelPatzer/ReCrystal/assets/135106090/0d600afb-2159-4e21-9bad-0c6b63c8be77">

Fig. 1: ORTEP of a fragment of calcium tartrate tetrahydrate - Ellipsoids on 50 % propability level; after refinement with ReCrystal V3.3.

## Step by step refinement

To obtain this refinement result, the structure must first be solved (e.g. shelxT). After the IAM refinement, ReCrystal could be used to refine the structure model shown in Figure 1. 
In the residual density one finds systematic undescribed electron density between atomic centres. In addition, Henn and Meindl's fractal analysis shows an asymmetric shape. 

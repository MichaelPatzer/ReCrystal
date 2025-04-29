from math import *
import subprocess
import datetime

time = datetime.datetime.now()
time_start = datetime.datetime.now()

#################################### INTRO ###########################################

print('')
print('')
print('')
print('               ##### #####   ##### ##### ##   ## ##### #######')
print('               #   # #       #     #   #  ## ##  #       ##   ')
print('               #   # #       #     #   #   ##    #       ##')
print('               ##### #####   #     #####   #     #####   ##')
print('               ###   #       #     ##      #         #   ##')
print('               # ##  #       #     # #     #         #   ##')
print('               #  ## #####   ##### #  ##  ###   ######   ##')
print('')
print('                            Version 3.3 - final ')
print('')
print('           ---  Refinement routine in X-ray crystallography  ---')
print('')
print('                         Written by Michael Patzer')
print('')
print('')
print('                  Other programs are used in this routine: ')
print('                        XD2016, shelxL for refinement ')
print('                               & Crystal17') 
print('             for calculation of theoretical multipole parameters')
print('')
print('')
print('') 
################################### INTRO END ##########################################

################################ START CRYSTAL 17 ######################################

Name = input('Name of CIF File:  ')
print('')
print('###########################################################')
print('')
print('OPTIONS FOR REFINEMENT')
print('')
Basis = input('Basis Set [STO-3G/STO-6G/POB-DZVP/POB-DZVPP/POB-TZVP]: ')
print('')
Theory = input('DFT functional  [B3LYP-D3, CAM-B3LYP, BLYP]          : ')
print('')
grid = input('Pack-Monkhorst & Gilat shrinking factors [e.g.: 8 8] : ')
print('')
Nproc = input('Number of processors                                 : ')
print('')
queue = input('Select queue [e.g. xe30th, ep29th, ep30th]           : ')
print('')
Cycles = input('Maximum Number of refining cycles                    : ')
print('')

############################# END PARAMETERS FOR REFINEMENT ############################

#################################### ATOM LIST OF PSE ##################################

atom_list = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar', \
'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr']

################################## END ATOM LIST OF PSE ################################

#################################### REFINEMENT CONTROLE ###############################

diff = open("ReCryst_convergence.log", "a")

#################################### CONVERGENCE LOG #######################################

diff.write('Refinement started at:  ' + str(time_start))
diff.write('\n')
diff.write('\n')
diff.write('Cycle        RMS-shift:  xyz(Angstroem)')
diff.write('\n--------------------------------------------------')
diff.write('\n')

file = open(Name)
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

for k in range(1,len(tmp)):
     if '_atom_site_disorder_group' in tmp[k]:
          for u in range(1,1000):
               z = tmp[k + u].split()
               if 'loop_' in tmp[k + u + 2]:
                   break
b = 0
atom = int(u)

shift_1_xyz = open("shift_1_xyz.dat", "a")

for k in range(1,len(tmp)):
     if '_atom_site_disorder_group' in tmp[k]:
         for b in range(1,int(atom)+1):
             z = tmp[k + b].split()
             x_frac = z[2].split('(')
             if len(x_frac) == 1:
                 x_frac.append('1')
             y_frac = z[3].split('(')
             if len(y_frac) == 1:
                 y_frac.append('1')
             z_frac = z[4].split('(')
             if len(z_frac) == 1:
                 z_frac.append('1')
             shift_1_xyz.write(str(z[1]) +  '   ')
             shift_1_xyz.write("%.6f" % float(x_frac[0])  + '   ')
             length = int(len(x_frac[0])) - 2
             shift_1_xyz.write("0.")
             new = x_frac[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_xyz.write('0')
             shift_1_xyz.write(str(new[0]) + '   ')
             shift_1_xyz.write("%.6f" % float(y_frac[0])  + '   ')
             length = int(len(y_frac[0])) - 2
             shift_1_xyz.write("0.")
             new = y_frac[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_xyz.write('0')
             shift_1_xyz.write(str(new[0]) + '   ')
             shift_1_xyz.write("%.6f" % float(z_frac[0])  + '   ')
             length = int(len(z_frac[0])) - 2
             shift_1_xyz.write("0.")
             new = z_frac[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_xyz.write('0')
             shift_1_xyz.write(str(new[0]) + '   ')
             shift_1_xyz.write('\n')

shift_1_xyz.close()

########################### ADP CONVERGENCE CONTROLE  ###################################

shift_1_adp = open("shift_1_adp.dat", "a")

for k in range(1,len(tmp)):
     if '_atom_site_aniso_U_12' in tmp[k]:
         for b in range(1,int(atom)+1):
             z = tmp[k + b].split()
             u11 = z[1].split('(')
             if len(u11) == 1:
                 u11.append('1')
             u22 = z[2].split('(')
             if len(u22) == 1:
                 u22.append('1')
             u33 = z[3].split('(')
             if len(u33) == 1:
                 u33.append('1')
             u23 = z[4].split('(')
             if len(u23) == 1:
                 u23.append('1')
             u13 = z[5].split('(')
             if len(u13) == 1:
                 u13.append('1')
             u12 = z[6].split('(')
             if len(u12) == 1:
                 u12.append('1')
             shift_1_adp.write(str(z[0]) +  '   ')
             shift_1_adp.write("%.6f" % float(u11[0])  + '   ')
             length = int(len(u11[0])) - 2
             shift_1_adp.write("0.")
             new = u11[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_adp.write('0')
             shift_1_adp.write(str(new[0]) + '   ')
             shift_1_adp.write("%.6f" % float(u22[0])  + '   ')
             length = int(len(u22[0])) - 2
             shift_1_adp.write("0.")
             new = u22[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_adp.write('0')
             shift_1_adp.write(str(new[0]) + '   ')
             shift_1_adp.write("%.6f" % float(u33[0])  + '   ')
             length = int(len(u33[0])) - 2
             shift_1_adp.write("0.")
             new = u33[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_adp.write('0')
             shift_1_adp.write(str(new[0]) + '   ')
             shift_1_adp.write("%.6f" % float(u12[0])  + '   ')
             length = int(len(u12[0])) - 2
             shift_1_adp.write("0.")
             new = u12[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_adp.write('0')
             shift_1_adp.write(str(new[0]) + '   ')
             shift_1_adp.write("%.6f" % float(u13[0])  + '   ')
             length = int(len(u13[0])) - 2
             shift_1_adp.write("0.")
             new = u13[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_adp.write('0')
             shift_1_adp.write(str(new[0]) + '   ')
             shift_1_adp.write("%.6f" % float(u23[0])  + '   ')
             length = int(len(u23[0])) - 2
             shift_1_adp.write("0.")
             new = u23[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_1_adp.write('0')
             shift_1_adp.write(str(new[0]) + '   ')
             shift_1_adp.write('\n')
             if '_geom_special_details' in tmp[k + b + 2]:
                 break

shift_1_adp.close()


################################ PREPARE INPUT FOR CRYSTAL #############################

file = open(Name)
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

f = open("crystal.d12", "a")

for i in range(1,len(tmp)):
    if '_space_group_name_H-M_alt' in tmp[i]:
         space = i
    if '_cell_length_a' in tmp[i]:
         check = i
    if '_diffrn_reflns_number' in tmp[i]:
         number = i
    if '_diffrn_radiation_wavelength' in tmp[i]:
         wave = i

x = tmp[space].split("'")

f.write('RECRYST')
f.write('\nCRYSTAL')
f.write('\n1 0 0')
f.write('\n' +  str(x[1]) )
f.write('\n')

test_1 = 0.0

for k in range(1,len(tmp)):
     if '_cell_length_a' in tmp[k]:
                 for u in range(0,6):
                     check = k + u
                     z = tmp[check].split()
                     h = z[1].split("(")
                     if float(h[0]) == 90.0 or float(h[0]) == 120.0 or float(h[0]) == test_1:
                         continue
                     f.write(str(h[0]) + ' ' )
                     test_1 = float(h[0])
f.write('\n')

for k in range(1,len(tmp)):
     if '_atom_site_disorder_group' in tmp[k]:
          for u in range(1,1000):
               z = tmp[k + u].split()
               if 'loop_' in tmp[k + u + 2]:
                   break
b = 0
atom = int(u)

f.write(str(atom))
f.write('\n')

for k in range(1,len(tmp)):
     if '_atom_site_disorder_group' in tmp[k]:
         for b in range(1,int(atom)+1):
             z = tmp[k + b].split()
             for y in range(0,35):
                 if str(z[1]) in atom_list[y]:
                     p = y + 1
                     f.write(str(p) + '  ')
                     break
             x_frac = z[2].split('(')
             y_frac = z[3].split('(')
             z_frac = z[4].split('(')
             f.write("%.6f" % float(x_frac[0])  + '   ')
             f.write("%.6f" % float(y_frac[0])  + '   ')
             f.write("%.6f" % float(z_frac[0])  + '   ')
             f.write('\n')

f.write('BASISSET')
f.write('\n' + str(Basis))
f.write('\nDFT')
f.write('\n' +str(Theory))
f.write('\nEND')
f.write('\nSHRINK')
f.write('\n' + str(grid))
f.write('\nEND')

f.close()

#################################### PREPARE INPUT END ##########################################

# Start Crystal-Rechnung ------------------------------------------------------------------------

gain = ['./subcry17 -n ',Nproc,' -q ', queue,' crystal']
trennzeichen = ''
pcrystal_command = trennzeichen.join(gain)
subprocess.call(str(pcrystal_command), shell = True)
subprocess.call("rm crystal.d12", shell = True)

# END Crystal-Rechnung --------------------------------------------------------------------------

################################### PREPARE XFAC INPUT  ##########################################

f = open("crystal.d3", "a")

# Schreiben eines Inputfiles zur Berechnung der statischen Strukturfaktoren mit PROPERTIES

f.write('XFAC')

print('')
print('')
print('#    #  #####     #       ######')
print(' #  #   #        # #      #')
print('   #    #####   #   #     #')
print('  #     #      #######    #')
print(' #  #   #     #       #   #')
print('#    #  #    #         #  ######')

print('')
print('###################################################################')
print('')
print('HKL-Calculation to d = 0.40 Angstroem via CIF cell parameters')
print('')
print('###################################################################')
print('')
time = datetime.datetime.now()
print('PREPARE XFAC INPUT       Start-time: ' + str(time))

################################## PREPARE XFAC INPUT ###########################################

###################################### a,b,c Axis ###############################################

for i in range(1,len(tmp)):
   if '_cell_length_a' in tmp[i]:
         o = tmp[i].split()
         p = o[1].split('(')
         a_axis = p[0]
         o = tmp[i+1].split()
         p = o[1].split('(')
         b_axis = p[0]
         o = tmp[i+2].split()
         p = o[1].split('(')
         c_axis = p[0]

###################################### alpha,beta,gamma###########################################

for i in range(1,len(tmp)):
   if '_cell_angle_alpha' in tmp[i]:
         o = tmp[i].split()
         p = o[1].split('(')
         alpha = p[0]
         o = tmp[i+1].split()
         p = o[1].split('(')
         beta = p[0]
         o = tmp[i+2].split()
         p = o[1].split('(')
         gamma = p[0]

a_axis = float(a_axis)
b_axis = float(b_axis)
c_axis = float(c_axis)

######################################### cell Volume ############################################

for i in range(1,len(tmp)):
   if '_cell_volume' in tmp[i]:
         o = tmp[i].split()
         p = o[1].split('(')
         V = p[0]

##################################################################################################

a_axis_sq = float(a_axis)**2
b_axis_sq = float(b_axis)**2
c_axis_sq = float(c_axis)**2

V = float(V)**2

alpha_rad = float(alpha)*(pi/180.0)
beta_rad = float(beta)*(pi/180.0)
gamma_rad = float(gamma)*(pi/180.0)

A = sin(alpha_rad)*sin(alpha_rad)
B = sin(beta_rad)*sin(beta_rad)
C = sin(gamma_rad)*sin(gamma_rad)
D = cos(alpha_rad)*cos(alpha_rad)
E = cos(beta_rad)*cos(beta_rad)
F = cos(gamma_rad)*cos(gamma_rad)

####################################################################################################

j = 50
i = 50
m = 50

a = 0

j = int(j)*2 + 1
i = int(i)*2 + 1
m = int(m)*2 + 1

for x in range(0,int(m)):
   for y in range(0,int(i)):
      for z in range(0,int(j)):
           h = z-(int(j)-1)/2
           k = y-(int(i)-1)/2
           l = x-(int(m)-1)/2
           h = int(h)
           k = int(k)
           l = int(l)
           calc = (1/V) * ((h**2)*b_axis_sq*c_axis_sq*A + (k**2)*a_axis_sq*c_axis_sq*B + (l**2)*a_axis_sq*b_axis_sq*C + \
           2*h*k*a_axis*b_axis*c_axis_sq*(cos(alpha_rad)*cos(beta_rad)-cos(gamma_rad)) + \
           2*k*l*a_axis_sq*b_axis*c_axis*(cos(beta_rad)*cos(gamma_rad)-cos(alpha_rad)) + \
           2*h*l*a_axis*b_axis_sq*c_axis*(cos(alpha_rad)*cos(gamma_rad)-cos(beta_rad)))
           if float(calc) > 6.25:
              continue
           if h==0 and k==0 and l==0:
              continue
           else:
              a = a + 1

f.write('\n'+ str(a) + ' ' + '1')

for x in range(0,int(m)):
   for y in range(0,int(i)):
      for z in range(0,int(j)):
           h = z-(int(j)-1)/2
           k = y-(int(i)-1)/2
           l = x-(int(m)-1)/2
           h = int(h)
           k = int(k)
           l = int(l)
           calc = (1/V) * ((h**2)*b_axis_sq*c_axis_sq*A + (k**2)*a_axis_sq*c_axis_sq*B + (l**2)*a_axis_sq*b_axis_sq*C + \
           2*h*k*a_axis*b_axis*c_axis_sq*(cos(alpha_rad)*cos(beta_rad)-cos(gamma_rad)) + \
           2*k*l*a_axis_sq*b_axis*c_axis*(cos(beta_rad)*cos(gamma_rad)-cos(alpha_rad)) + \
           2*h*l*a_axis*b_axis_sq*c_axis*(cos(alpha_rad)*cos(gamma_rad)-cos(beta_rad)))
           if float(calc) > 6.25:
              continue
           if h==0 and k==0 and l==0:
              continue
           else:
              f.write('\n')
              f.write("%4i %3i %3i" % (int(h), int(k), int(l)))

f.write('\n' + 'END')
f.write('\n' + 'END')

f.close()
####################################### PREPARE INPUT END #########################################

print('')
time = datetime.datetime.now()
print('PREPARE XFAC INPUT       Finish-time: ' + str(time))
print('')
print('###################################################################')

# Start XFAC Calculation---------------------------------------------------------------------------

print('')
print('Calculating Scattering factors...')
print('')

gain2 = ['./subprop17 -n ',Nproc,' -q ',queue,' crystal']
trennzeichen2 = ''
pproperties_command = trennzeichen2.join(gain2)

subprocess.call(str(pproperties_command), shell = True)
subprocess.call("cp crystal.d3 crystal.d3_save", shell = True)

#  End XFAC Calculation ---------------------------------------------------------------------------

####################################### MAKE HKLF4 ################################################

v = open("check.hkl", "a")

file = open('crystal.out')
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

for k in range(0,len(tmp)):
    if 'X-RAY STATIC STRUCTURE FACTORS' in tmp[k]:
        for n in range(k + 10,len(tmp)):
            w = tmp[n]
            h = w[-66:-63]
            k = w[-63:-60]
            l = w[-60:-57]
            I = w[-10:]
            I = float(I)**2
            s = float(I) * 0.01
#           print(h, k, l, I, s)
            v.write("%4i %3i %3i %7.3f %7.3f" % (int(h), int(k), int(l), float(I), float(s)))
            v.write("\n")
            if int(h)==0 and int(k)==0 and int(l)==0:
                continue
            if 'XFAC' in tmp[n+1]:
                break

v.close()

#subprocess.call("rm fort* diis* dffit3.dat", shell = True)

####################################### MAKE HKLF4 END ############################################

######################### Theoretical_Multipole_Parameter_Generation###############################

#1. Generate Shelx-INS from CIF: CHECK

q = open("shelx.ins", "a")

q.write('TITL CHECK')
q.write('\n')

file = open(Name)
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

for i in range(1,len(tmp)):
    if '_shelx_res_file' in tmp[i]:
        for d in range(i+5,len(tmp)):
            if 'FVAR' in tmp[d]:
                q.write(tmp[d])
                q.write('\n')
                for o in range(d+1, len(tmp)):
                    if 'HKLF 4' in tmp[o]:
                        q.write('HKLF 4')
                        break
                    if '=' in tmp[o]:
                        new = tmp[o].split()
                        for m in range(0,6):
                            q.write(new[m] + '  ')
                        q.write('10.0000')
                        q.write('\n')
                    if 'H' in tmp[o]:
                        new = tmp[o].split()
                        for m in range(0,6):
                            q.write(new[m] + '  ')
                        q.write('10.0000')
                        q.write('\n')    
                break
            q.write(tmp[d])
            q.write('\n')

q.close()

###################################### Start Multipol-Refinement###################################

subprocess.call("bash /usr/users/patzer/xd_data/xd_start.sh", shell = True)
subprocess.call("mv check.hkl shelx.hkl", shell = True)
subprocess.call("/usr/users/patzer/bin/shelxl shelx", shell = True)
subprocess.call("mv shelx.cif xd.cif", shell = True)
subprocess.call("mv shelx.fcf xd.fcf", shell = True)
subprocess.call("/usr/users/patzer/bin/xdini check cif vm", shell = True)

################################ Edit xd.mas for refinement #######################################

file = open("xd.mas")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

t = open("xd_new.mas", "a")

for i in range(0,len(tmp)):
    if 'SELECT  model' in tmp[i]:
        t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
        t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
        t.write('\n')
        continue
    if 'SELECT  cycle' in tmp[i]:
        continue
    if 'SCAT' in tmp[i]:
        t.write(str(tmp[i]))
        t.write('\n')
        for q in range(i+1,len(tmp)):
            if 'END SCAT' in tmp[q]:
                break
            new = tmp[q].split('.')
            t.write(str(new[0]))
            t.write('.0000  0.0000  0.000')
            t.write('\n')
        break
    t.write(tmp[i])
    t.write('\n')

t.write('END SCAT')
t.write('\n' + '!------------------------------------------------------------------------------')
t.write('\n' + 'ATOM     ATOM0    AX1 ATOM1    ATOM2   AX2 R/L TP TBL KAP LMX SITESYM  CHEMCON')
t.write('\n')

kappa_value = 0

for n in range(0, len(tmp)):
    if 'CHEMCON' in tmp[n]:
        for b in range(n+1, n+atom+1):
            kappa_new = tmp[b].split()
            t.write(str(kappa_new[0]) + '  ')
            t.write(str(kappa_new[1]) + '  ')
            t.write(str(kappa_new[2]) + '  ')
            t.write(str(kappa_new[3]) + '  ')
            t.write(str(kappa_new[4]) + '  ')
            t.write(str(kappa_new[5]) + '  ')
            t.write(str(kappa_new[6]) + '  ')
            t.write(str(kappa_new[7]) + '  ')
            t.write(str(kappa_new[8]) + '  ')
            kappa_value = kappa_value + 1
            t.write(str(kappa_value) + '  ')
            t.write(str(kappa_new[10]) + '  ')
            t.write(str(kappa_new[11]) + '  ')
            t.write('\n')


for p in range(0,len(tmp)):
    if 'END ATOM' in tmp[p]:
        for i in range(p,len(tmp)):
            if 'KEEP     kappa' in tmp[i]:
                t.write('KEEP     kappa' + ' ')
                for i in range(1,atom+1):
                    t.write(str(i) + ' ')
                t.write('\n')
                continue
            if '!DMSDA' in tmp[i]:
                t.write('DMSDA    1.1  1.8')
                continue
            if '!FOUR' in tmp[i]:
                t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
                t.write('\n')
                continue
            if 'KAPPA' in tmp[i]:
                break
            if 'KEY     XYZ' in tmp[i]:
                t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
                t.write('\n')
                for h in range(i+1, len(tmp)):
                    new = tmp[h].split()
                    if 'H(' in tmp[h]:
                        t.write(new[0])
                        t.write('  000 000000 0000000000 000000000000000 10 111 11111 0000000 000000000')
                        t.write('\n')
                        continue
                    if '111 111111 0000000000 000000000000000' in tmp[h]:
                        t.write(new[0])
                        t.write('  111 111111 0000000000 000000000000000 10 111 11111 1111111 111111111')
                        t.write('\n')
                        continue
                    if 'KAPPA' in tmp[h]:
                        break
                    t.write(tmp[h])
                    t.write('\n')
                break
            t.write(tmp[i])
            t.write('\n')


for p in range(1, atom + 1):
    t.write('KAPPA   000000')
    t.write('\n')

for p in range(0,len(tmp)):
    if 'EXTCN   0000000' in tmp[p]:
        for g in range(p, len(tmp)):
            t.write(str(tmp[g]))
            t.write('\n')

t.close()

############################################ EDIT XD.MAS END ##########################################

####################################### Generate Multipolparameters ###################################

subprocess.call("mv xd_new.mas xd.mas", shell = True)

print('')
print('')
print('#               #  #       #  #     ############ #  ######   #######  #')
print('##             ##  #       #  #          #       #  #     #  #     #  #')
print('# #           # #  #       #  #          #       #  #     #  #     #  #')
print('#  #         #  #  #       #  #          #       #  #     #  #     #  #')
print('#   #       #   #  #       #  #          #       #  ######   #     #  #')
print('#    #     #    #  #       #  #          #       #  #        #     #  #')
print('#     #   #     #  #       #  #          #       #  #        #     #  #')
print('#      # #      #  #       #  #          #       #  #        #     #  #')
print('#       #       #  #########  ########   #       #  #        #######  #########')
print('')
print('')

print('')
print('')
print('####### #   #  ####  #### ####   # #####')
print('   #    #   #  #     #  # #   #  # #')
print('   #    #####  ####  #  # ####   # ##### ')
print('   #    #   #  #     #  # # #    # #')
print('   #    #   #  ####  #### #  #   # #####')
print('')
print('Multipoles - spherical harmonics')
print('')

subprocess.call("rm shelx* INPUT", shell = True)
subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)
subprocess.call("mv xd.res xd.inp", shell = True)

############################################# NEXT STEP ################################################

file = open("xd.mas")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

t = open("xd_new.mas", "a")

for i in range(0,len(tmp)):
    if 'SELECT  model' in tmp[i]:
        t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
        t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
        t.write('\n')
        continue
    if 'SELECT  cycle' in tmp[i]:
        continue
    if '!DMSDA' in tmp[i]:
        t.write('DMSDA    1.1  1.8')
        continue
    if '!FOUR' in tmp[i]:
        t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
        t.write('\n')
        continue
    if 'KEY     XYZ' in tmp[i]:
        t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
        t.write('\n')
        for h in range(i+1, len(tmp)):
            new = tmp[h].split()
            if 'H(' in tmp[h]:
                t.write(new[0])
                t.write('  000 000000 0000000000 000000000000000 00 000 00000 0000000 000000000')
                t.write('\n')
                continue
            if '  111 111111 0000000000 000000000000000 10 111 11111 1111111 111111111' in tmp[h]:
                t.write(new[0])
                t.write('  111 111111 0000000000 000000000000000 00 000 00000 0000000 000000000')
                t.write('\n')
                continue
            if 'KAPPA   000000' in tmp[h]:
                if 'EXTCN' in tmp[h+1]:
                    t.write('KAPPA   111111')
                    t.write('\n')
                    continue
                t.write('KAPPA   111111')
                t.write('\n')
                continue
            t.write(tmp[h])
            t.write('\n')
        break
    t.write(tmp[i])
    t.write('\n')

t.close()

subprocess.call("mv xd_new.mas xd.mas", shell = True)

print('')
print('')
print('####### #   #  ####  #### ####   # #####')
print('   #    #   #  #     #  # #   #  # #')
print('   #    #####  ####  #  # ####   # ##### ')
print('   #    #   #  #     #  # # #    # #')
print('   #    #   #  ####  #### #  #   # #####')
print('')
print('Kappa - radial distribution')
print('')

subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)
subprocess.call("mv xd.res xd.inp", shell = True)

############################################## NEXT STEP ################################################

file = open("xd.mas")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

t = open("xd_new.mas", "a")

for i in range(0,len(tmp)):
    if 'SELECT  model' in tmp[i]:
        t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
        t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
        t.write('\n')
        continue
    if 'SELECT  cycle' in tmp[i]:
        continue
    if '!DMSDA' in tmp[i]:
        t.write('DMSDA    1.1  1.8')
        continue
    if '!FOUR' in tmp[i]:
        t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
        t.write('\n')
        continue
    if 'KEY     XYZ' in tmp[i]:
        t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
        t.write('\n')
        for h in range(i+1, len(tmp)):
            new = tmp[h].split()
            if 'H(' in tmp[h]:
                t.write(new[0])
                t.write('  000 000000 0000000000 000000000000000 00 000 00000 0000000 000000000')
                t.write('\n')
                continue
            if '  111 111111 0000000000 000000000000000 00 000 00000 0000000 000000000' in tmp[h]:
                t.write(new[0])
                t.write('  000 000000 0000000000 000000000000000 10 111 11111 1111111 111111111')
                t.write('\n')
                continue
            if 'KAPPA   111111' in tmp[h]:
                if 'EXTCN' in tmp[h+1]:
                    t.write('KAPPA   000000')
                    t.write('\n')
                    continue
                t.write('KAPPA   000000')
                t.write('\n')
                continue
            t.write(tmp[h])
            t.write('\n')
        break
    t.write(tmp[i])
    t.write('\n')

t.close()

subprocess.call("mv xd_new.mas xd.mas", shell = True)

print('')
print('')
print('####### #   #  ####  #### ####   # #####')
print('   #    #   #  #     #  # #   #  # #')
print('   #    #####  ####  #  # ####   # ##### ')
print('   #    #   #  #     #  # # #    # #')
print('   #    #   #  ####  #### #  #   # #####')
print('')
print('All Parameters')
print('')

subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)

########################################## END OF THEORY PART ###########################################

subprocess.call("mv xd.res theory.res", shell = True)
subprocess.call("rm xd*", shell = True)

#########################################################################################################
#################################### PREPARE EXPERIMENTAL XD.HKL ########################################

q = open("shelx.ins", "a")

q.write('TITL CHECK')
q.write('\n')

file = open(Name)
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

for i in range(1,len(tmp)):
    if '_shelx_res_file' in tmp[i]:
        for d in range(i+5,len(tmp)):
            if 'FVAR' in tmp[d]:
                q.write(tmp[d])
                q.write('\n')
                for o in range(d+1, len(tmp)):
                    if 'HKLF 4' in tmp[o]:
                        q.write('HKLF 4')
                        break
                    if '=' in tmp[o]:
                        new = tmp[o].split()
                        for m in range(0,6):
                            q.write(new[m] + '  ')
                        q.write('10.0000')
                        q.write('\n')
                    if 'H' in tmp[o]:
                        new = tmp[o].split()
                        for m in range(0,6):
                            q.write(new[m] + '  ')
                        q.write('10.0000')
                        q.write('\n')
                break
            q.write(tmp[d])
            q.write('\n')

q.close()

q = open("shelx.hkl", "a")

for n in range(1, len(tmp)):
    if '_shelx_hkl_file' in tmp[n]:
        for b in range(n+2, len(tmp)):
            if '_computing_structure_solution' in tmp[b+1]:
                break
            check = tmp[b].split()
            a = check[0]
            b = check[1]
            c = check[2]
            d = check[3]
            e = check[4]
            q.write("%4i %3i %3i %7.3f %7.3f" % (int(a), int(b), int(c), float(d), float(e)))
            q.write('\n')
q.close()

################################# PREPARE EXPERIMENTAL XD.HKL END #################################

subprocess.call("/usr/users/patzer/bin/shelxl shelx", shell = True)
subprocess.call("mv shelx.cif xd.cif", shell = True)
subprocess.call("mv shelx.fcf xd.fcf", shell = True)
subprocess.call("rm shelx*", shell = True)
subprocess.call("/usr/users/patzer/bin/xdini check cif vm", shell = True)
subprocess.call("mv xd.hkl experiment.hkl", shell = True)
subprocess.call("mv xd.mas final.mas", shell = True)
subprocess.call("rm xd*", shell = True)
subprocess.call("mv theory.res xd.inp", shell = True)
subprocess.call("mv final.mas xd.mas", shell = True)
subprocess.call("mv experiment.hkl xd.hkl", shell = True)

########################################## SOME CODE STUFF ######################################

############################# PREPARE XD.MAS FOR FINAL REFINEMENT################################

file = open("xd.mas")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

t = open("xd_new.mas", "a")

for i in range(0,len(tmp)):
    if 'SELECT  model' in tmp[i]:
        t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
        t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
        t.write('\n')
        continue
    if 'SELECT  cycle' in tmp[i]:
        continue
    if 'END SCAT' in tmp[i]:
        break
    t.write(tmp[i])
    t.write('\n')


t.write('END SCAT')
t.write('\n' + '!------------------------------------------------------------------------------')
t.write('\n' + 'ATOM     ATOM0    AX1 ATOM1    ATOM2   AX2 R/L TP TBL KAP LMX SITESYM  CHEMCON')
t.write('\n')

kappa_value = 0

for n in range(0, len(tmp)):
    if 'CHEMCON' in tmp[n]:
        for b in range(n+1, n+atom+1):
            kappa_new = tmp[b].split()
            t.write(str(kappa_new[0]) + '  ')
            t.write(str(kappa_new[1]) + '  ')
            t.write(str(kappa_new[2]) + '  ')
            t.write(str(kappa_new[3]) + '  ')
            t.write(str(kappa_new[4]) + '  ')
            t.write(str(kappa_new[5]) + '  ')
            t.write(str(kappa_new[6]) + '  ')
            t.write(str(kappa_new[7]) + '  ')
            t.write(str(kappa_new[8]) + '  ')
            kappa_value = kappa_value + 1
            t.write(str(kappa_value) + '  ')
            t.write(str(kappa_new[10]) + '  ')
            t.write(str(kappa_new[11]) + '  ')
            t.write('\n')


for p in range(0,len(tmp)):
    if 'END ATOM' in tmp[p]:
        for i in range(p,len(tmp)):
            if 'KEEP     kappa' in tmp[i]:
                t.write('KEEP     kappa' + ' ')
                for i in range(1,atom+1):
                    t.write(str(i) + ' ')
                t.write('\n')
                continue
            if '!DMSDA' in tmp[i]:
                t.write('DMSDA    1.1  1.8')
                continue
            if '!FOUR' in tmp[i]:
                t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
                t.write('\n')
                continue
            if 'KAPPA' in tmp[i]:
                break
            if 'KEY     XYZ' in tmp[i]:
                t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
                t.write('\n')
                for h in range(i+1, len(tmp)):
                    new = tmp[h].split()
                    if 'H(' in tmp[h]:
                        t.write(new[0])
                        t.write('  000 000000 0000000000 000000000000000 00 000 00000 0000000 000000000')
                        t.write('\n')
                        continue
                    if '111 111111 0000000000 000000000000000' in tmp[h]:
                        t.write(new[0])
                        t.write('  111 111111 0000000000 000000000000000 00 000 00000 0000000 000000000')
                        t.write('\n')
                        continue
                    if 'KAPPA' in tmp[h]:
                        break
                    t.write(tmp[h])
                    t.write('\n')
                break
            t.write(tmp[i])
            t.write('\n')


for p in range(1, atom + 1):
    t.write('KAPPA   000000')
    t.write('\n')

for p in range(0,len(tmp)):
    if 'EXTCN   0000000' in tmp[p]:
        for g in range(p, len(tmp)):
            t.write(str(tmp[g]))
            t.write('\n')

t.close()

########################### PREPARE END #################################

print('')
print('')
print('####  #### #### # #   # #####')
print('#  #  #    #    # ##  # #')
print('###   ###  ###  # # # # ###')
print('# #   #    #    # #  ## #')
print('#  #  #### #    # #   # #####')
print('')
print('')


subprocess.call("mv xd_new.mas xd.mas", shell = True)
subprocess.call("cp xd.mas save_1.mas", shell = True)
subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)
subprocess.call("mv xd.res xd.inp", shell = True)

####################################### NEXT STEP ##########################################

file = open("xd.mas")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

t = open("xd_new.mas", "a")

for i in range(0,len(tmp)):
    if 'SELECT  model' in tmp[i]:
        t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
        t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
        t.write('\n')
        continue
    if 'SELECT  cycle' in tmp[i]:
        continue
    if '!DMSDA' in tmp[i]:
        t.write('DMSDA    1.1  1.8')
        continue
    if '!FOUR' in tmp[i]:
        t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
        t.write('\n')
        continue
    if 'KEY     XYZ' in tmp[i]:
        t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
        t.write('\n')
        for h in range(i+1, len(tmp)):
            new = tmp[h].split()
            if 'H(' in tmp[h]:
                t.write(new[0])
                t.write('  111 100000 0000000000 000000000000000 00 000 00000 0000000 000000000')
                t.write('\n')
                continue
            if '111 111111 0000000000 000000000000000' in tmp[h]:
                t.write(new[0])
                t.write('  111 111111 0000000000 000000000000000 00 000 00000 0000000 000000000')
                t.write('\n')
                continue
            if 'KAPPA   000000' in tmp[h]:
                if 'EXTCN' in tmp[h+1]:
                    t.write('KAPPA   000000')
                    t.write('\n')
                    continue
                t.write('KAPPA   000000')
                t.write('\n')
                continue
            t.write(tmp[h])
            t.write('\n')
        break
    t.write(tmp[i])
    t.write('\n')

t.close()

print('')
print('')
print('####  #### #### # #   # #####')
print('#  #  #    #    # ##  # #')
print('###   ###  ###  # # # # ###')
print('# #   #    #    # #  ## #')
print('#  #  #### #    # #   # #####')
print('')
print('')


subprocess.call("mv xd_new.mas xd.mas", shell = True)
subprocess.call("cp xd.mas save_2.mas", shell = True)
subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)
subprocess.call("mv xd.res xd.inp", shell = True)

##################################### NEXT STEP ############################################

file = open("xd.mas")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

t = open("xd_new.mas", "a")

for i in range(0,len(tmp)):
    if 'SELECT  model' in tmp[i]:
        t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
        t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
        t.write('\n')
        continue
    if 'SELECT  cycle' in tmp[i]:
        continue
    if '!DMSDA' in tmp[i]:
        t.write('DMSDA    1.1  1.8')
        continue
    if '!FOUR' in tmp[i]:
        t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
        t.write('\n')
        continue
    if 'KEY     XYZ' in tmp[i]:
        t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
        t.write('\n')
        for h in range(i+1, len(tmp)):
            new = tmp[h].split()
            if 'H(' in tmp[h]:
                t.write(new[0])
                t.write('  111 111111 0000000000 000000000000000 00 000 00000 0000000 000000000')
                t.write('\n')
                continue
            if '111 111111 0000000000 000000000000000' in tmp[h]:
                t.write(new[0])
                t.write('  111 111111 0000000000 000000000000000 00 000 00000 0000000 000000000')
                t.write('\n')
                continue
            if 'KAPPA   000000' in tmp[h]:
                if 'EXTCN' in tmp[h+1]:
                    t.write('KAPPA   000000')
                    t.write('\n')
                    continue
                t.write('KAPPA   000000')
                t.write('\n')
                continue
            t.write(tmp[h])
            t.write('\n')
        break
    t.write(tmp[i])
    t.write('\n')

t.close()

print('')
print('')
print('####  #### #### # #   # #####')
print('#  #  #    #    # ##  # #')
print('###   ###  ###  # # # # ###')
print('# #   #    #    # #  ## #')
print('#  #  #### #    # #   # #####')
print('')
print('')


subprocess.call("mv xd_new.mas xd.mas", shell = True)
subprocess.call("cp xd.mas save_3.mas", shell = True)
subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)


#################################### DOKUMENTATION #########################################

atomnumber = atom

out = open("ReCryst.out", "a")
trj = open("ReCryst_trj.xyz", "a")
diff = open("ReCryst_convergence.log", "a")
save_1 = open("save_1.xyz", "a") 

#################################### CONVERGENCE LOG #######################################

out.write('\n')
out.write('\n')
out.write('\n               ##### #####   ##### ##### ##   ## ##### #######')
out.write('\n               #   # #       #     #   #  ## ##  #       ##   ')
out.write('\n               #   # #       #     #   #   ##    #       ##')
out.write('\n               ##### #####   #     #####   #     #####   ##')
out.write('\n               ###   #       #     ##      #         #   ##')
out.write('\n               # ##  #       #     # #     #         #   ##')
out.write('\n               #  ## #####   ##### #  ##  ###   ######   ##')
out.write('\n')
out.write('\n                            Version 3.3 - final ')
out.write('\n')
out.write('\n           ---  Refinement routine in X-ray crystallography  ---')
out.write('\n')
out.write('\n                         Written by Michael Patzer')
out.write('\n')
out.write('\n')
out.write('\n                  Other programs are used in this routine: ')
out.write('\n                        XD2016, shelxL for refinement ')
out.write('\n                               & Crystal17')
out.write('\n             for calculation of theoretical mutlipole parameters')
out.write('\n')
out.write('\n')
out.write('\n')
out.write('\n')
out.write('\n')
out.write('\n')
out.write('###########################  INPUT PARAMETERS ##################################')
out.write('\n')
out.write('\n' + '   ' + 'BASIS SET       : ' + str(Basis))
out.write('\n' + '   ' + 'DFT FUNCTIONAL  : ' + str(Theory))
out.write('\n' + '   ' + 'SHRINK          : ' + str(grid))
out.write('\n' + '   ' + 'Number of Procs : ' + str(Nproc))
out.write('\n' + '   ' + 'MAX Num. Cycles : ' + str(Cycles))
out.write('\n')
out.write('############################## DOKU R-Values ###################################')
out.write('\n')
out.write('\n')
out.write('Refinement starts at :' + str(time))
out.write('\n')
out.write('--------------------------------------------------------------------------------')
out.write('\n')

##################################### DOKU PART #############################################

file = open('xd_lsm.out')
doku = []

for line in file:
    doku.append(line.strip())
file.close()

for p in range(0,len(doku)):
    if 'Residuals after final cycle' in doku[p]:
        for m in range(p,len(doku)):
            if 'Variables after final cycle' in doku[m]:
                break
            out.write(doku[m])
            out.write('\n')
        break

trj.write(str(atomnumber))
trj.write('\n')
trj.write('\n')

for p in range(0,len(doku)):
    if 'Atomic parameters in Cartesian crystal system' in doku[p]:
        for m in range(p+3, len(doku)):
            if '-----' in doku[m]:
                break
            if '(' in doku[m]:
                new = doku[m].split()
                one = new[0].split('(')
                one = one[0]
                trj.write(str(one))
                trj.write('  ' + new[1] + '   ' + new[2] + '   ' + new[3])
                trj.write('\n')
                save_1.write('  ' + new[1] + '   ' + new[2] + '   ' + new[3])
                save_1.write('\n')
save_1.write('*')
save_1.close()

########################################### DOKU END #####################################

#################################### ANALYSE SHIFTS XYZ FRAC #############################

subprocess.call("/usr/users/patzer/bin/xdgeom", shell = True)

file = open("xd_geo.cif")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

shift_2_xyz = open("shift_2_xyz.dat", "a")

for k in range(1,len(tmp)):
     if '_atom_site_U_iso_or_equiv' in tmp[k]:
         for b in range(1,int(atom)+1):
             z = tmp[k + b].split()
             x_frac = z[1].split('(')
             if len(x_frac) == 1:
                 x_frac.append('1')
             y_frac = z[2].split('(')
             if len(y_frac) == 1:
                 y_frac.append('1')
             z_frac = z[3].split('(')
             if len(z_frac) == 1:
                 z_frac.append('1')
             new = z[0].split('(')
             shift_2_xyz.write(str(new[0]) +  '   ')
             shift_2_xyz.write("%.6f" % float(x_frac[0])  + '   ')
             length = int(len(x_frac[0])) - 2
             shift_2_xyz.write("0.")
             new = x_frac[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_xyz.write('0')
             shift_2_xyz.write(str(new[0]) + '   ')
             shift_2_xyz.write("%.6f" % float(y_frac[0])  + '   ')
             length = int(len(y_frac[0])) - 2
             shift_2_xyz.write("0.")
             new = y_frac[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_xyz.write('0')
             shift_2_xyz.write(str(new[0]) + '   ')
             shift_2_xyz.write("%.6f" % float(z_frac[0])  + '   ')
             length = int(len(z_frac[0])) - 2
             shift_2_xyz.write("0.")
             new = z_frac[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_xyz.write('0')
             shift_2_xyz.write(str(new[0]) + '   ')
             shift_2_xyz.write('\n')

shift_2_xyz.close()

######################################### ANALYSE SHIFTS XYZ FRAC #####################################

file = open("shift_1_xyz.dat")
shift_1 = []

for line in file:
    shift_1.append(line.strip())
file.close()

file = open("shift_2_xyz.dat")
shift_2 = []

for line in file:
    shift_2.append(line.strip())
file.close()

tmp = []
tmp2 = []

shifts_xyz_data = open("ReCryst_shift_xyz.dat","a")

for n in range(0,atom):
    tmp = shift_1[n].split()
    tmp2 = shift_2[n].split()
    shifts_xyz_data.write(str(tmp[0]) + '  ')
    diff_x_frac = abs(float(tmp[1])-float(tmp2[1]))
    shift_ESD_x = float(diff_x_frac)/float(tmp2[2])
    diff_y_frac = abs(float(tmp[3])-float(tmp2[3]))
    shift_ESD_y = float(diff_y_frac)/float(tmp2[4])
    diff_z_frac = abs(float(tmp[5])-float(tmp2[5]))
    shift_ESD_z = float(diff_z_frac)/float(tmp2[6])
    shifts_xyz_data.write("%.6f" % float(shift_ESD_x) + '  ' )
    shifts_xyz_data.write("%.6f" % float(shift_ESD_y) + '  ' )
    shifts_xyz_data.write("%.6f" % float(shift_ESD_z) + '  ' )
    shifts_xyz_data.write('\n')
shifts_xyz_data.write("END CYCLE 1")
shifts_xyz_data.write('\n' )
shifts_xyz_data.write('\n' )

##############################  ANALYSIS OF ADPs   ###########################

file = open("xd_geo.cif")
tmp = []

for line in file:
    tmp.append(line.strip())
file.close()

shift_2_adp = open("shift_2_adp.dat", "a")

for k in range(1,len(tmp)):
     if '_atom_site_aniso_U_23' in tmp[k]:
         for b in range(1,int(atom)+1):
             z = tmp[k + b].split()
             z = tmp[k + b].split()
             u11 = z[1].split('(')
             if len(u11) == 1:
                 u11.append('1')
             u22 = z[2].split('(')
             if len(u22) == 1:
                 u22.append('1')
             u33 = z[3].split('(')
             if len(u33) == 1:
                 u33.append('1')
             u12 = z[4].split('(')
             if len(u12) == 1:
                 u12.append('1')
             u13 = z[5].split('(')
             if len(u13) == 1:
                 u13.append('1')
             u23 = z[6].split('(')
             if len(u23) == 1:
                 u23.append('1')
             shift_2_adp.write(str(z[0]) +  '   ')
             shift_2_adp.write("%.6f" % float(u11[0])  + '   ')
             length = int(len(u11[0])) - 2
             shift_2_adp.write("0.")
             new = u11[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_adp.write('0')
             shift_2_adp.write(str(new[0]) + '   ')
             shift_2_adp.write("%.6f" % float(u22[0])  + '   ')
             length = int(len(u22[0])) - 2
             shift_2_adp.write("0.")
             new = u22[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_adp.write('0')
             shift_2_adp.write(str(new[0]) + '   ')
             shift_2_adp.write("%.6f" % float(u33[0])  + '   ')
             length = int(len(u33[0])) - 2
             shift_2_adp.write("0.")
             new = u33[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_adp.write('0')
             shift_2_adp.write(str(new[0]) + '   ')
             shift_2_adp.write("%.6f" % float(u12[0])  + '   ')
             length = int(len(u12[0])) - 2
             shift_2_adp.write("0.")
             new = u12[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_adp.write('0')
             shift_2_adp.write(str(new[0]) + '   ')
             shift_2_adp.write("%.6f" % float(u13[0])  + '   ')
             length = int(len(u13[0])) - 2
             shift_2_adp.write("0.")
             new = u13[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_adp.write('0')
             shift_2_adp.write(str(new[0]) + '   ')
             shift_2_adp.write("%.6f" % float(u23[0])  + '   ')
             length = int(len(u23[0])) - 2
             shift_2_adp.write("0.")
             new = u23[1].split(')')
             for n in range(0,length-len(new[0])):
                 shift_2_adp.write('0')
             shift_2_adp.write(str(new[0]) + '   ')
             shift_2_adp.write('\n')
             if '_geom_special_details' in tmp[k + b + 2]:
                 break

shift_2_adp.close()

##########################################   ANALYSE SHIFTS ADP    #####################################

file = open("shift_1_adp.dat")
shift_1_adp = []

for line in file:
    shift_1_adp.append(line.strip())
file.close()

file = open("shift_2_adp.dat")
shift_2_adp = []

for line in file:
    shift_2_adp.append(line.strip())
file.close()

tmp_adp = []
tmp2_adp = []

shifts_adp_data = open("ReCryst_shift_adp.dat","a")

for n in range(0,atom):
    tmp2_adp = shift_2_adp[n].split()
    if 'H' in tmp2_adp[0]:
        break
    tmp_adp = shift_1_adp[n].split()
    shifts_adp_data.write(str(tmp_adp[0]) + '  ')
    diff_u11 = abs(float(tmp_adp[1])-float(tmp2_adp[1]))
    shift_ESD_u11 = float(diff_u11)/float(tmp2_adp[2])
    diff_u22 = abs(float(tmp_adp[3])-float(tmp2_adp[3]))
    shift_ESD_u22 = float(diff_u22)/float(tmp2_adp[4])
    diff_u33 = abs(float(tmp_adp[5])-float(tmp2_adp[5]))
    shift_ESD_u33 = float(diff_u33)/float(tmp2_adp[6])
    diff_u12 = abs(float(tmp_adp[7])-float(tmp2_adp[7]))
    shift_ESD_u12 = float(diff_u12)/float(tmp2_adp[8])
    diff_u13 = abs(float(tmp_adp[9])-float(tmp2_adp[9]))
    shift_ESD_u13 = float(diff_u13)/float(tmp2_adp[10])
    diff_u23 = abs(float(tmp_adp[11])-float(tmp2_adp[11]))
    shift_ESD_u23 = float(diff_u23)/float(tmp2_adp[12])
    shifts_adp_data.write("%.6f" % float(shift_ESD_u11) + '  ' )
    shifts_adp_data.write("%.6f" % float(shift_ESD_u22) + '  ' )
    shifts_adp_data.write("%.6f" % float(shift_ESD_u33) + '  ' )
    shifts_adp_data.write("%.6f" % float(shift_ESD_u12) + '  ' )
    shifts_adp_data.write("%.6f" % float(shift_ESD_u13) + '  ' )
    shifts_adp_data.write("%.6f" % float(shift_ESD_u23) + '  ' )
    shifts_adp_data.write('\n')
shifts_adp_data.write("END CYCLE 1")
shifts_adp_data.write('\n' )
shifts_adp_data.write('\n' )


################################## PREPARE FOR FURTHER CYCLES ############################

subprocess.call("rm xd_geo.cif", shell = True)
subprocess.call("mv shift_2_xyz.dat shift_1_xyz.dat", shell = True)
subprocess.call("mv shift_2_adp.dat shift_1_adp.dat", shell = True)

######################################### Next Cycles ####################################

Cycles = int(Cycles)
ref = 1

while ref < Cycles:

    file = open(Name)
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    f = open("crystal.d12", "a")
    
    for i in range(1,len(tmp)):
        if '_space_group_name_H-M_alt' in tmp[i]:
             space = i
        if '_cell_length_a' in tmp[i]:
             check = i
        if '_diffrn_reflns_number' in tmp[i]:
             number = i
        if '_diffrn_radiation_wavelength' in tmp[i]:
             wave = i
    
    x = tmp[space].split("'")
    
    f.write('RECRYST')
    f.write('\nCRYSTAL')
    f.write('\n1 0 0')
    f.write('\n' +  str(x[1]) )
    f.write('\n')
    
    test_1 = 0.0
    
    for k in range(1,len(tmp)):
         if '_cell_length_a' in tmp[k]:
                     for u in range(0,6):
                         check = k + u
                         z = tmp[check].split()
                         h = z[1].split("(")
                         if float(h[0]) == 90.0 or float(h[0]) == 120.0 or float(h[0]) == test_1:
                             continue
                         f.write(str(h[0]) + ' ' )
                         test_1 = float(h[0])
    f.write('\n')
    
    for k in range(1,len(tmp)):
         if '_atom_site_disorder_group' in tmp[k]:
              for u in range(1,1000):
                   z = tmp[k + u].split()
                   if 'loop_' in tmp[k + u + 2]:
                       break
    b = 0
    atom = int(u)
    
    f.write(str(atom))
    f.write('\n')
    
    file = open('xd.res')
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    for i in range(0,len(tmp)):
        if '(' in tmp[i]:
            new = tmp[i].split()
            two = new[0].split('(')
            for j in range(0,35):
                if two[0] in atom_list[j]:
                    g = j + 1
                    f.write(str(g))
                    f.write('  '+ new[12] + '  ' + new[13] + '  ' + new[14])
                    f.write('\n')
                    break
    
    f.write('BASISSET')
    f.write('\n' + str(Basis))
    f.write('\nDFT')
    f.write('\n' +str(Theory))
    f.write('\nEND')
    f.write('\nSHRINK')
    f.write('\n' + str(grid))
    f.write('\nEND')
    
    f.close()
    
    subprocess.call("mv xd.hkl save.hkl", shell = True)
    subprocess.call("mv xd.res save.res", shell = True)
    subprocess.call("rm xd*", shell = True)
    subprocess.call(str(pcrystal_command), shell = True)
    subprocess.call("rm crystal.d12", shell = True)
    
    f = open("INPUT", "a")
    
    #1. Schreiben eines Inputfiles zur Berechnung der statischen Strukturfaktoren mit PROPERTIES
    
    f.write('XFAC')
    
    print('')
    print('')
    print('#    #  #####     #       ######')
    print(' #  #   #        # #      #')
    print('   #    #####   #   #     #')
    print('  #     #      #######    #')
    print(' #  #   #     #       #   #')
    print('#    #  #    #         #  ######')
    
    print('')
    print('###################################################################')
    print('')
    print('Calculations of structure factors - F(hkl)')
    print('')
    print('###################################################################')
    print('')

    subprocess.call("cp crystal.d3_save crystal.d3", shell = True)
    subprocess.call(str(pproperties_command), shell = True)
    
    v = open("check.hkl", "a")
    
    file = open('crystal.out')
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    for k in range(0,len(tmp)):
        if 'X-RAY STATIC STRUCTURE FACTORS' in tmp[k]:
            for n in range(k + 10,len(tmp)):
                w = tmp[n]
                h = w[-66:-63]
                k = w[-63:-60]
                l = w[-60:-57]
                I = w[-10:]
                I = float(I)**2
                s = float(I) * 0.01
    #           print(h, k, l, I, s)
                v.write("%4i %3i %3i %7.3f %7.3f" % (int(h), int(k), int(l), float(I), float(s)))
                v.write("\n")
                if int(h)==0 and int(k)==0 and int(l)==0:
                    continue
                if 'XFAC' in tmp[n+1]:
                    break
    
    v.close()
    
#    subprocess.call("rm fort* diis* dffit3.dat", shell = True)
    
    # Theoretical_Multipole_Parameter_Generation
    
    #1. Generate Shelx-INS from CIF: CHECK
    
    q = open("shelx.ins", "a")
    
    q.write('TITL CHECK')
    q.write('\n')
    
    file = open(Name)
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    for i in range(1,len(tmp)):
        if '_shelx_res_file' in tmp[i]:
            for d in range(i+5,len(tmp)):
                if 'FVAR' in tmp[d]:
                    q.write(tmp[d])
                    q.write('\n')
                    for o in range(d+1, len(tmp)):
                        if 'HKLF 4' in tmp[o]:
                            q.write('HKLF 4')
                            break
                        if '=' in tmp[o]:
                            new = tmp[o].split()
                            for m in range(0,6):
                                q.write(new[m] + '  ')
                            q.write('10.0000')
                            q.write('\n')
                        if 'H' in tmp[o]:
                            new = tmp[o].split()
                            for m in range(0,6):
                                q.write(new[m] + '  ')
                            q.write('10.0000')
                            q.write('\n')
                    break
                q.write(tmp[d])
                q.write('\n')
    
    q.close()
    
    #2. Start Multipol-Refinement
    
    #2.1 xdini
    subprocess.call("bash /usr/users/patzer/xd_data/xd_start.sh", shell = True)
    subprocess.call("mv check.hkl shelx.hkl", shell = True)
    subprocess.call("/usr/users/patzer/bin/shelxl shelx", shell = True)
    subprocess.call("mv shelx.cif xd.cif", shell = True)
    subprocess.call("mv shelx.fcf xd.fcf", shell = True)
    subprocess.call("/usr/users/patzer/bin/xdini check cif vm", shell = True)
    subprocess.call("mv save.res xd.inp", shell = True)
    
    #edit xd.mas for refinement!!!
    
    file = open("xd.mas")
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    t = open("xd_new.mas", "a")
    
    for i in range(0,len(tmp)):
        if 'SELECT  model' in tmp[i]:
            t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
            t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
            t.write('\n')
            continue
        if 'SELECT  cycle' in tmp[i]:
            continue
        if 'SCAT' in tmp[i]:
            t.write(str(tmp[i]))
            t.write('\n')
            for q in range(i+1,len(tmp)):
                if 'END SCAT' in tmp[q]:
                    break
                new = tmp[q].split('.')
                t.write(str(new[0]))
                t.write('.0000  0.0000  0.000')
                t.write('\n')
            break
        t.write(tmp[i])
        t.write('\n')
    
    t.write('END SCAT')
    t.write('\n' + '!------------------------------------------------------------------------------')
    t.write('\n' + 'ATOM     ATOM0    AX1 ATOM1    ATOM2   AX2 R/L TP TBL KAP LMX SITESYM  CHEMCON')
    t.write('\n')
    
    kappa_value = 0
    vib_static = 0
    
    for n in range(0, len(tmp)):
        if 'CHEMCON' in tmp[n]:
            for b in range(n+1, n+atom+1):
                kappa_new = tmp[b].split()
                t.write(str(kappa_new[0]) + '  ')
                t.write(str(kappa_new[1]) + '  ')
                t.write(str(kappa_new[2]) + '  ')
                t.write(str(kappa_new[3]) + '  ')
                t.write(str(kappa_new[4]) + '  ')
                t.write(str(kappa_new[5]) + '  ')
                t.write(str(kappa_new[6]) + '  ')
                t.write(str(vib_static) + '  ')
                t.write(str(kappa_new[8]) + '  ')
                kappa_value = kappa_value + 1
                t.write(str(kappa_value) + '  ')
                t.write(str(kappa_new[10]) + '  ')
                t.write(str(kappa_new[11]) + '  ')
                t.write('\n')
    
    
    for p in range(0,len(tmp)):
        if 'END ATOM' in tmp[p]:
            for i in range(p,len(tmp)):
                if 'KEEP     kappa' in tmp[i]:
                    t.write('KEEP     kappa' + ' ')
                    for i in range(1,atom+1):
                        t.write(str(i) + ' ')
                    t.write('\n')
                    continue
                if '!DMSDA' in tmp[i]:
                    t.write('DMSDA    1.1  1.8')
                    continue
                if '!FOUR' in tmp[i]:
                    t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
                    t.write('\n')
                    continue
                if 'KAPPA' in tmp[i]:
                    break
                if 'KEY     XYZ' in tmp[i]:
                    t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
                    t.write('\n')
                    for h in range(i+1, len(tmp)):
                        new = tmp[h].split()
                        if 'H(' in tmp[h]:
                            t.write(new[0])
                            t.write('  000 000000 0000000000 000000000000000 10 111 11111 0000000 000000000')
                            t.write('\n')
                            continue
                        if '111 111111 0000000000 000000000000000' in tmp[h]:
                            t.write(new[0])
                            t.write('  000 111111 0000000000 000000000000000 10 111 11111 1111111 111111111')
                            t.write('\n')
                            continue
                        if 'KAPPA' in tmp[h]:
                            break
                        t.write(tmp[h])
                        t.write('\n')
                    break
                t.write(tmp[i])
                t.write('\n')
    
    
    for p in range(1, atom + 1):
        t.write('KAPPA   000000')
        t.write('\n')
    
    for p in range(0,len(tmp)):
        if 'EXTCN   0000000' in tmp[p]:
            for g in range(p, len(tmp)):
                t.write(str(tmp[g]))
                t.write('\n')
    
    t.close()

    # edit END
    
    subprocess.call("mv xd_new.mas xd.mas", shell = True)
    
    print('')
    print('')
    print('#               #  #       #  #     ############ #  ######   #######  #')
    print('##             ##  #       #  #          #       #  #     #  #     #  #')
    print('# #           # #  #       #  #          #       #  #     #  #     #  #')
    print('#  #         #  #  #       #  #          #       #  #     #  #     #  #')
    print('#   #       #   #  #       #  #          #       #  ######   #     #  #')
    print('#    #     #    #  #       #  #          #       #  #        #     #  #')
    print('#     #   #     #  #       #  #          #       #  #        #     #  #')
    print('#      # #      #  #       #  #          #       #  #        #     #  #')
    print('#       #       #  #########  ########   #       #  #        #######  #########')
    print('')
    print('')
    
    print('')
    print('')
    print('####### #   #  ####  #### ####   # #####')
    print('   #    #   #  #     #  # #   #  # #')
    print('   #    #####  ####  #  # ####   # ##### ')
    print('   #    #   #  #     #  # # #    # #')
    print('   #    #   #  ####  #### #  #   # #####')
    print('')
    print('Multipoles - spherical harmonics')
    print('')
    
    subprocess.call("rm shelx* INPUT", shell = True)
    subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)

    ############################ INSERT FURTHER REFINENT OPTIONS THEORY ####################
    
    subprocess.call("mv xd.res xd.inp", shell = True)

    ############################################# NEXT STEP ################################################
    
    file = open("xd.mas")
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    t = open("xd_new.mas", "a")
    
    for i in range(0,len(tmp)):
        if 'SELECT  model' in tmp[i]:
            t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
            t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
            t.write('\n')
            continue
        if 'SELECT  cycle' in tmp[i]:
            continue
        if '!DMSDA' in tmp[i]:
            t.write('DMSDA    1.1  1.8')
            continue
        if '!FOUR' in tmp[i]:
            t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
            t.write('\n')
            continue
        if 'KEY     XYZ' in tmp[i]:
            t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
            t.write('\n')
            for h in range(i+1, len(tmp)):
                new = tmp[h].split()
                if 'H(' in tmp[h]:
                    t.write(new[0])
                    t.write('  000 000000 0000000000 000000000000000 00 000 00000 0000000 000000000')
                    t.write('\n')
                    continue
                if '  000 111111 0000000000 000000000000000 10 111 11111 1111111 111111111' in tmp[h]:
                    t.write(new[0])
                    t.write('  000 111111 0000000000 000000000000000 00 000 00000 0000000 000000000')
                    t.write('\n')
                    continue
                if 'KAPPA   000000' in tmp[h]:
                    if 'EXTCN' in tmp[h+1]:
                        t.write('KAPPA   111111')
                        t.write('\n')
                        continue
                    t.write('KAPPA   111111')
                    t.write('\n')
                    continue
                t.write(tmp[h])
                t.write('\n')
            break
        t.write(tmp[i])
        t.write('\n')
    
    t.close()
    
    subprocess.call("mv xd_new.mas xd.mas", shell = True)
    
    print('')
    print('')
    print('####### #   #  ####  #### ####   # #####')
    print('   #    #   #  #     #  # #   #  # #')
    print('   #    #####  ####  #  # ####   # ##### ')
    print('   #    #   #  #     #  # # #    # #')
    print('   #    #   #  ####  #### #  #   # #####')
    print('')
    print('Kappa - radial distribution')
    print('')
    
    subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)
    subprocess.call("mv xd.res xd.inp", shell = True)
    
    ############################################## NEXT STEP ################################################
    
    file = open("xd.mas")
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    t = open("xd_new.mas", "a")
    
    for i in range(0,len(tmp)):
        if 'SELECT  model' in tmp[i]:
            t.write('SELECT  model 0 2 1 0 based_on F^2 test verbose 1')
            t.write('\nSELECT  cycle 40 dampk 1. cmin 0.6 cmax 1. eigcut 1.d-09 convcrit 0.0')
            t.write('\n')
            continue
        if 'SELECT  cycle' in tmp[i]:
            continue
        if '!DMSDA' in tmp[i]:
            t.write('DMSDA    1.1  1.8')
            continue
        if '!FOUR' in tmp[i]:
            t.write('\nFOUR     fmod1 4 2 0 0  fmod2 -1 2 0 0')
            t.write('\n')
            continue
        if 'KEY     XYZ' in tmp[i]:
            t.write('KEY     XYZ --U2-- ----U3---- ------U4------- M- -D- --Q-- ---O--- ----H----')
            t.write('\n')
            for h in range(i+1, len(tmp)):
                new = tmp[h].split()
                if 'H(' in tmp[h]:
                    t.write(new[0])
                    t.write('  000 000000 0000000000 000000000000000 00 000 00000 0000000 000000000')
                    t.write('\n')
                    continue
                if '  000 111111 0000000000 000000000000000 00 000 00000 0000000 000000000' in tmp[h]:
                    t.write(new[0])
                    t.write('  000 000000 0000000000 000000000000000 10 111 11111 1111111 111111111')
                    t.write('\n')
                    continue
                if 'KAPPA   111111' in tmp[h]:
                    if 'EXTCN' in tmp[h+1]:
                        t.write('KAPPA   000000')
                        t.write('\n')
                        continue
                    t.write('KAPPA   000000')
                    t.write('\n')
                    continue
                t.write(tmp[h])
                t.write('\n')
            break
        t.write(tmp[i])
        t.write('\n')
    
    t.close()
    
    subprocess.call("mv xd_new.mas xd.mas", shell = True)
    
    print('')
    print('')
    print('####### #   #  ####  #### ####   # #####')
    print('   #    #   #  #     #  # #   #  # #')
    print('   #    #####  ####  #  # ####   # ##### ')
    print('   #    #   #  #     #  # # #    # #')
    print('   #    #   #  ####  #### #  #   # #####')
    print('')
    print('All parameters')
    print('')
    
    subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)
    
    ########################################## END OF THEORY PART ###########################################

    subprocess.call("mv xd.res theory.res", shell = True)
    subprocess.call("rm xd*", shell = True)
    
    subprocess.call("cp save_1.mas xd.mas", shell = True)
    subprocess.call("cp save.hkl xd.hkl", shell = True)
    subprocess.call("mv theory.res xd.inp", shell = True)
    
    print('')
    print('')
    print('####  #### #### # #   # #####')
    print('#  #  #    #    # ##  # #')
    print('###   ###  ###  # # # # ###')
    print('# #   #    #    # #  ## #')
    print('#  #  #### #    # #   # #####')
    print('')
    print('')
    
    subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)

    subprocess.call("mv xd.res xd.inp", shell = True)
    subprocess.call("rm xd.mas", shell = True)
    subprocess.call("cp save_2.mas xd.mas", shell = True)

    print('')
    print('')
    print('####  #### #### # #   # #####')
    print('#  #  #    #    # ##  # #')
    print('###   ###  ###  # # # # ###')
    print('# #   #    #    # #  ## #')
    print('#  #  #### #    # #   # #####')
    print('')
    print('')

    subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)

    subprocess.call("mv xd.res xd.inp", shell = True)
    subprocess.call("rm xd.mas", shell = True)
    subprocess.call("cp save_3.mas xd.mas", shell = True)
    
    print('')
    print('')
    print('####  #### #### # #   # #####')
    print('#  #  #    #    # ##  # #')
    print('###   ###  ###  # # # # ###')
    print('# #   #    #    # #  ## #')
    print('#  #  #### #    # #   # #####')
    print('')
    print('')

    subprocess.call("/usr/users/patzer/bin/xdlsm check", shell = True)

    ref = ref + 1
    
    ########################DOKU###########################
    
    save_2 = open("save_2.xyz", "a")

    file = open('xd_lsm.out')
    doku = []
    
    for line in file:
        doku.append(line.strip())
    file.close()
    
    for p in range(0,len(doku)):
        if 'Residuals after final cycle' in doku[p]:
            for m in range(p,len(doku)):
                if 'Variables after final cycle' in doku[m]:
                    break
                out.write(doku[m])
                out.write('\n')
            break
    
    trj.write(str(atomnumber))
    trj.write('\n')
    trj.write('\n')
    
    for p in range(0,len(doku)):
        if 'Atomic parameters in Cartesian crystal system' in doku[p]:
            for m in range(p+3, len(doku)):
                if '-----' in doku[m]:
                    break
                if '(' in doku[m]:
                    new = doku[m].split()
                    one = new[0].split('(')
                    one = one[0]
                    trj.write(str(one))
                    trj.write('  ' + new[1] + '   ' + new[2] + '   ' + new[3])
                    trj.write('\n')
                    save_2.write('  ' + new[1] + '   ' + new[2] + '   ' + new[3])
                    save_2.write('\n')
    save_2.write('*')
    save_2.close()
    ################################### DOKU END ###########################################

    #################################### ANALYSE SHIFTS XYZ FRAC #############################
    
    subprocess.call("/usr/users/patzer/bin/xdgeom", shell = True)
    
    file = open("xd_geo.cif")
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    shift_2_xyz = open("shift_2_xyz.dat", "a")
    
    for k in range(1,len(tmp)):
         if '_atom_site_U_iso_or_equiv' in tmp[k]:
             for b in range(1,int(atom)+1):
                 z = tmp[k + b].split()
                 x_frac = z[1].split('(')
                 if len(x_frac) == 1:
                     x_frac.append('1')
                 y_frac = z[2].split('(')
                 if len(y_frac) == 1:
                     y_frac.append('1')
                 z_frac = z[3].split('(')
                 if len(z_frac) == 1:
                     z_frac.append('1')
                 new = z[0].split('(')
                 shift_2_xyz.write(str(new[0]) +  '   ')
                 shift_2_xyz.write("%.6f" % float(x_frac[0])  + '   ')
                 length = int(len(x_frac[0])) - 2
                 shift_2_xyz.write("0.")
                 new = x_frac[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_xyz.write('0')
                 shift_2_xyz.write(str(new[0]) + '   ')
                 shift_2_xyz.write("%.6f" % float(y_frac[0])  + '   ')
                 length = int(len(y_frac[0])) - 2
                 shift_2_xyz.write("0.")
                 new = y_frac[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_xyz.write('0')
                 shift_2_xyz.write(str(new[0]) + '   ')
                 shift_2_xyz.write("%.6f" % float(z_frac[0])  + '   ')
                 length = int(len(z_frac[0])) - 2
                 shift_2_xyz.write("0.")
                 new = z_frac[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_xyz.write('0')
                 shift_2_xyz.write(str(new[0]) + '   ')
                 shift_2_xyz.write('\n')
    
    shift_2_xyz.close()
    
    ######################################### ANALYSE SHIFTS XYZ FRAC #####################################
    
    file = open("shift_1_xyz.dat")
    shift_1 = []
    
    for line in file:
        shift_1.append(line.strip())
    file.close()
    
    file = open("shift_2_xyz.dat")
    shift_2 = []
    
    for line in file:
        shift_2.append(line.strip())
    file.close()
    
    tmp = []
    tmp2 = []
    
    shifts_xyz_data = open("ReCryst_shift_xyz.dat","a")
    
    for n in range(0,atom):
        tmp = shift_1[n].split()
        tmp2 = shift_2[n].split()
        shifts_xyz_data.write(str(tmp[0]) + '  ')
        diff_x_frac = abs(float(tmp[1])-float(tmp2[1]))
        shift_ESD_x = float(diff_x_frac)/float(tmp2[2])
        diff_y_frac = abs(float(tmp[3])-float(tmp2[3]))
        shift_ESD_y = float(diff_y_frac)/float(tmp2[4])
        diff_z_frac = abs(float(tmp[5])-float(tmp2[5]))
        shift_ESD_z = float(diff_z_frac)/float(tmp2[6])
        shifts_xyz_data.write("%.6f" % float(shift_ESD_x) + '  ' )
        shifts_xyz_data.write("%.6f" % float(shift_ESD_y) + '  ' )
        shifts_xyz_data.write("%.6f" % float(shift_ESD_z) + '  ' )
        shifts_xyz_data.write('\n')
    shifts_xyz_data.write("END CYCLE" + ' ' + str(ref))
    shifts_xyz_data.write('\n' )
    shifts_xyz_data.write('\n' )
    
    ############################## NEXT ADP ANALYSIS ###########################
    
    file = open("xd_geo.cif")
    tmp = []
    
    for line in file:
        tmp.append(line.strip())
    file.close()
    
    shift_2_adp = open("shift_2_adp.dat", "a")
    
    for k in range(1,len(tmp)):
         if '_atom_site_aniso_U_23' in tmp[k]:
             for b in range(1,int(atom)+1):
                 z = tmp[k + b].split()
                 z = tmp[k + b].split()
                 u11 = z[1].split('(')
                 if len(u11) == 1:
                     u11.append('1')
                 u22 = z[2].split('(')
                 if len(u22) == 1:
                     u22.append('1')
                 u33 = z[3].split('(')
                 if len(u33) == 1:
                     u33.append('1')
                 u12 = z[4].split('(')
                 if len(u12) == 1:
                     u12.append('1')
                 u13 = z[5].split('(')
                 if len(u13) == 1:
                     u13.append('1')
                 u23 = z[6].split('(')
                 if len(u23) == 1:
                     u23.append('1')
                 shift_2_adp.write(str(z[0]) +  '   ')
                 shift_2_adp.write("%.6f" % float(u11[0])  + '   ')
                 length = int(len(u11[0])) - 2
                 shift_2_adp.write("0.")
                 new = u11[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_adp.write('0')
                 shift_2_adp.write(str(new[0]) + '   ')
                 shift_2_adp.write("%.6f" % float(u22[0])  + '   ')
                 length = int(len(u22[0])) - 2
                 shift_2_adp.write("0.")
                 new = u22[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_adp.write('0')
                 shift_2_adp.write(str(new[0]) + '   ')
                 shift_2_adp.write("%.6f" % float(u33[0])  + '   ')
                 length = int(len(u33[0])) - 2
                 shift_2_adp.write("0.")
                 new = u33[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_adp.write('0')
                 shift_2_adp.write(str(new[0]) + '   ')
                 shift_2_adp.write("%.6f" % float(u12[0])  + '   ')
                 length = int(len(u12[0])) - 2
                 shift_2_adp.write("0.")
                 new = u12[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_adp.write('0')
                 shift_2_adp.write(str(new[0]) + '   ')
                 shift_2_adp.write("%.6f" % float(u13[0])  + '   ')
                 length = int(len(u13[0])) - 2
                 shift_2_adp.write("0.")
                 new = u13[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_adp.write('0')
                 shift_2_adp.write(str(new[0]) + '   ')
                 shift_2_adp.write("%.6f" % float(u23[0])  + '   ')
                 length = int(len(u23[0])) - 2
                 shift_2_adp.write("0.")
                 new = u23[1].split(')')
                 for n in range(0,length-len(new[0])):
                     shift_2_adp.write('0')
                 shift_2_adp.write(str(new[0]) + '   ')
                 shift_2_adp.write('\n')
                 if '_geom_special_details' in tmp[k + b + 2]:
                     break
    
    shift_2_adp.close()
    
    
    
    ########################################## ANALYSE ADP  SHIFTS  #####################################
    
    file = open("shift_1_adp.dat")
    shift_1_adp = []
    
    for line in file:
        shift_1_adp.append(line.strip())
    file.close()
    
    file = open("shift_2_adp.dat")
    shift_2_adp = []
    
    for line in file:
        shift_2_adp.append(line.strip())
    file.close()
    
    tmp_adp = []
    tmp2_adp = []
    
    shifts_adp_data = open("ReCryst_shift_adp.dat","a")
    
    for n in range(0,atom):
        tmp2_adp = shift_2_adp[n].split()
    #    if 'H' in tmp2_adp[0]:
    #        break
        tmp_adp = shift_1_adp[n].split()
        shifts_adp_data.write(str(tmp_adp[0]) + '  ')
        diff_u11 = abs(float(tmp_adp[1])-float(tmp2_adp[1]))
        shift_ESD_u11 = float(diff_u11)/float(tmp2_adp[2])
        diff_u22 = abs(float(tmp_adp[3])-float(tmp2_adp[3]))
        shift_ESD_u22 = float(diff_u22)/float(tmp2_adp[4])
        diff_u33 = abs(float(tmp_adp[5])-float(tmp2_adp[5]))
        shift_ESD_u33 = float(diff_u33)/float(tmp2_adp[6])
        diff_u12 = abs(float(tmp_adp[7])-float(tmp2_adp[7]))
        shift_ESD_u12 = float(diff_u12)/float(tmp2_adp[8])
        diff_u13 = abs(float(tmp_adp[9])-float(tmp2_adp[9]))
        shift_ESD_u13 = float(diff_u13)/float(tmp2_adp[10])
        diff_u23 = abs(float(tmp_adp[11])-float(tmp2_adp[11]))
        shift_ESD_u23 = float(diff_u23)/float(tmp2_adp[12])
        shifts_adp_data.write("%.6f" % float(shift_ESD_u11) + '  ' )
        shifts_adp_data.write("%.6f" % float(shift_ESD_u22) + '  ' )
        shifts_adp_data.write("%.6f" % float(shift_ESD_u33) + '  ' )
        shifts_adp_data.write("%.6f" % float(shift_ESD_u12) + '  ' )
        shifts_adp_data.write("%.6f" % float(shift_ESD_u13) + '  ' )
        shifts_adp_data.write("%.6f" % float(shift_ESD_u23) + '  ' )
        shifts_adp_data.write('\n')
    shifts_adp_data.write("END CYCLE" + ' ' + str(ref))
    shifts_adp_data.write('\n' )
    shifts_adp_data.write('\n' )
    

    ################################## PREPARE FOR FURTHER CYCLES ############################
    
    subprocess.call("rm xd_geo.cif", shell = True)
    subprocess.call("mv shift_2_xyz.dat shift_1_xyz.dat", shell = True)
    subprocess.call("mv shift_2_adp.dat shift_1_adp.dat", shell = True)

    ######################################### Next Cycles ####################################


    ############################# CHECK OF CONVERGENCE #####################################
    
    diff = open("ReCryst_convergence.log", "a")
    
    file = open('save_1.xyz')
    save_1 = []

    for line in file:
        save_1.append(line.strip())
    file.close()

    file = open('save_2.xyz')
    save_2 = []

    for line in file:
        save_2.append(line.strip())
    file.close()
    
    diff_x_sum = 0.0
    diff_y_sum = 0.0
    diff_z_sum = 0.0
    diff_sum = 0.0
    diff_all_sum = 0.0
    RMS = 0.0

    for i in range(0,len(save_1)):
        if '*' in save_1[i]:
            break
        one = save_1[i].split()
        two = save_2[i].split()
        diff_x = (abs(float(one[0])-float(two[0])))**2
        diff_y = (abs(float(one[1])-float(two[1])))**2
        diff_z = (abs(float(one[2])-float(two[2])))**2
        diff_sum = sqrt(diff_x + diff_y + diff_z)
        diff_sum = diff_sum * diff_sum
        diff_all_sum = diff_all_sum + diff_sum

    RMS = 1.0/float(atomnumber) * sqrt(float(diff_all_sum))
    diff.write('  ' + str(ref) + '                      ' + str(RMS))
    diff.write('\n')

    subprocess.call("mv save_2.xyz save_1.xyz", shell = True)

    ######################### CONVERGENCE REACHED ? ########################################

    if float(RMS) < 0.0001:
        print('')
        print('--------------------------- HURRAY ---------------------------------')
        print('')
        print('CONVERGENCE of coordinates reached - will leave refining cycle')
        print('')
        break

    ########################################################################################


############################### CIF GENERATION ##################################

print('Generation of new CIF ....')
subprocess.call("/usr/users/patzer/bin/xdgeom", shell = True)
#subprocess.call("mv xd_geo.cif ReCrystal.cif", shell = True)
print('')

#Write CIF without Pseudo Atom ------------------------------------------

Re_CIF = open("ReCryst.cif", "a")

file = open("xd_geo.cif")
xdgeo = []

for line in file:
    xdgeo.append(line.strip())
file.close()

for i in range(0,len(xdgeo)):
    if 'DUM' in xdgeo[i]:
        continue
    Re_CIF.write(str(xdgeo[i]))
    Re_CIF.write('\n')

#Write CIF END ----------------------------------------------------------

############################ CIF GENERATION END #################################

time = datetime.datetime.now()
out.write('\n')
out.write('Refinement finished at :' + str(time))
diff.write('--------------------------------------------------')
diff.write('\nRefinement finished at: ' + str(time))
out.close()
trj.close()

print('##############################################################')
print('')
print('Refinement started  at: ', str(time_start))
print('Refinement fineshed at: ', str(time))
print('')
print('################# PROGRAM END SUCCESSFUL #####################')
print('') 
    
    
     
    
    


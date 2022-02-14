## Script to predict and visualize the idealized theoretical cases of an equal mixture of two gases separated with STAM-17-OEt
    # select 2 gases of interest and edit sheet_name (lines 24 and 32) 
    # rename plt.xlabel, plt.ylabel and plt.title labels to gas choices (lines 77 - 79) 
    # rename ax.annotate to the first of the 2 gases of interest (lines 87 - 88) 
    # save figure as .tiff  or  .png  or  .pdf (line 101)


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import matplotlib.lines as mlines
from matplotlib import rcParams

fxn_groups=['F–','CN–','CH$_3$–','COOH–','NH$_2$–','OH–']
pos_groups = ['R$_2$','R$_6$','R$_{2, 6}$','R$_{4, 6}$','R$_{2, 4, 6}$']
electrons = ['(non-polar EWG)','(polar EWG)', '(non-polar EDG)','(polar EWG)','(polar EDG)','(polar EDG)']
all_groups = []
for i in range (len(fxn_groups)):
    for j in range(len(pos_groups)):
        combine_group = fxn_groups[i] + pos_groups[j]+' '+ electrons[i]
        all_groups.append(combine_group)
    

# Read in Excel sheet  
# Select 2 gases of interest 
df1 = pd.read_excel('/Users/uche/Box Sync/1.Research/1.Reports/STAM17/Manuscript/Final/Omega/GitHub/STAM-17-OEt_Adsorption_Energies.xlsx',sheet_name="C2H2")
gas1_F=df1.iloc[4:9,2].values
gas1_CN=df1.iloc[11:16,2].values
gas1_CH3=df1.iloc[18:23,2].values
gas1_COOH=df1.iloc[25:30,2].values
gas1_NH2=df1.iloc[32:37,2].values
gas1_OH=df1.iloc[39:44,2].values

df2 = pd.read_excel('/Users/uche/Box Sync/1.Research/1.Reports/STAM17/Manuscript/Final/Omega/GitHub/STAM-17-OEt_Adsorption_Energies.xlsx',sheet_name="C2H4")
gas2_F=df2.iloc[4:9,2].values
gas2_CN=df2.iloc[11:16,2].values
gas2_CH3=df2.iloc[18:23,2].values
gas2_COOH=df2.iloc[25:30,2].values
gas2_NH2=df2.iloc[32:37,2].values
gas2_OH=df2.iloc[39:44,2].values



fig, ax = plt.subplots()
marker_plot = ['o', 'v', 's', '*', 'X']
colors_array = ['r','b','m', 'k','g','cyan']
X_AXIS  = []
Y_AXIS = []
X_AXIS.append(gas1_F)
X_AXIS.append(gas1_CN)
X_AXIS.append(gas1_CH3)
X_AXIS.append(gas1_COOH)
X_AXIS.append(gas1_NH2)
X_AXIS.append(gas1_OH)

Y_AXIS.append(gas2_F)
Y_AXIS.append(gas2_CN)
Y_AXIS.append(gas2_CH3)
Y_AXIS.append(gas2_COOH)
Y_AXIS.append(gas2_NH2)
Y_AXIS.append(gas2_OH)

n_rows = len(X_AXIS)
n_cols = len(X_AXIS[0])

for i in range(n_rows):
    for j in range(n_cols):
        plt.scatter(X_AXIS[i][j],Y_AXIS[i][j], marker=marker_plot[j],color =colors_array[i],facecolor='none')


rcParams['font.family'] = 'arial'
plt.legend(all_groups,loc='best',bbox_to_anchor=(1.0, 1.0),prop={"size":9})



# Rename to gas choices
plt.xlabel('C$_2$H$_2$',fontweight="semibold",fontsize=10)
plt.ylabel('C$_2$H$_4$',fontweight="semibold",fontsize=10)
plt.title('C$_2$H$_2$/C$_2$H$_4$ Separation',fontweight="bold",fontsize=11)

plt.xlim(-130,5)
plt.ylim(-130,5)

# Rename more/less selective for specific gas
right_arrow = dict(boxstyle="RArrow,pad=0.1", fc="r",alpha=0.4, ec="k",lw=0.5)
left_arrow = dict(boxstyle="LArrow,pad=0.1", fc="g",alpha=0.4, ec="k",lw=0.5)
ax.annotate("More selective for C$_2$H$_2$",fontsize=8, xy=(0.2, 0.4), xycoords=ax.transAxes,rotation=-45,bbox=left_arrow)
ax.annotate("Less selective for C$_2$H$_2$",fontsize=8, xy=(0.6, 0.3), xycoords=ax.transAxes,rotation=-45,bbox=right_arrow)

# Plots gridlines
plt.grid(color='gray',alpha=0.3, linestyle='--', linewidth=0.3) 

# Diagonal line independent of the scatter plot data, stays rooted to the axes even if window resized
line = mlines.Line2D([0, 1], [0, 1],linewidth=1,linestyle='--',color='k')
transform = ax.transAxes
line.set_transform(transform)
ax.add_line(line)


# Save figure as .tiff  or  .png  or  .pdf
plt.savefig('gas_selectivity.png',bbox_inches='tight',dpi = 250)

# Show plot
plt.show()

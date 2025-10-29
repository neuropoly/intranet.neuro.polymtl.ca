# MATLAB

MATLAB is installed on some [internal machines](/computing-resources/neuropoly/README.md) (but [not yet all](https://github.com/neuropoly/computers/issues/326)). 

To run MATLAB on your personal computer, follow these instructions:

1. Create a MathWorks Account:
  * Go to the [MathWorks account](https://www.mathworks.com/mwaccount/account/create) creation page and sign up using your PolyMtl email address.
2. Download MATLAB:
  * Visit the [download MATLAB](https://www.mathworks.com/downloads/) page.
  * Select the MATLAB release version you want to download from the dropdown menu.
  * Click the download button.
    * Note: If you are using a recent Mac computer with an M1/M2/M3 chip, click the "Get Apple silicon MATLAB" button.
3. Run the Installer:
  * Open the downloaded installer file.
    * Note: Your operating system may prompt you to provide credentials to install new software.
  * When prompted, log in using your PolyMtl email account credentials associated with your MathWorks account.
  * Read and accept the terms of the license agreement.
4. Select Toolboxes:
  * On the "Select product" tab, choose the toolboxes you need.
    * Note: Selecting all toolboxes will consume significant disk space (~30 GB). Start with the essentials (e.g., core MATLAB, Curve Fitting, Deep Learning, Image Processing, Optimization, Statistics and Machine Learning) and add more later if needed.
5. Complete Installation:
  * Follow the prompts and click "Begin install."
  * Once the installation is complete, you can create a shortcut by navigating to the installation directory and following your operating system's standard procedure.
6. Verify Installation:
  * Launch MATLAB to ensure it opens without errors.

**Additional Notes:**

* You do not need to be connected to the PolyMtl VPN to activate or run MATLAB, as long as you use your PolyMtl email account for licensing.
* If you encounter issues during installation, refer to the MathWorks Support page for troubleshooting.
* To uninstall MATLAB, use the standard uninstallation process for your operating system.

## Figures

Here is an example of how to display and print a figure:

```text
h_fig = figure
set(h_fig,'position',[500,100,800,350]); % set position and size of the figure
h_axes = axes('FontSize',14,'FontName','arial'); % font size of the axis
plot(inspF(i,:)','r','linewidth',2), hold on
plot(expF(i,:)','--b','linewidth',2)
grid % display grid
xlim([0 18]); % set limimts for X-coordinate
ylim([-400 100]);
set(h_axes,'XTick',(1:17)); % number of partitions for X-coordinate
set(h_axes,'XTickLabel',{'Brain';'BS';'C1';'C2';'C3';'C4';'C5';'C6';'C7';'T1';'T2';'T3';'T4';'T5';'T6';'T7';'T8'}); % name of X-coordinate
set(h_fig,'PaperPositionMode','auto'); % for print --> uses the resolution that appears on your screen
legend('inspired','expired')
xlabel('Vertebral level')
ylabel('Field (Hz)')
title(['Subject ',num2str(i)])
print(h_fig,'-depsc',['individual_plots_subj',num2str(i)]);
```

## Resources

* [Matlab to Python\(Numpy\) cheat sheet](http://mathesaurus.sourceforge.net/matlab-numpy.html)

### Toolbox <a id="toolbox"></a>

* [Ezyfit \(curve fitting\)](http://www.mathworks.com/matlabcentral/fileexchange/10176)

## Issues

### Yosemite Issue <a id="yosemite_issue"></a>

Updating Mac OSX to Yosemite causes issues to run MATLAB. Indeed, you won't be able to run Matlab due to some Java requirements. Mathworks released a patch to fix this issue that is available [Here](https://www.dropbox.com/s/bhr8f69bl4odlbc/Matlab2014_Yosemite_patch.zip?dl=0). Follow the instructions in README file to install it.


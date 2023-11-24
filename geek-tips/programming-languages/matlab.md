# MATLAB

MATLAB is installed on some [internal machines](computing-resources/neuropoly) (but [not yet all](https://github.com/neuropoly/computers/issues/326)). If you install MATLAB on your local machine, download the institutional license from [duke](/data/duke), at `duke:/public/software/matlab/license_laboslicsent.dat` and use it to activate your copy. Thereafter, **you must be connected to the [VPN](/computing-resources/neuropoly#vpn)** when using MATLAB because it is a _network license_, meaning the school runs a licensing server, behind the VPN, that authenticates your right to use MATLAB.

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


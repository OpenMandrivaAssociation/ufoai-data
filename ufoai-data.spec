%define	oname	ufoai

Name:		%{oname}-data
Version:	2.4
Release:	1
URL:		http://ufoai.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{oname}/%{oname}-%{version}-data.tar
License:	GPLv2+ and CC-BY and CC-BY-SA and GFDL and MIT and Public Domain and Creative Commons Sampling Plus
Group:		Games/Strategy
Summary:	Data files for %{oname}
BuildArch:	noarch
Requires:	%{oname}

%rename ufo-data

%description
Data files needed to run %{oname}.


%prep

%install
mkdir -p %{buildroot}%{_gamesdatadir}/%{oname}
tar -xf %{SOURCE0} -C %{buildroot}%{_gamesdatadir}/%{oname}

%files
%dir %{_gamesdatadir}/%{oname}
%{_gamesdatadir}/%{oname}/*


%changelog
* Fri May 04 2012 Johnny A. Solbu <solbu@mandriva.org> 2.4-1
+ Revision: 795809
- New version

* Mon Jul 11 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.1-1
+ Revision: 689576
- drop legacy stuff
- import ufoai-data

  + Johnny A. Solbu <solbu@mandriva.org>
    - New version
    - License changes. See "LICENSES" file in ufoai package for details.


* Fri Jul 16 2010 Johnny A. Solbu <johnny@solbu.net> 2.3-1plf
- Upgraded the package.

* Tue Mar 31 2010 Johnny A. Solbu <johnny@solbu.net> 2.2.1-1plf
- Renamed to ufoai.
- Some spec cleanup

* Tue Mar 30 2010 Johnny A. Solbu <johnny@solbu.net> 2.2.1-1plf
- Upgraded the package.

* Fri Feb 20 2004 Per �yvind Karlsen <peroyvind@sintrax.net> 0.10-1plf
- initial plf release

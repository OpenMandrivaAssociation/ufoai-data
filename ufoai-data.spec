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

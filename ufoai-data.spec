%define	oname	ufoai

Name:		%{oname}-data
Version:	2.3.1
Release:	%mkrel 1
URL:		http://ufoai.sourceforge.net/
Source0:	http://sourceforge.net/projects/ufoai/files/UFO_AI%202.x/%{version}/%{oname}-%{version}-data.tar
Source1:	%{oname}-%{version}-data-1maps.pk3
License:	GPLv2+ and CC-BY and CC-BY-SA and GFDL and MIT and Public Domain and Creative Commons Sampling Plus
Group:		Games/Strategy
Summary:	Data files for %{oname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	%{oname}

%rename ufo-data

%description
Data files needed to run %{oname}.


%prep

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_gamesdatadir}/%{oname}
tar -xf %{SOURCE0} -C %{buildroot}%{_gamesdatadir}/%{oname}
install -m644 %{SOURCE1} %{buildroot}%{_gamesdatadir}/%{oname}/base/1maps.pk3

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_gamesdatadir}/%{oname}
%{_gamesdatadir}/%{oname}/*


%define	oname	ufoai

Name:		%{oname}-data
Version:	2.3
Release:	%mkrel 1
URL:		http://ufoai.sourceforge.net/
Source0:	%{oname}-%{version}-data.tar
License:	Distributable
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_gamesdatadir}/%{oname}
%{_gamesdatadir}/%{oname}/*


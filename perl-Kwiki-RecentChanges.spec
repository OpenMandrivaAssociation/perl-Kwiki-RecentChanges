%define module	Kwiki-RecentChanges
%define name	perl-%{module}
%define version 0.14
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Kwiki Recent Changes Plugin
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Kwiki)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
List pages that were recently changed (how long ago can be configured).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


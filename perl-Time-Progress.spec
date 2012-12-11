%define upstream_name       Time-Progress
%define upstream_version    1.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Elapsed and estimated finish time reporting
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl(Module::Build)
BuildRoot:  %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%description
Elapsed and estimated finish time reporting.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/
make

%check
make test

%install
rm -rf %buildroot
make install DESTDIR=${RPM_BUILD_ROOT}
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Time/Progress.pm
%{_mandir}/man3/*


%changelog
* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.700.0-1mdv2011.0
+ Revision: 596056
- update to new version 1.7

* Wed Nov 18 2009 Michael Scherer <misc@mandriva.org> 1.500.0-2mdv2011.0
+ Revision: 467234
- rpm is not arch dependent
- fix summary

* Sun Nov 15 2009 Bruno Cornec <bcornec@mandriva.org> 1.500.0-1mdv2010.1
+ Revision: 466114
- Package creation (Mandatory for SVK)
- create perl-Time-Progress

